# Altium Designer必要设置

一、Altium Designer的层叠设置

​		如下图所示，在设计(Design)选项中可以找到Layer Stack Manager，其描述如下图所示：

<img src="E:\技术武器库\技术开发笔记\硬件开发笔记\Altium Designer\Image\PCB_LayerStackSetting.jpg" style="zoom: 33%;" />

​		

| 层次描述     | 作用                                                         | 注解                                                    |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
| Top Overlay  | Top Overlay是指PCB板顶部的覆盖层，通常包括PCB板的标识、标志、文字、线条和图形等信息。<br/>Top Overlay层通常是由PCB设计师在设计软件中添加的，用于标识和说明PCB板上各个元件、电路和功能的位置和用途。 | 一般是需要在最顶层或者最底层。                          |
| Dielectric   | 这个层是绝缘层，用于不同层之间绝缘                           |                                                         |
| Signal & Gnd | 信号层或者地层                                               | 上图稚晖君把GND放在第三层，如果有射频可以考虑放在第二层 |

