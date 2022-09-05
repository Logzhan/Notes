# **ESP32 DevKit v1 资料**

链接：https://github.com/Nicholas3388/LuaNode

## 一、GPIO的基本操作

可以看到LED灯的IO口是D2，那么对应的闪烁LED灯的例程如下所示：

```c
#define BLINK_GPIO 2

void app_main(void)
{
    gpio_reset_pin(BLINK_GPIO);
    /* Set the GPIO as a push/pull output */
    gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);
    while(1) {
        /* Blink off (output low) */
        printf("Turning off the LED\n");
        gpio_set_level(BLINK_GPIO, 0);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        /* Blink on (output high) */
        printf("Turning on the LED\n");
        gpio_set_level(BLINK_GPIO, 1);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
```

开发板上的D表示GPIO的意思，D2就表示GPIO2，其他IO口也是类似的。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220828213702936.png" alt="image-20220828213702936" style="zoom:50%;" />