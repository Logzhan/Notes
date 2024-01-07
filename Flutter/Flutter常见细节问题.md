# Flutter常见问题

基本上flutter安装官方教程进行环境安装即可，但是有些细节会导致安装出现问题。常见问题如下：

## 一、flutter doctor长时间等待问题

​		产生的原因：1) Powershell没有采用管理员权限运行 2) 没有采用国内镜像源

​		1、先配置国内镜像仓库源：

```shell
# 参考网址：https://flutter.cn/community/china
# 下面命令不一定生效，可以采用手动的方式在环境变量中增加变量名和变量值
# 配置默认国内镜像源
$env:PUB_HOSTED_URL="https://pub.flutter-io.cn";
$env:FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
# 配置清华源
$env:PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub";
$env:FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"
```

​		2、采用管理员身份运行Powershell或者cmd