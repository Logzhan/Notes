# Kotlin测量经过的时间

## 一、使用 `System.nanoTime()` 功能

在 Kotlin 中测量程序运行时间的推荐方法是 `System.nanoTime()`，它以纳秒精度返回 JVM 时间源的当前值。

```kotlin
fun main() {
    val begin = System.nanoTime()
    /* 代码开始 */
    // 休眠 2 秒
    Thread.sleep(2000)
    /* 代码结束 */
    val end = System.nanoTime()
    println("Elapsed time in nanoseconds: ${end-begin}")
}
```

## 二、使用 `System.currentTimeMillis()` 功能

您还可以使用 `System.currentTimeMillis()`，但结果可能不是那么准确。

```kotlin

fun main() {
    val begin = System.currentTimeMillis()
    /* 代码开始 */
    // 休眠 2 秒
    Thread.sleep(2000)
    /* 代码结束 */
    val end = System.currentTimeMillis()
    println("Elapsed time in milliseconds: ${end-begin}")
}
```

这是使用的替代解决方案 `Instant.now()` 内部使用 `System.currentTimeMillis()`.

```kotlin
import java.time.Instant
 
fun main() {
    val begin = Instant.now().toEpochMilli()
    /* 代码开始 */
    // 休眠 2 秒
    Thread.sleep(2000)
    /* 代码结束 */
    val end = Instant.now().toEpochMilli()
    println("Elapsed time in milliseconds: ${end-begin}")
}
```

## 三.使用 `Date.getTime()` 功能

```kotlin
import java.util.Date
 
fun main() {
    val begin = Date().time
    /* 代码开始 */
    // 休眠 2 秒
    Thread.sleep(2000)
    /* 代码结束 */
    val end = Date().time
    println("Elapsed time in milliseconds: ${end-begin}")
```

