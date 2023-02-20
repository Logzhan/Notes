```java
// 给定视频的URL
final String url = videoUrl;
// 调用Android的MediaMetadataRetriever获取视频封面
final MediaMetadataRetriever mmr = new MediaMetadataRetriever();
new Thread(() -> {
    Map<String, String> headers = new HashMap<>() ;
    // 指定header和url
    mmr.setDataSource(url, headers);
    // 设置截取视频第10秒钟内容
    Long sec = 10L;
    // sec转us单位
    Long msec = sec * 1000L;
    Long us = msec * 1000L;

    final Bitmap image = mmr.getFrameAtTime(us, MediaMetadataRetriever.OPTION_CLOSEST_SYNC);
    // 更新imageview显示图片
    runOnUiThread(() -> {
        ImageView tv = findViewById(R.id.imageView);
        tv.setImageBitmap(image);
    });
    // 释放mmr，断开连接
    mmr.release();
}).start();
```

HTTP视频请求Range的计算方法
