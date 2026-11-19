<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">A. Three Piles</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">1 second</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/A" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

There are three piles of stones. The first pile contains<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>stones, the second pile contains<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>stones, and the third pile contains<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>c</i></span>stones.

You must make exactly one move: take one stone from one of the piles and put it on one of the other two piles. You cannot skip this move, and you cannot make more than one move.

Determine whether you can make this move so that all three piles contain the same number of stones.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

Each test contains multiple test cases. The first line contains the number of test cases<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 1000</span>). The description of the test cases follows.

The only line of each test case contains three integers<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>,<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>, and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>c</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>a</i> ≤ <i>b</i> ≤ <i>c</i> ≤ 10</span>) — the numbers of stones in the first, second, and third piles.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

For each test case, print "YES" if you can make the move so that all three piles contain the same number of stones, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">6</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">1 2 3</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">2 2 2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">3 4 5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">1 1 4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">8 9 10</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">3 5 7</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">YES</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">YES</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">YES</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">NO</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

In the first test case, you can take a stone from the third pile and put it on the first pile. Then each pile contains<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>stones.

In the second test case, all piles already contain the same number of stones. However, a move is mandatory, and after any move the piles no longer contain the same number of stones.

In the fourth test case, two moves would be enough to make each pile contain<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>stones, but only one move is allowed. After any single move, the piles do not contain the same number of stones.

</div>