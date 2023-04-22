Altium Designer 常见问题解决方案

## 一、元件无法对齐 & 元件拖动步距过大

​		这是以为栅格的最小步长太小了，元件存在拖动无法对齐的问题。解决方案：视图(View) -> 栅格(Gird) -> 设置捕捉栅格(Set Snap Gird)。点击后弹出对话框，我们可以把最小的栅格修改变小。那么画图的时候会更加精确。

二、原理图修改样式和尺寸

​		部分原理图偏小，导致一个项目的原理图需要多个文件才能绘制完。可以把A4的原理图修改为A3.

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230416151604248.png" alt="image-20230416151604248" style="zoom:50%;" />

​		鼠标点击原理图，在右侧的Properties中就可以看到原理图的选项。一般我们选择标准的原理图大小。复杂一点的项目可以选择A3。方向一般选择Landsapce（水平）。Title一般用于记录公司、时间、作者等信息。