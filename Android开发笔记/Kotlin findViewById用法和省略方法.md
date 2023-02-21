# Kotlin 操作Layout控件

在Android Acitivity开发中，传统的java开发中findviewbyid。在kotlin中，有两种写法都可以操作layout控件。

## 一、传统写法（不推荐）

​		不推荐的原因主要是麻烦，满屏幕都是findViewById，非常的繁琐。

```kotlin
package com.geek.motion

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        var textView = findViewById<TextView>(R.id.textView)
        textView.setText("Hello Kotlin")
    }
}
```

## 二、省略写法(推荐)

​		下面采用的是省略写法，注意需要引入import kotlinx.android.synthetic.main.activity_main.*

```kotlin
package com.geek.motion

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        textView.text = "Hello kotlin"
    }
}
```

​		如果在引用import kotlinx.android.synthetic.main.activity_main.*时报错，注意在build.gradle中，添加：**'kotlin-android-extensions'**

```shell
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
    // 添加
    id 'kotlin-android-extensions'
}
android {
    compileSdk 32
    ...
```

