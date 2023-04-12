 

# 使用颜色突出显示网络——Altium Designer 笔记

*   [在原理图编辑器中设置网络颜色](#_4)
*   [在 PCB 编辑器中设置网络颜色](#_PCB__20)
*   *   [在 PCB 中网络的两种表示方式](#_PCB__23)
    *   [在 PCB 中网络的两个颜色设置](#_PCB__33)
    *   *   [基本模式——图层和网络颜色的混合图案](#_53)
        *   [缩小行为——图层或网络颜色占主导](#_60)
    *   [设置和显示网络颜色](#_84)
*   [在原理图和 PCB 之间传输颜色](#_PCB__102)

在[原理图](https://so.csdn.net/so/search?q=%E5%8E%9F%E7%90%86%E5%9B%BE&spm=1001.2101.3001.7020)编辑器中设置网络颜色
=====================================================================================================

  使用 view > Set Net Colors 命令，可以在原理图编辑器中将高亮颜色应用于网络或总线。**请注意，网络颜色设置无法撤消**，要删除颜色设置，请使用 “Clear Net Color” 命令或 “Clear All Net Colors” 命令。

![在这里插入图片描述](https://img-blog.csdnimg.cn/9d309b678fac4388a06cb803f34b4ecb.png?x-oss-process=image,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_13,color_FFFFFF,t_70,g_se,x_16#pic_center)

设置原理图网络颜色

 

![在这里插入图片描述](https://img-blog.csdnimg.cn/fce84713b7cf4e46aa67d61049d65bf8.png#pic_center)

网络颜色效果图

  

在 PCB 编辑器中设置网络颜色
================

在 PCB 中网络的两种表示方式
----------------

  在 PCB 编辑器中，一个网络有两种表示方式；作为未布线的**连接线**或由一系列轨道段定义的**布线网络**。

![在这里插入图片描述](https://img-blog.csdnimg.cn/57a7a6d8b7cb4df8ba912506da9c97c3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

连接线和布线网络

  

在 PCB 中网络的两个颜色设置
----------------

  在 PCB 编辑器中，一个网络有两个颜色设置；**图层** (layer) 颜色和**网络**颜色。网络颜色始终应用于连接线。布线网络可以以图层颜色或网络颜色显示。


![在这里插入图片描述](https://img-blog.csdnimg.cn/b77a9f3e75624e81994361fd6d45e4d1.png#pic_center)

图层颜色

  

![在这里插入图片描述](https://img-blog.csdnimg.cn/68cba868c811419eba4aa39696fb125f.png#pic_center)

网络颜色

  

![在这里插入图片描述](https://img-blog.csdnimg.cn/34f4acb3865047f98315035bb2d4ef69.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

图层颜色和网络颜色效果图（**开和关闭可以通过F5完成开启和关闭**）

  

### 基本模式——图层和网络颜色的混合图案

  打开首选项（界面右上角齿轮图案），在 PCB Editor > Board Insight Color Overrides 界面可以设置图层颜色和网络颜色混合的基本图案。

![在这里插入图片描述](https://img-blog.csdnimg.cn/de7bab4d458046538d982fa60c198638.png#pic_center)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c08f31ef94714459bc1781b70c1485d0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 缩小行为——图层或网络颜色占主导

  打开首选项（界面右上角齿轮图案），在 PCB Editor > Board Insight Color Overrides 界面可以设置缩小行为。

缩小时，此显示行为可以是：

*   缩小时保持不变（基本图案比例），或
*   图案可以逐渐消失以恢复图层颜色（图层颜色占主导地位），或
*   覆盖颜色 (即网络颜色) 可以加强（覆盖颜色占主导地位）。

![在这里插入图片描述](https://img-blog.csdnimg.cn/ce449c4bd0e247b2b06a278705b731e7.png#pic_center)

缩小时保持不变（基本图案比例）

![在这里插入图片描述](https://img-blog.csdnimg.cn/8696b749d33040cf89d6f41a42dde414.png#pic_center)

图案可以逐渐消失以恢复图层颜色（图层颜色占主导地位）

![在这里插入图片描述](https://img-blog.csdnimg.cn/21d5bed5306a490abcf0e01abb9296b0.png#pic_center)

覆盖颜色 (即网络颜色) 可以加强（覆盖颜色占主导地位）

  

设置和显示网络颜色
---------

  在 PCB 编辑器的 PCB 面板中 (如果没有此面板，左下角 Panels 可以调出) ，选择 `Nets` 模式，点击 `All Net` 显示所有网络，右键单击选定的网络并选择 `Change Net Color` 命令可以设置网络颜色。  
  

![在这里插入图片描述](https://img-blog.csdnimg.cn/7c87804e10634f1a90796e04aee284fa.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

设置 PCB 网络颜色

  

  布线网络默认是显示为其所在图层的**图层颜色**，要显示**网络颜色**则需要如上图所示，勾选网络以启用网络颜色。如果勾选后没有显示网络颜色，可以按下快捷键 F5 全局启用 / 禁用网络颜色显示，或在右下角 Panels 调出 View Configuration 面板，然后在 View Options 标签中使用 Net Color Override 按钮启用 / 禁用网络颜色显示。

![在这里插入图片描述](https://img-blog.csdnimg.cn/99f737d065d54a55a5d28e3b241d1e81.png?x-oss-process=image,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_9,color_FFFFFF,t_70,g_se,x_16#pic_center)

![在这里插入图片描述](https://img-blog.csdnimg.cn/e7e8bef9bb6c4ea9b28c30655c134470.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center)

在原理图和 PCB 之间传输颜色
================

  通过 Design > Update 命令，可以在原理图和 PCB 编辑器之间（双向）传输网络颜色。在工程变更单 (ECO) 中仅需勾选 Change Net Colors 项中的变更即可。

![在这里插入图片描述](https://img-blog.csdnimg.cn/ad8e44b2bcd444e192675ac54567ff55.png?x-oss-process=image,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)


如果颜色没有转移，请检查 Project > Project Options 对话框中是否启用了以下选项 ：

*   Comparato 选项卡：与网络相关的差异 —— 更改网络颜色
*   ECO Generation 选项卡：与网络相关的修改 —— 更改网络颜色

![在这里插入图片描述](https://img-blog.csdnimg.cn/3e426ad191c74b48ae077d306dc3839a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

![在这里插入图片描述](https://img-blog.csdnimg.cn/ee674ac8152b41caa776a2f551300450.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAQmVuQmVuRjE5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)