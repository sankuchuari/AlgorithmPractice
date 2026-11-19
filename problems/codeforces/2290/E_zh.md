<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">E. Avalanche</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/E" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

共有 CFTOKEN0 个石堆排成一行，从左到右依次为 CFTOKEN1 到 CFTOKEN2。第 CFTOKEN3 个石堆中有 CFTOKEN4 块石子。此外，你还被给定一个整数 CFTOKEN5。

Alice 和 Bob 玩一个游戏。他们轮流行动，Alice 先行动。在一次行动中，玩家选择一个非空的堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>，并从它移除一颗石子。然后，每个堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>j</i></span>都会添加一颗石子，即在堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>的左侧<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">min(<i>k</i>, <i>i</i>-1)</span>个堆。如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">max(1, <i>i</i>-<i>k</i>) ≤ <i>j</i> ≤ <i>i</i>-1</span>，那么不添加石子。新石子的供应是无限的。例如，如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i> = 5</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 2</span>，那么堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>都会添加一颗石子。

无法做出移动的玩家会输。可以证明该游戏总是会在有限数量的移动后结束。

如果双方玩家都采取最优策略，那么最终的胜者会是谁？

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>)。测试用例的描述随后出现。

每一测试用例的第一行包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 ≤ <i>n</i> ≤ 2· 10<sup>5</sup></span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>k</i> ≤ <i>n</i>-1</span>）—— 棋盘的个数和游戏的参数。

每一测试用例的第二行包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0 ≤ a<sub>i</sub> ≤ 10<sup>9</sup></span>）——表示每堆石子的数量。

每个测试案例的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>总和保证不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2· 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果爱丽丝获胜则打印爱丽丝，否则打印鲍勃。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">5
2 1
1 1
3 2
0 0 1
4 1
0 0 1 0
5 2
1 2 3 4 5
3 1
2 5 2</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#E5C07B;font-weight:bold;">Alice</span>
<span style="color:#61AFEF;font-weight:bold;">Bob</span>
<span style="color:#E5C07B;font-weight:bold;">Alice</span>
<span style="color:#E5C07B;font-weight:bold;">Alice</span>
<span style="color:#61AFEF;font-weight:bold;">Bob</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 1</span>和每一堆都包含一块石头。

如果 Alice 从第二堆石头中取走一块石头，第一堆石头的数量就会增加一块，因此第一堆石头含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>块，第二堆石头含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>块。然后，Bob 和 Alice 各从第一堆石头中取走一块石头，Bob 无法再进行移动。
如果 Alice 从第一堆石子中取走一块石子，那么 Bob 必须从第二堆石子中取走一块石子，这样第一堆石子就会增加一块石子。然后 Alice 取走这块石子，而 Bob 将无法移动。

在这种情况下，Alice 赢。

在第二组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 2</span>，然后艾丽丝需要从第三堆石头中取一块。然后，第一堆和第二堆各增加了一块石头，因此第一堆和第二堆分别含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>块石头。

如果 Bob 从第二堆石头中取走一块石头，第一堆石头中会增加一块石头，因此第一堆和第二堆石头分别含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>块石头。然后 Alice 和 Bob 各从第一堆石头中取走一块石头，Alice 无法再进行移动。
如果 Bob 从第一堆石头中取走一块石头，那么 Alice 必须从第二堆石头中取走一块石头，这样第一堆石头就会增加一块石头。然后 Bob 取走那块石头，而 Alice 无法再进行移动。

在这种情况下，鲍勃获胜。

</div>