## 一、Room Definition Violation

​		[Room Definition Violation]	GeekIMU.PcbDoc	Advanced PCB	Room Definition: Between Room Sensor 

​		主要解决方案是在DRC检查的时候，删除掉不用的ROOM。

## 二、Minimum Solder Mask Sliver Constraint

​		这个问题主要描述的是两个焊盘之间，阻焊层的最小间距。如果阻焊层的宽度过小，PCB在生产的时候可能导致阻焊层制造失败。如下图所示：

​        [Minimum Solder Mask Sliver Constraint Violation]	GeekIMU.PcbDoc	Advanced PCB	Minimum Solder Mask Sliver Constraint: (4.842mil < 10mil) 

<img src="E:\技术武器库\技术开发笔记\硬件开发笔记\Altium Designer\Image\Minimum Solder Mask Sliver.png" style="zoom:50%;" />

​		解决方案：在Design -> Rule -> Manufacturing中，找到Minimum Solder Mask Sliver。设置4mil即可。

## 三、Silk To Solder Mask Clearance

​		这个地方设置的是丝印到阻焊层的最小距离。

​		<img src="E:\技术武器库\技术开发笔记\硬件开发笔记\Altium Designer\Image\Silk To Solder Mask Clearance.png" style="zoom: 67%;" />

​		解决方案：在Design -> Rule -> Manufacturing中，找到Silk To Solder Mask Clearance，设置为0mil即可。

## 四、Hole Size Constrain

​		这个描述是最大孔径，默认是100mil，在生产制造的时候，如果挖的孔太大，可能机器的钻头无法钻出这么大的孔，如果生产能力满足，直接把规则设大即可。

​		解决方案：在Design -> Rule -> Manufacturing中，找到Hole，设置为合适值即可。

## 五、Silk To Silk Clearance Constraint

​		描述的是丝印之间的最小间距，这个问题不大，大不了就是丝印混在一起了。有时候真不好处理，可以设置为0mil。