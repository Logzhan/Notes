​		

# ESP内存和存储模型

ESP32-WROOM 规格说明书写到：

• 448 KB 的 ROM，用于程序启动和内核功能调用 

• 用于数据和指令存储的 520 KB 片上 SRAM • RTC 快速存储器，为 8 KB 的 SRAM，可以在 Deep-sleep 模式下 RTC 启动时用于数据存储以及被主 CPU 访问 

• RTC 慢速存储器，为 8 KB 的 SRAM，可以在 Deep-sleep 模式下被协处理器访问

• 1 Kbit 的 eFuse，其中 256 bit 为系统专用（MAC 地址和芯片设置）; 其余 768 bit 保留给用户程序, 这些 程序包括 flash 加密和芯片 ID

**1.1、ESP32的内存结构**

- IRAM：internal ram 内部RAM，指的是集成到SoC内部的RAM
- DRAM：dynamic ram 动态RAM，特点就是容量大、价格低，缺点就是上电后不能直接使用，需要软件初始化后才可以使用。

```C
I (434) heap_init: Initializing. RAM available for dynamic allocation:
I (441) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (447) heap_init: At 3FFBC0E0 len 00023F20 (143 KiB): DRAM
I (454) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (460) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (466) heap_init: At 4008E7C4 len 0001183C (70 KiB): IRAM
```

​		从以上的输出结果来看，ESP32的DRAM149KB，IRAM一共195KB，合并一共344KB。

**1.2 字节Bytes和KB**

​		观察ESP32生成的程序信息：DRAM可用128KB，IRAM可用70KB。

```
Total sizes:
 DRAM .data size:   11532 bytes
 DRAM .bss  size:   37864 bytes
Used static DRAM:   49396 bytes ( 131340 available, 27.3% used)
Used static IRAM:   59330 bytes (  71742 available, 45.3% used)
      Flash code:  349355 bytes
    Flash rodata:  296268 bytes
Total image size:~ 716485 bytes (.bin may be padded larger)
```

​		**Flash Code：即代码域，它通常是指编译器生成的机器指令，这些内容会被存储到ROM区。** 大约有340KB

​		**RO-data：Read Only data，即只读数据域，它指程序中用到的只读数据，这些数据被存储在ROM区，因而程序不能被修改的内容。** 大约290KB。

​		