# **Git使用教程**

## 一、Git的公钥和私钥

github支持https和ssh方式访问代码库，https是无状态传输。git传输使用rsa算法，rsa生产一对数字，一个数字用来加密，另一个数字用来解密。git中这两个数字分别是公钥public key和私钥private key。通常，公钥给服务器，本地访问远端仓库下载代码时，服务器通过公钥加密代码然后发出去，本地电脑接收时，用本地存储的私钥解密它。如果匹配，就正常下载；如果不匹配，则下载失败。


## 二、生成密钥的步骤

1、在电脑桌面，鼠标右键，选择"Git Bash Here"，打开Git命令窗口；
2、在Git命令窗口中配置用户，输入如下命令：

```shell
# 这里的your_name需要替换为自己的id
git config --global user.name "your_name"
```

3、继续在Git窗口中配置邮箱，输入如下命令：

```shell
git config --global user.email "xxx@xx.com"
```

4、此时会在C:\Users\zhouxy目录下生成.gitconfig配置文件(此文件不能删除)；
5、查看.gitconfig配置文件里的内容；

6、继续在Git命令窗口中输入如下命令，即可生成SSH公钥和私钥

```shell
ssh-keygen -t rsa -C "xxx@xx.com"
```

![image-20220827162221537](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220827162221537.png)

7、进入C:\Users\Administrator.ssh目录下，查看生成的SSH密钥

# Git基本操作

qit切换分支

```
git checkout branchName
```

## Git创建分支并提交代码

```
# 创建新的本地分支, 新本地分支的代码是从原有分支拷贝
git checkout -b newB
# 将newB提交到远程仓库
git push -u origin newB
```

