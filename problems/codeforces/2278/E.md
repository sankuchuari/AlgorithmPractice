<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">E. Swap and Negate</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/E" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

You are given an array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>of length<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>.

You are allowed to perform the following operation on the array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>any number of times (including zero):

* Choose an index<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>such that<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>i</i>  <  <i>n</i></span>;
* Set<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>i</sub> := -a<sub>i+1</sub></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>i+1</sub> := -a<sub>i</sub></span>simultaneously.

Determine the maximum possible sum of all elements in the array that can be achieved by performing the operations optimally.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

The first line of the input contains a single integer<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>) — the number of test cases. The description of each test case follows.

The first line of each test case contains a single integer<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i> ≤ 2·10<sup>5</sup></span>) — the length of the array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>.

The second line of each test case contains<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>integers<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-10<sup>9</sup> ≤ a<sub>i</sub> ≤ 10<sup>9</sup></span>) — the elements of the array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>.

It is guaranteed that the sum of<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>over all test cases does not exceed<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2·10<sup>5</sup></span>.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

For each test case, print a single integer — the maximum possible sum of the array elements after performing the operations any number of times.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">-3</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">1 -2 -3 4</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">-10 1 0 1 -10</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">8</span><span style="color:#E06C75;">2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">9</span><span style="color:#E06C75;">6 -7</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#98C379;">-3</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#98C379;">10</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#98C379;">18</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#98C379;">1</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

For the first test case, no operation can be performed. Hence, the maximum sum will be equal to<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-3</span>.

For the second test case, choosing<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i> = 2</span>makes the array<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i> = [1, 3, 2, 4]</span>. Now, the sum of all the elements is equal to<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">10</span>. It can be shown that this is the maximum possible.

</div>