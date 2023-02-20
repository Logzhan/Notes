## Android引入其他工程

​       在安卓开发中，我们为了开发方便，所以需要引入其他的已经封装好的模块。如下所示：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230211150717050.png" alt="image-20230211150717050" style="zoom: 50%;" />

​        在app工程中，需要用到libsmb库提供的smb管理和访问的功能。需要在两个地方进行配置。首先是app工程目录下的settings.gradle中配置。

```shell
# settings.gradle的配置，是编译器包含libsmb
rootProject.name = "My Application"
include ':app'
include ':libsmb'
# 在build.gradle中添加依赖选项
implementation fileTree(include: ['*.jar'], dir: 'libs')
...
implementation project(':libsmb')
```

