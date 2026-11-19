<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">G. 0s and 1s</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2278/problem/G" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

一棵树是一个无环且相连的无向图。

给你一颗有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个节点的树，根节点<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>。每个节点<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>i</i> ≤ <i>n</i></span>) 初始状态为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>i</sub></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>i</sub> ∈ texttt0,texttt1</span>)，并与其关联有一个目标状态<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">y<sub>i</sub></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">y<sub>i</sub> ∈ texttt0,texttt1</span>)。

你想让每个节点的状态都与目标状态一致。为此，你可以允许在根节点注入能量脉冲。每次注入脉冲时，它会按照以下程序通过树传播：

如果当前节点的状态是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt0</span>，则其状态变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt1</span>，且在此节点处脉冲停止。
否则，如果节点的当前状态为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt1</span>，则其状态变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt0</span>，并向每个子节点发送一个脉冲。如果它没有子节点，则脉冲消失。每个发送给子节点的脉冲都遵循相同的传播规则。

判断是否可以通过能量脉冲使每个节点的状态都达到目标状态。如果可行，还需找出实现这一目标所需的最小能量脉冲数。由于这个数值可能非常大，因此请报告该数值对<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>取模的结果。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

输入的第一行为一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>)，表示测试用例的数量。每个测试用例的描述紧随其后。

每一测试用例的第一行包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i> ≤ 2 · 10<sup>5</sup></span>) — 树中的节点数。

接下来的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i>-1</span>行，每行包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>u</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>v</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>u</i>,<i>v</i> ≤ <i>n</i></span>,<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>u</i> ≠ <i>v</i></span>），表示节点<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>u</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>v</i></span>之间的无向边。保证给定的边形成一棵树。

下一行包含一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>i</sub> ∈ texttt0,texttt1</span>的二进制字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>，其中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>i</sub></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>i</i> ≤ <i>n</i></span>,<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>i</sub> ∈ texttt0,texttt1</span>) 表示节点<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>的初始状态。

下一行包含一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的二进制字符串<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">y<sub>i</sub></span>，其中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>i</i> ≤ <i>n</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">y<sub>i</sub> ∈ texttt0,texttt1</span>) 表示节点<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>的目标状态。

每个测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的总和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 · 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果无法使每个节点的状态都等于其目标状态，输出<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-1</span>。否则，打印所需最小的能量脉冲数，模<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">998 244 353</span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">5
1
0
0
1
0
1
3
1 2
1 3
000
011
3
1 2
1 3
000
010
3
1 2
2 3
000
001</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#98C379;">0</span>
<span style="color:#98C379;">1</span>
<span style="color:#98C379;">2</span>
<span style="color:#98C379;">-1</span>
<span style="color:#98C379;">4</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，初始状态已经与目标状态相同。因此，不需要能量脉冲，答案是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>。

在第二组测试案例中，树中只有根节点。初始状态下，它的状态是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">x<sub>1</sub> = texttt0</span>。

在根注入一次脉冲后，其状态变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt1 = y<sub>1</sub></span>，脉冲随即停止。因此，答案是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>。

对于第三组测试案例，需要<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>脉冲。以下图像展示了这两个脉冲通过树木的传播。

两个脉冲的传播。脉冲<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>产生状态<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt100</span>，而脉冲<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>传播以达到目标<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">texttt011</span>。

</div>