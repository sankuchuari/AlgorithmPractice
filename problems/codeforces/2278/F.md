<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">F. Modulo and Counting</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">512 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/F" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

You are given two integers<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>.

An array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>of length<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>is called good if it satisfies the following two conditions:

*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">colorredm + 2 ≥ a<sub>1</sub> ≥ a<sub>2</sub> ≥ … ≥ a<sub>n-1</sub> ≥ a<sub>n</sub> ≥ 1</span>;
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(a<sub>1</sub>  mod  a<sub>2</sub>) + (a<sub>2</sub>  mod  a<sub>3</sub>) + … + (a<sub>n-1</sub>  mod  a<sub>n</sub>) = <i>m</i></span>.

Your task is to find the number of good arrays. Since the answer can be very large, report it modulo<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

The first line of the input contains a single integer<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 2 000</span>) — the number of test cases. The description of each test case follows.

The only line of each test case contains two space-separated integers<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 ≤ <i>n</i> ≤ 4 000</span>;<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>m</i> ≤ 4 000</span>).

It is guaranteed that the sum of<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>over all the test cases does not exceed<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4000</span>and the sum of<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>over all the test cases does not exceed<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4000</span>.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

For each test case, print the number of good arrays. As the answer can be large, output it modulo<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">6</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">3 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">3 2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">6 7</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">41 67</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">998 244</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">353 420</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#98C379;">3</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#98C379;">1</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#98C379;">60</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#98C379;">972763487</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#98C379;"><span style="color:#98C379;">288208692</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#98C379;"><span style="color:#98C379;">566410295</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

For the first test case, the good arrays are:

*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 2, 1]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  2) + (2  mod  1) = 1 + 0 = 1</span>.
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 2, 2]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  2) + (2  mod  2) = 1 + 0 = 1</span>.
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[3, 3, 2]</span>:<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3  mod  3) + (3  mod  2) = 0 + 1 = 1</span>.

For the second test case, the only good array is<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[4, 3, 2]</span>.

</div>