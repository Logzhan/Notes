```kotlin
Unit : 相当于JAVA的void
```

kotlin中when的用法

```kotlin
fun foo(value: Int): String {
    return when (value) {
        0 -> {
            "Zero"
        }
        1 -> {
            "One"
        }
        2 -> {
            "Two"
        }
        else -> {
            "Other"
        }
    }
}

```

