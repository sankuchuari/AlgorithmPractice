<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">G2. Lakeside Trail (Hard Version)</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">4 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/G2" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

这是问题的困难版本。两个版本之间的唯一区别仅在于所有测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的约束、所有测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的和的约束，以及测试用例的数量。

一个围绕湖泊的环形小径由从编号<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个路段组成。第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>个路段的高度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">h<sub>i</sub></span>。对于每个<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>从<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i>+1</span>到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>i</i></span>，路段<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i>-1</span>是相邻的。同样，路段<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>也是相邻的。

这条小路的陡峭程度是相邻两节高度差的最大绝对值。换句话说，陡峭程度是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">max<sub>1 ≤ <i>i</i> ≤ n</sub> ≤ft|h<sub>i</sub> - h<sub>i+1</sub>right|</span>，其中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">h<sub>n+1</sub></span>应该存在并且等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">h<sub>1</sub></span>。

你有<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>单位的土壤。一个单位的土壤可以增加一个区域的高度<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>；可以对同一段使用多个单位。土壤不能被移除，因此高度只能增加。

找到在使用最多<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>单位土壤后，路径的最小可能陡峭程度。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>)。测试用例的描述随后出现。

每一测试用例的第一行包含两个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3 ≤ <i>n</i> ≤ 10<sup>6</sup></span>,<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0 ≤ <i>k</i> ≤ 10<sup>18</sup></span>) — 分区的数量和土壤单位的数量。

第二行包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">h<sub>1</sub>, h<sub>2</sub>, …, h<sub>n</sub></span>个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ h<sub>i</sub> ≤ 10<sup>9</sup></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>）——各部分的高度。

每个测试用例中<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的总和保证不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">10<sup>6</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，打印一个整数——使用最多<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>k</i></span>单位土壤后，路径的最小坡度。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">6
4 3
1 5 2 8
5 5
2 9 4 1 6
3 0
1 4 7
3 100
1 10 1
5 5
4 1 1 1 1
6 14
3 6 2 4 1 5</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#98C379;">5</span>
<span style="color:#98C379;">4</span>
<span style="color:#98C379;">6</span>
<span style="color:#98C379;">0</span>
<span style="color:#98C379;">2</span>
<span style="color:#98C379;">1</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，可以在第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>处使用两单位土壤，在第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>处使用一单位土壤。高度变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3, 5, 3, 8</span>，相邻部分之间的高度差分别为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">5</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">5</span>，最后一个高度差出现在第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>和第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>处。因此陡度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">5</span>。

![](https://espresso.codeforces.com/7fccb31535c51b705254ec886143ddd1e3d42a32.png)

环形被划分为四个路段，每个路段内标有高度。边界处的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">Δ</span>标签显示相邻高度之间的绝对差异，而<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">+2</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">+1</span>则显示新增的土壤。

陡度无法达到：CFTOKEN46段的高度至少为CFTOKEN47，而CFTOKEN48段和CFTOKEN49段与其相邻，因此它们都需要被提升到至少CFTOKEN50的高度，这需要CFTOKEN51单位的土壤。

在第二组测试案例中，可以通过使用<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3 + 1 + 1 = 5</span>单位的土壤将高度变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">5, 9, 5, 2, 6</span>，而陡度变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>。陡度<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>无法实现：第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>节的高度至少为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">9</span>，因此需要将第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>节提升到至少<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">6</span>，这需要<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4 + 2 = 6</span>单位的土壤。

在第三组测试案例中，无法使用土壤。<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>是相邻的，因此陡度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">7 - 1 = 6</span>。

在第四组测试案例中，可以通过使用<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">18</span>单位的土壤将所有高度均设置为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">10</span>。

在第五个测试案例中，可以通过使用<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 + 1 = 2</span>单位的土壤将高度变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4, 2, 1, 1, 2</span>，而陡度变为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>。陡度<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>无法实现：第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>节的高度至少为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>，而第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>节和第<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">5</span>节与其相邻，因此它们需要至少提升到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">3</span>节至少提升到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>，这需要<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2 + 1 + 1 + 2 = 6</span>单位的土壤。

</div>