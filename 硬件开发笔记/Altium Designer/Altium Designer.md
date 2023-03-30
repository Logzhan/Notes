## Altium Designer 3D 渲染设置 

​         Altium Designer的3D渲染设置，可以在右下角找到Panel, 然后 选择View Configraution

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230319152206373.png" alt="image-20230319152206373" style="zoom: 50%;" />

​        View Configuration的界面如下图所示，在Configuration中我们可以选择不同颜色的板子。比较主要注意的是Projection选项中的Orthographic和Perspective的区别。当我们选择的Orthographic模式的时候，3D渲染会显得非常的畸形。Perspective则是正常的近大远小的透视关系。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230319152314180.png" alt="image-20230319152314180" style="zoom:50%;" />

## Altium Designer 元件的透明度设置

​		在Altium Designer中，选中元件后，可以在properties中设置3D body的Opacity，这个参数可以控制3D渲染时3D元器件的透明度。对于部分对其他遮挡严重的器件，可以适当调整透明度，实现更好的渲染呈现。

## Altium Designer 铺铜隐藏

​		在画电路板的时候，由于铺铜的存在，其会导致其他的线路被掩盖，导致我们无法看清其他的布线，我们可以在View Configuration中找到IObject visibity，