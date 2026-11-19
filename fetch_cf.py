import operator
import os
import platform
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright
import html as html_lib

_MLX_CACHE = None

BS = chr(92)
DL = chr(36)
SL = chr(47)
GET0 = operator.itemgetter(0)

LATEX_SYMBOLS = {
    BS + "lt": "<",
    BS + "gt": ">",
    BS + "le": "≤",
    BS + "leq": "≤",
    BS + "ge": "≥",
    BS + "geq": "≥",
    BS + "ne": "≠",
    BS + "neq": "≠",
    BS + "cdot": "·",
    BS + "times": "×",
    BS + "pm": "±",
    BS + "mp": "∓",
    BS + "infty": "∞",
    BS + "sum": "∑",
    BS + "prod": "∏",
    BS + "max": "max",
    BS + "min": "min",
    BS + "gcd": "gcd",
    BS + "lcm": "lcm",
    BS + "log": "log",
    BS + "ln": "ln",
    BS + "bmod": " mod ",
    BS + "pmod": " mod ",
    BS + "to": "→",
    BS + "rightarrow": "→",
    BS + "leftarrow": "←",
    BS + "leftrightarrow": "↔",
    BS + "Rightarrow": "⇒",
    BS + "in": "∈",
    BS + "notin": "∉",
    BS + "subset": "⊂",
    BS + "subseteq": "⊆",
    BS + "cup": "∪",
    BS + "cap": "∩",
    BS + "emptyset": "∅",
    BS + "forall": "∀",
    BS + "exists": "∃",
    BS + "oplus": "⊕",
    BS + "otimes": "⊗",
    BS + "land": "∧",
    BS + "lor": "∨",
    BS + "lnot": "¬",
    BS + "alpha": "α",
    BS + "beta": "β",
    BS + "gamma": "γ",
    BS + "delta": "δ",
    BS + "epsilon": "ε",
    BS + "varepsilon": "ε",
    BS + "theta": "θ",
    BS + "lambda": "λ",
    BS + "mu": "μ",
    BS + "pi": "π",
    BS + "sigma": "σ",
    BS + "phi": "φ",
    BS + "omega": "ω",
    BS + "Delta": "Δ",
    BS + "Sigma": "Σ",
    BS + "Omega": "Ω",
    BS + "dots": "…",
    BS + "ldots": "…",
    BS + "cdots": "⋯",
    BS + "lfloor": "⌊",
    BS + "rfloor": "⌋",
    BS + "lceil": "⌈",
    BS + "rceil": "⌉",
    BS + "{": "{",
    BS + "}": "}",
    BS + " ": " ",
    BS + ",": " ",
    BS + ";": " ",
    BS + "quad": "  ",
}

def build_url(*parts):
    return SL.join(str(x).strip(SL) for x in parts)

def get_system_proxy():
    proxies = urllib.request.getproxies()
    for key in ("https", "http", "all", "socks", "socks5"):
        if proxies.get(key):
            p = proxies[key]
            return p if "://" in p else f"http:{SL}{SL}{p}"

    if platform.system() == "Darwin":
        try:
            out = subprocess.check_output(["scutil", "--proxy"], text=True)
            if "HTTPEnable : 1" in out:
                h = re.search(r"HTTPProxy\s*:\s*\((\S+)\)", out)
                pt = re.search(r"HTTPPort\s*:\s*(\d+)", out)
                if h and pt:
                    return f"http:{SL}{SL}{h.group(1)}:{pt.group(1)}"
            if "SOCKSEnable : 1" in out:
                h = re.search(r"SOCKSProxy\s*:\s*\((\S+)\)", out)
                pt = re.search(r"SOCKSPort\s*:\s*(\d+)", out)
                if h and pt:
                    return f"socks5:{SL}{SL}{h.group(1)}:{pt.group(1)}"
        except Exception:
            pass

    return None


def tex_to_html(tex):
    s = html_lib.unescape(tex.strip())
    p_frac = re.escape(BS) + r"frac\{([^{}]+)\}\{([^{}]+)\}"
    s = re.sub(p_frac, r"(\1)/(\2)", s)
    s = re.sub(re.escape(BS) + r"sqrt\{([^{}]+)\}", r"√(\1)", s)
    p_txt = re.escape(BS) + r"(?:text|texttt|textsf|mathrm|mathbf|mathit|mathcal)\{([^{}]+)\}"
    s = re.sub(p_txt, r"\1", s)
    for cmd in sorted(LATEX_SYMBOLS.keys(), key=len, reverse=True):
        s = s.replace(cmd, LATEX_SYMBOLS[cmd])
    s = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"\^([a-zA-Z0-9])", r"<sup>\1</sup>", s)
    s = re.sub(r"_([a-zA-Z0-9])", r"<sub>\1</sub>", s)
    s = s.replace("{", "").replace("}", "").replace(BS, "")
    s = re.sub(r"(?<![a-zA-Z<>])([a-zA-Z])(?![a-zA-Z<>])", r"<i>\1</i>", s)
    return s

def colorize_output(text):
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.upper() in ("YES", "ALICE", "FIRST"):
            lines.append(
                f'<span style="color:#E5C07B;font-weight:bold;">{line}</span>'
            )
        elif stripped.upper() in ("NO", "BOB", "SECOND"):
            lines.append(
                f'<span style="color:#61AFEF;font-weight:bold;">{line}</span>'
            )
        else:
            lines.append(f'<span style="color:#98C379;">{line}</span>')
    return "\n".join(lines)

def route_handler(route):
    if "mathjax" in route.request.url.lower():
        route.abort()
    else:
        route.continue_()

def grab_html(p, url, selector, use_proxy=None, timeout_ms=8000):
    base_args = ["--disable-blink-features=AutomationControlled"]
    launch_opts = {"headless": True}
    if use_proxy:
        launch_opts["proxy"] = {"server": use_proxy}
        launch_opts["args"] = base_args
    else:
        launch_opts["args"] = base_args + ["--no-proxy-server"]

    br = p.chromium.launch(**launch_opts)
    try:
        ua = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
        ctx = br.new_context(user_agent=ua, ignore_https_errors=True)
        pg = ctx.new_page()
        pg.route("**/*", route_handler)
        pg.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
        pg.wait_for_selector(selector, timeout=timeout_ms)
        return pg.inner_html(selector)
    finally:
        br.close()

def smart_fetch(p, url, selector, proxy_url):
    for attempt in range(1, 4):
        try:
            print(f"Direct attempt {attempt}/3: {url}", flush=True)
            html = grab_html(p, url, selector, use_proxy=None, timeout_ms=8000)
            print("Direct connection succeeded!", flush=True)
            return html
        except Exception as e:
            print(f"Direct attempt {attempt} failed: {e}", flush=True)

    if not proxy_url:
        raise RuntimeError("Direct failed 3 times and no proxy found.")
    print(f"Switching to proxy: {proxy_url}", flush=True)
    return grab_html(p, url, selector, use_proxy=proxy_url, timeout_ms=25000)

def translate_md(p, text, proxy_url):
    global _MLX_CACHE
    lines = text.splitlines()
    idxs, batch = [], []
    for i, line in enumerate(lines):
        st = line.strip()
        if st and not re.fullmatch(r"(CFTOKEN\d+END\s*)+", st):
            idxs.append(i)
            batch.append(st)
    if not batch:
        return text

    joined = "\n".join(batch)
    q = urllib.parse.quote(joined)
    gg_url = (
        f"https:{SL}{SL}translate.googleapis.com{SL}translate_a{SL}single"
        f"?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
    )
    for use_px in ([None, proxy_url] if proxy_url else [None]):
        opts = {"headless": True}
        if use_px:
            opts["proxy"] = {"server": use_px}
        else:
            opts["args"] = ["--no-proxy-server"]
        br = p.chromium.launch(**opts)
        try:
            ctx = br.new_context(ignore_https_errors=True)
            data = ctx.request.get(gg_url, timeout=5000).json()
            zh_lines = "".join(seg[0] for seg in data[0] if seg[0]).splitlines()
            if len(zh_lines) == len(idxs):
                for i, zh in zip(idxs, zh_lines):
                    lines[i] = re.sub(r"\s*(CFTOKEN\d+END)\s*", r" \1 ", zh).strip()
                return "\n".join(lines)
        except Exception:
            pass
        finally:
            br.close()

    is_apple_silicon = (
            platform.system() == "Darwin" and platform.machine() == "arm64"
    )

    if is_apple_silicon:
        try:
            os.environ["HF_HUB_OFFLINE"] = "1"
            from mlx_lm import load, generate

            print("Translating with M-series local MLX model...", flush=True)
            if _MLX_CACHE is None:
                _MLX_CACHE = load("mlx-community/Qwen2.5-3B-Instruct-4bit")
            model, tokenizer = _MLX_CACHE

            for i, s in zip(idxs, batch):
                prompt = tokenizer.apply_chat_template(
                    [
                        {
                            "role": "system",
                            "content": "你是算法竞赛翻译专家。将所有英文单词和句子全部翻译为简体中文，原样保留所有 CFTOKEN...END 占位符，只输出译文，不要任何解释，输出前请逐子检查是否有漏翻译的单词。",
                        },
                        {"role": "user", "content": s},
                    ],
                    tokenize=False,
                    add_generation_prompt=True,
                )
                zh = generate(
                    model, tokenizer, prompt=prompt, max_tokens=512, verbose=False
                )
                lines[i] = re.sub(r"\s*(CFTOKEN\d+END)\s*", r" \1 ", zh).strip()
            return "\n".join(lines)
        except Exception as e:
            print(f"MLX fallback warning: {e}", flush=True)

    try:
        import argostranslate.translate

        print("Translating with local Argos neural model...", flush=True)
        for i, s in zip(idxs, batch):
            zh = argostranslate.translate.translate(s, "en", "zh")
            lines[i] = re.sub(r"\s*(CFTOKEN\d+END)\s*", r" \1 ", zh).strip()
        return "\n".join(lines)
    except Exception as e:
        print(f"Local translation skipped: {e}", flush=True)

    return "\n".join(lines)


def parse_and_save(p, contest_id, index, url, html, proxy_url):
    print(f"Parsing {contest_id}{index.upper()}...", flush=True)
    tokens = {}

    def put(val):
        k = f"CFTOKEN{len(tokens)}END"
        tokens[k] = val
        return k

    def rep_blk(m):
        h = tex_to_html(m.group(1))
        st = "margin:12px 0;font-size:1.15em;color:#E6EDF3;"
        return put(f'\n\n<div align="center" style="{st}">{h}</div>\n\n')

    def rep_inl(m):
        h = tex_to_html(m.group(1))
        st = (
            "font-family:Georgia,serif;font-size:1.06em;"
            "color:#A5D6FF;padding:0 2px;"
        )
        return put(f'<span style="{st}">{h}</span>')

    d3 = re.escape(DL * 3)
    d6 = re.escape(DL * 6)
    html = re.sub(f"{d6}(.+?){d6}", rep_blk, html, flags=re.S)
    html = re.sub(f"{d3}(.+?){d3}", rep_inl, html, flags=re.S)

    soup = BeautifulSoup(html, "html.parser")
    header_md = ""
    header_div = soup.find("div", class_="header")
    if header_div:
        t_el = header_div.find("div", class_="title")
        tl_el = header_div.find("div", class_="time-limit")
        ml_el = header_div.find("div", class_="memory-limit")
        title = t_el.get_text(strip=True) if t_el else ""
        tl = (
            tl_el.get_text().replace("time limit per test", "").strip()
            if tl_el
            else ""
        )
        ml = (
            ml_el.get_text().replace("memory limit per test", "").strip()
            if ml_el
            else ""
        )
        h_html = (
            '<div align="center" style="margin-bottom:16px;">\n'
            f'  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">{title}</h1>\n'
            '  <div style="color:#ABB2BF;font-size:0.95em;">'
            f'<b>time:</b> <span style="color:#98C379;">{tl}</span> | '
            f'<b>memory:</b> <span style="color:#61AFEF;">{ml}</span> | '
            f'<a href="{url}" style="color:#56B6C2;">Open in Browser</a>'
            "</div>\n</div>\n"
            '<hr style="border-color:#3E4451;">\n\n'
        )
        header_md = put(h_html)
        header_div.decompose()

    h2_st = (
        "color:#FFF;font-weight:700;font-size:1.3em;"
        "margin:22px 0 10px 0;border-bottom:1px solid #3E4451;"
        "padding-bottom:4px;"
    )
    for sec in soup.find_all("div", class_="section-title"):
        txt = sec.get_text(strip=True)
        if txt.lower() == "example":
            sec.decompose()
        else:
            sec.replace_with(put(f'\n\n<h2 style="{h2_st}">{txt}</h2>\n\n'))

    for tt in soup.find_all(["tt", "code"]):
        txt = tt.get_text()
        base = "background:#2C313A;padding:1px 5px;border-radius:4px;"
        if txt.strip() in ("Alice", "YES", "Yes"):
            st = base + "color:#E5C07B;font-weight:bold;"
            tt.replace_with(put(f'<code style="{st}">{txt}</code>'))
        elif txt.strip() in ("Bob", "NO", "No"):
            st = base + "color:#61AFEF;font-weight:bold;"
            tt.replace_with(put(f'<code style="{st}">{txt}</code>'))
        else:
            st = base + "color:#E06C75;"
            tt.replace_with(put(f'<code style="{st}">{txt}</code>'))

    def with_line_numbers(raw_text, text_color):
        rows = []
        for row_idx, line in enumerate(raw_text.splitlines(), 1):
            num_st = (
                "display:inline-block;width:2.2em;text-align:right;"
                "padding-right:10px;margin-right:10px;color:#5C6370;"
                "border-right:1px solid #2C313A;user-select:none;"
            )
            rows.append(
                f'<div><span style="{num_st}">{row_idx}</span>'
                f'<span style="color:{text_color};">{line}</span></div>'
            )
        return "".join(rows)

    for sdiv in soup.find_all("div", class_="sample-test"):
        ins = sdiv.find_all("div", class_="input")
        outs = sdiv.find_all("div", class_="output")
        s_html = f'\n\n<h2 style="{h2_st}">Example</h2>\n\n'
        box = (
            "width:96%;margin:0 auto 16px auto;"
            "border:1px solid #3E4451;border-radius:6px;overflow:hidden;"
        )
        hdr = (
            "background:#21252B;padding:7px 14px;"
            "color:#FFF;font-weight:bold;font-size:1.05em;"
            "border-bottom:1px solid #3E4451;"
        )
        pre_st = (
            "margin:0;width:100%;display:block;"
            "font-family:JetBrains Mono,monospace;"
            "font-size:1.05em;line-height:1.5;background:transparent;"
        )
        for inp, out in zip(ins, outs):
            ip = inp.find("pre")
            op = out.find("pre")
            for pre in (ip, op):
                if pre:
                    for br in pre.find_all(["br", "div"]):
                        br.replace_with("\n" + br.get_text())
            it = with_line_numbers(ip.get_text().strip() if ip else "", "#E06C75")
            ot = with_line_numbers(
                colorize_output(op.get_text().strip() if op else ""), "#98C379"
            )
            s_html += (
                f'<div style="{box}">\n'
                f'  <div style="{hdr}">Input</div>\n'
                f'  <div style="background:#1B1E23;padding:10px 14px;">'
                f'<pre style="{pre_st}">{it}</pre></div>\n'
                f'  <div style="{hdr}border-top:1px solid #3E4451;">Output</div>\n'
                f'  <div style="background:#1B1E23;padding:10px 14px;">'
                f'<pre style="{pre_st}">{ot}</pre></div>\n'
                "</div>\n\n"
            )
        sdiv.replace_with(put(s_html))

    body_en = md(str(soup), heading_style="ATX")
    print("Translating to Chinese...", flush=True)
    body_zh = translate_md(p, body_en, proxy_url)

    out_dir = f"problems{SL}codeforces{SL}{contest_id}"
    os.makedirs(out_dir, exist_ok=True)
    wrap_st = "font-size:1.12em;line-height:1.65;color:#DCDFE4;"

    for suffix, body in [("", body_en), ("_zh", body_zh)]:
        full = header_md + f'<div style="{wrap_st}">\n\n{body}\n\n</div>'
        for k, v in tokens.items():
            num = k.replace("CFTOKEN", "").replace("END", "")
            full = re.sub(
                rf"\s*CFTOKEN\s*{num}\s*END\s*",
                lambda _: str(v),
                full,
                flags=re.IGNORECASE,
            )
        path = f"{out_dir}{SL}{index.upper()}{suffix}.md"
        with open(path, "w", encoding="utf-8") as f:
            f.write(re.sub(r"\n{3,}", "\n\n", full).strip())
        print(f"Saved: {path}", flush=True)


def run(contest_id, index=None):
    proxy_url = get_system_proxy()
    category = "gym" if int(contest_id) >= 100000 else "contest"
    base_host = f"https:{SL}{SL}codeforces.com"

    with sync_playwright() as p:
        if index:
            indices = [index.upper()]
        else:
            contest_url = build_url(base_host, category, contest_id)
            print(f"Fetching contest problem list: {contest_url}", flush=True)
            table_html = smart_fetch(p, contest_url, "table.problems", proxy_url)
            soup = BeautifulSoup(table_html, "html.parser")
            indices = []
            for td in soup.find_all("td", class_="id"):
                a = td.find("a")
                if a:
                    code = a.get_text(strip=True).upper()
                    if code and code not in indices:
                        indices.append(code)
            print(f"Found {len(indices)} problems: {', '.join(indices)}", flush=True)

        for idx in indices:
            prob_url = build_url(base_host, category, contest_id, "problem", idx)
            html = smart_fetch(p, prob_url, ".problem-statement", proxy_url)
            parse_and_save(p, contest_id, idx, prob_url, html, proxy_url)


if __name__ == "__main__":
    args = list(sys.argv)
    args.pop(0)
    if len(args) >= 2:
        run(args.pop(0), args.pop(0))
    elif len(args) == 1:
        run(args.pop(0))
    else:
        print("Usage: python fetch_cf.py <contest_id> [index]")
