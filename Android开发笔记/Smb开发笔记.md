## Android Smb开发笔记

### 一、SMB的基本操作

Android的SMB开发会用到jcifs这个库。这个库提供了SMB的底层操作功能。

根据URI打开一个SMB。

```java
// 指定SMB的路径
String uri = "smb://administrator:351002@192.168.31.52/H/琅琊榜 全54集 1080P/";
// 网络的相关操作必须通过新线程的方式启动，否则会触发Android的错误
new Thread(new Runnable() {
    @Override
    public void run() {
        try {
            // 根据uri打开SmbFile
            SmbFile smbFile = new SmbFile(uri);
            String fileName = smbFile.getName();
            Log.d("Test", fileName);
            // 控制台打印SMB路径下的文件
            try{
                String[] FileList = smbFile.list();
                for (String s : FileList) {
                    Log.d("Test", s);
                }
            }catch (SmbException e){
                e.printStackTrace();
            }
        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        }
    }
}).start();
```

### 二、SMB转HTTP

当我们把SMB的Uri提供给播放器后，播放器会请求GET视频。对于一个完整的视频，Http的请求如下所示。

如果我们在解析请求头的时候没有收到请求的范围信息，那么默认就是返回全部的内容。

```shell
GET  /smb/192.168.31.52/I/XXX.mp4 HTTP/1.1
User-Agent: ExoPlayerTime/1.0 (Linux;Android 12) ExoPlayerLib/2.7.1
Accept-Encoding:identity
Host: 127.0.0.1:2222
Connection: Keep-Alive
```

当我们拖动进度条的时候，此时视频不是从0开始播放，所以视频播放器会请求包含Range的信息：

```Shell
GET  /smb/192.168.31.52/I/XXX.mp4 HTTP/1.1
User-Agent: ExoPlayerTime/1.0 (Linux;Android 12) ExoPlayerLib/2.7.1
Range: bytes=1207598076-
Accept-Encoding:identity
Host: 127.0.0.1:2222
Connection: Keep-Alive
```

上述情况下，如果我们收到包含Range信息的请求时，返回的时候就需要额外指定一些信息。

```Java
// 获取文件长度bytes
long contentLen = file.length();
// 从文件获得输入流
InputStream contentIn = file.getInputStream();
// 检查输入数据流是否正常
if (contentLen <= 0 || contentIn == null) {
    httpReq.returnBadRequest();
    return;
}
// 创建Http返回请求
HTTPResponse httpRes = new HTTPResponse();
// 指定视频数据格式
httpRes.setContentType("video/mpeg4");

if(startFrom == 0 && endAt == 0){
    // 请求没有范围信息则返回全部内容，状态OK(200)表示全部内容
    httpRes.setStatusCode(HTTPStatus.OK);
}else if(startFrom > 0){
    // 如果是包含RangeCotent,则需要返回PARTIAL_CONTENT(206)
    httpRes.setStatusCode(HTTPStatus.PARTIAL_CONTENT);
    httpRes.setContentRange(startFrom,endAt, contentLen);
}
// 设置内容总长度
httpRes.setContentLength(contentLen);
// 指定内容数据流
httpRes.setContentInputStream(contentIn);
// HttpReq提交数据
httpReq.post(httpRes);
contentIn.close();
```

