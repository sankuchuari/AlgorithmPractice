<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">A. Fraction and Six</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">1 second</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/A" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

You are given two strings<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>, consisting of lowercase English letters.

Interpret the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>as the product of variables written in the numerator of a fraction, and the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>as the product of variables written in the denominator. Each character represents a variable.

Since multiplication is commutative, the variables in both the numerator and the denominator may be reordered arbitrarily. In addition, any variable that appears in both the numerator and the denominator may be cancelled. Note that a single occurrence of a variable in the denominator can only cancel exactly one occurrence of that variable in the numerator and vice versa.

Determine whether it is possible to simplify the fraction so that the resulting expression is exactly equal to the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>. In other words, after performing any number of cancellations and rearrangements, the remaining variables in the numerator must form the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>, and no variables may remain in the denominator.

For example, if<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i>=textttsinx</span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i>=textttn</span>, then the variable<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttn</span>can be cancelled, leaving<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>in the numerator.

 ![](https://espresso.codeforces.com/1ac4929438e4908210cb2bb8872c7d6702fcd18f.png)

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

The first line of the input contains a single integer<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 100</span>) — the number of test cases. The description of each test case follows.

The first line of each test case contains two integers<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i>, <i>m</i> ≤ 100</span>) — the lengths of the strings<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>and<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>, respectively.

The second line of each test case contains a string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>denoting the numerator of the fraction. It is guaranteed that the length of the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>is equal to<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>and that it contains only lowercase English letters.

The third line of each test case contains a string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>denoting the denominator of the fraction. It is guaranteed that the length of the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>q</i></span>is equal to<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>m</i></span>and that it contains only lowercase English letters.

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

For each test case, print "YES" if you can simplify the fraction so that the resulting expression is exactly equal to the string<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">textttsix</span>and "NO" otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">5
4 1
sinx
n
6 7
xixsms
mixsxim
8 5
fixtures
frute
3 3
abc
def
5 10
sixty
codeforces</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

In the first test case, the variable n appears in both the numerator and the denominator, so it can be cancelled. The remaining variables in the numerator are s, i, and x, which can be reordered to obtain six.

In the second test case, after cancelling all possible common variables, the numerator contains only s while the denominator contains only mi. Therefore, the fraction cannot be simplified to six.

In the third test case, the variables f, r, u, t, and e can be cancelled from both sides. The remaining variables in the numerator are s, i, and x, which can be reordered to form six.

</div>