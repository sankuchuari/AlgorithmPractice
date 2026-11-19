<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">A. Three Piles</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">1 second</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/A" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

有三堆石子。第一堆有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>颗石子，第二堆有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>颗石子，第三堆有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>c</i></span>颗石子。

你必须做出一次移动：从一个堆中取一块石头并放到另一个任意两个堆中的一个。你不能跳过这个移动，也不能做出超过一次的移动。

判断是否可以移动，使得三堆石子的数量相同。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 1000</span>)。测试用例的描述随后出现。

每一测试用例的第一行包含三个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>a</i></span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>c</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>a</i> ≤ <i>b</i> ≤ <i>c</i> ≤ 10</span>）——第一堆，第二堆和第三堆石子的数量。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果可以通过移动使得三堆石子数量相同，则打印 "YES"，否则打印 "NO"。

答案可以以任何形式输出（大写或小写）。例如，“yEs”，“yes”，“Yes”，“YES”都将被识别为积极回答。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">6
1 2 3
2 2 2
3 4 5
1 1 4
8 9 10
3 5 7</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span>
<span style="color:#E5C07B;font-weight:bold;">YES</span>
<span style="color:#61AFEF;font-weight:bold;">NO</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，你可以从第三堆中取一块石头放到第一堆。然后每堆石头的数量都是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>。

在第二组测试案例中，所有堆已经包含相同数量的石子。然而，必须进行一次移动，在任何一次移动之后，堆不再包含相同数量的石子。

在第四组测试案例中，只需要两次移动就可以使得每一堆石子数量变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>颗石子，但是只允许进行一次移动。在任何一次移动之后，每一堆石子都不再包含相同数量的石子。

</div>