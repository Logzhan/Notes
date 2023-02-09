## Android 播放器使用

### 一、调用第三方视频播放器

Android通过Intent调用第三方播放器，通过Url播放视频。

```java
// 启动第三方播放器
Intent intent = new Intent();
intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
intent.setAction(android.content.Intent.ACTION_VIEW);
intent.setDataAndType(Uri.parse(http), "video/*");
startActivity(intent);
```

### 二、Exo播放器的使用
