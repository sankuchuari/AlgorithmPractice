<div align="center" style="margin-bottom:16px;">
  <h1 style="margin:0 0 6px 0;color:#FFF;font-size:1.7em;">F. Value Counters</h1>
  <div style="color:#ABB2BF;font-size:0.95em;"><b>time:</b> <span style="color:#98C379;">2 seconds</span> | <b>memory:</b> <span style="color:#61AFEF;">256 megabytes</span> | <a href="https://codeforces.com/contest/2290/problem/F" style="color:#56B6C2;">Open in Browser</a></div>
</div>
<hr style="border-color:#3E4451;">

<div style="font-size:1.12em;line-height:1.65;color:#DCDFE4;">

对于长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的排列<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>，定义数组<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub></span>如下：

Initially，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>中的所有元素都等于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">0</span>。然后，考虑<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(<i>x</i>, <i>y</i>)</span>中每一对，它们在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>中位于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i></span>的左侧，并且<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>x</i>  lt  <i>y</i> ≤ <i>n</i></span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>出现在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(<i>x</i>, <i>y</i>)</span>的左侧。对于每一对这样的：

*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>x</sub></span>减去<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>。
*<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>y</sub></span>增加<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>。

注意数组<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i></span>是根据元素的值进行索引的，而不是根据它们的位置：<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>x</sub></span>是计数器，记录在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>中出现的元素<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>的次数。例如，对于<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i> = [2, 1, 3]</span>，配对是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(1, 3)</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(2, 3)</span>，因此<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>b</i> = [-1, -1, 2]</span>。

给你<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub></span>个整数。找到一个排列<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>，使得这个数组成为该排列的全排列，或者报告不存在这样的排列。

一个长度为<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>的排列是由<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>到<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>之间的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个不同的整数按任意顺序组成的数组。例如，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[2,3,1,5,4]</span>是一个排列，但<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[1,2,2]</span>不是一个排列（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2</span>在数组中重复出现），而且<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[1,3,4]</span>也不是一个排列（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i>=3</span>但数组中包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">4</span>）。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Input</h2>

每个测试包含多个测试用例。第一行包含测试用例的数量<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>t</i></span>(<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>t</i> ≤ 10<sup>4</sup></span>)。测试用例的描述随后出现。

每一测试用例的第一行包含一个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1 ≤ <i>n</i> ≤ 2· 10<sup>5</sup></span>—  permutation 的长度。

第二行每个测试用例包含<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个整数<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub></span>（<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-<i>n</i> ≤ b<sub>x</sub> ≤ <i>n</i></span>）——给定数组。

每个测试案例的<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>总和保证不超过<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">2· 10<sup>5</sup></span>。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Output</h2>

对于每个测试用例，如果不存在这样的排列，则打印<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">-1</span>。否则，打印<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>n</i></span>个<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">p<sub>1</sub>, p<sub>2</sub>, …, p<sub>n</sub></span>整数。

可以证明如果存在这样的排列，那么它是唯一的。

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Example</h2>

<div style="width:96%;margin:0 auto 16px auto;border:1px solid #3E4451;border-radius:6px;overflow:hidden;">
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;">Input</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;color:#E06C75;">5
3
0 -1 1
1
0
2
1 1
4
-2 1 -1 2
3
-1 0 1</pre></div>
  <div style="background:#21252B;padding:7px 14px;color:#FFF;font-weight:bold;font-size:1.05em;border-bottom:1px solid #3E4451;border-top:1px solid #3E4451;">Output</div>
  <div style="background:#1B1E23;padding:10px 14px;"><pre style="margin:0;width:100%;display:block;font-family:JetBrains Mono,monospace;font-size:1.05em;line-height:1.5;background:transparent;"><span style="color:#98C379;">2 3 1</span>
<span style="color:#98C379;">1</span>
<span style="color:#98C379;">-1</span>
<span style="color:#98C379;">3 1 4 2</span>
<span style="color:#98C379;">-1</span></pre></div>
</div>

<h2 style="color:#FFF;font-weight:700;font-size:1.3em;margin:22px 0 10px 0;border-bottom:1px solid #3E4451;padding-bottom:4px;">Note</h2>

在第一组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i> = [2, 3, 1]</span>。唯一一对值<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i>  lt  <i>y</i></span>，使得<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i></span>的左边的是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i> = 2</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i> = 3</span>。因此，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub> = 0</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>2</sub> = -1</span>，和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>3</sub> = 1</span>。这里<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub></span>对应于值<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">1</span>，它是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i></span>的最后一个元素。

在第三组测试用例中，置换<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[1, 2]</span>给出<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub> = -1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>2</sub> = 1</span>；而置换<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">[2, 1]</span>给出<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub> = 0</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>2</sub> = 0</span>。因此，没有任何置换给出<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub> = 1</span>和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>2</sub> = 1</span>。

在第四组测试案例中，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>p</i> = [3, 1, 4, 2]</span>。<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i>  lt  <i>y</i></span>中的值对，使得<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>x</i></span>在<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;"><i>y</i></span>的左边，分别是<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(1, 2)</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(1, 4)</span>，和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">(3, 4)</span>。因此，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>1</sub> = -2</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>2</sub> = 1</span>，<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>3</sub> = -1</span>，和<span style="font-family:Georgia,serif;font-size:1.06em;color:#A5D6FF;padding:0 2px;">b<sub>4</sub> = 2</span>。

</div>