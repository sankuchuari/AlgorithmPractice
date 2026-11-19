<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">E. Avalanche</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/E" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

有从左到右编号为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的一排石堆，第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>号石堆有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>块石子。你还要一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>i</sub></span>。

Alice 和 Bob 玩一个游戏。他们轮流行动，Alice 先行动。在一次行动中，玩家可以选择一个非空的堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>并从它移除一颗石子。然后，每个堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>j</i></span>上都会添加一颗石子，即在堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>左边的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">min(<i>k</i>, <i>i</i>-1)</span>个堆上。如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">max(1, <i>i</i>-<i>k</i>) ≤ <i>j</i> ≤ <i>i</i>-1</span>，那么不添加石子。新石子的供应是无限的。例如，如果<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i> = 5</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 2</span>，那么堆<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>上都会添加一颗石子。

无法做出移动的玩家会输。可以证明该游戏总是会在有限步之后结束。

如果双方玩家都采取最优策略，那么谁会获胜？

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>）。测试用例的描述随后。

第一行每个测试用例包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 ≤ <i>n</i> ≤ 2· 10<sup>5</sup></span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>k</i> ≤ <i>n</i>-1</span>） —— 堆数和游戏的参数。

第二行是每个测试用例的内容，包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0 ≤ a<sub>i</sub> ≤ 10<sup>9</sup></span>）——表示每个堆中石子的数量。

保证所有测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的和不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2· 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果爱丽丝获胜则打印爱丽丝，否则打印鲍勃。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#E06C75;">5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#E06C75;">2 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#E06C75;">1 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#E06C75;">3 2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#E06C75;">0 0 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">6</span><span style="color:#E06C75;">4 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">7</span><span style="color:#E06C75;">0 0 1 0</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">8</span><span style="color:#E06C75;">5 2</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">9</span><span style="color:#E06C75;">1 2 3 4 5</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">10</span><span style="color:#E06C75;">3 1</span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">11</span><span style="color:#E06C75;">2 5 2</span></div></pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">1</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">Alice</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">2</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">Bob</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">3</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">Alice</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">4</span><span style="color:#98C379;"><span style="color:#E5C07B;font-weight:bold;">Alice</span></span></div><div><span style="display:inline-block;width:2.2em;text-align:right;padding-right:10px;margin-right:10px;color:#5C6370;border-right:1px solid #2C313A;user-select:none;">5</span><span style="color:#98C379;"><span style="color:#61AFEF;font-weight:bold;">Bob</span></span></div></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 1</span>且每堆石堆里都只有一块石头。

* 如果 Alice 从第二堆石头中取了一块，第一堆石头的数量就会增加一块，所以第一堆石头有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>块，第二堆石头有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>块。然后 Bob 和 Alice 各从第一堆石头中取了一块，第一堆石头空了，Bob 无法再移动。
* 如果 Alice 从第一堆石子中取走一颗石子，那么 Bob 就必须从第二堆石子中取走一颗石子，这样第一堆石子就会增加一颗石子。 Alice 取走这颗石子，而 Bob 就无法移动了。

在这两种情况下，都是阿丽亚获胜。

在第二组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i> = 2</span>，然后艾丽丝需要从第三堆石头中取一块。然后，第一堆和第二堆各增加了一块石头，所以三堆石头分别含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>、<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>块石头。

* 如果 Bob 从第二堆石头中取了一块，第一堆石头中就会加一块石头，所以第一堆和第二堆石头分别含有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>块，然后 Alice 和 Bob 各从第一堆石头中取了一块，第一堆石头空了， Alice 无法再进行移动。
* 如果 Bob 从第一堆石头中取了一块，那么 Alice 就必须从第二堆石头中取一块，这样第一堆石头就会增加一块石头。 Bob 取了， Alice 就不能再动了。

在这两种情况下，鲍勃获胜。

</div>