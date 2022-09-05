# LVGL常用函数笔记

## 一、屏幕操作相关

**1.1 获取屏幕的对象**

```C
lv_obj_t * lv_scr_act(void)    // 获取当前活动屏幕的指针
```

**1.2 在屏幕上创建对象**

```C
// 获取当前屏幕对象并创建对象
lv_obj_t* root_obj = lv_obj_create(lv_scr_act()); 
// 设置对象背景颜色
lv_obj_set_style_bg_color(root, lv_color_black(), 0);
// 设置对象背景透明度 Opacity：透明度
lv_obj_set_style_bg_opa(root, LV_OPA_COVER, 0);
```

1.3 