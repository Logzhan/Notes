## 一、高亮网络

​		这个功能非常的核心，它可以高亮整个网络，可以这个功能观察布线是否完成，线路的整体走势如何。一旦高亮显示网络，那么其他的网络的透明度会降低，甚至进入3D模式，网络也是高亮的。操作步骤如下：

**高亮网络 ：**选中网络、Cirl + 鼠标左键单击

**关闭高亮网络：**选中网络、Cirl + 鼠标左键双击

## 二、Altium Designer 元件的透明度设置

​		在Altium Designer中，选中元件后，可以在properties中设置3D body的Opacity，这个参数可以控制3D渲染时3D元器件的透明度。对于部分对其他遮挡严重的器件，可以适当调整透明度，实现更好的渲染呈现。

## 三、Altium Designer 铺铜隐藏

​		在画电路板的时候，由于铺铜的存在，其会导致其他的线路被掩盖，导致我们无法看清其他的布线，我们可以在View Configuration中找到IObject visibity，