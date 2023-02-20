app : 程序的主页面(MainActivity)，程序的启动页面(SplashActivity)

AppConfig模块 ：负责App的功能设置

**播放器显示控制器逻辑：**

DanDanVideoPlayer -> onKeyDown检测KeyEvent事件类型 -> {1、音量加 2、音量减 3、其他 ： 触发控制View}

DanDanVideoPlayer -> 触摸检测 检测TouchEvent事件类型 -> {左上下滑动：亮度  右上下滑动：音量  横向滑动：视频进度}

自动更新功能：BaseApplication(应用启动时的单例) => EMASHelper(阿里巴巴EMAS应用研发平台) => 发起弹窗和下载

**SMB文件浏览逻辑：**



