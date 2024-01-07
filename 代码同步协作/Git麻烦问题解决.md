1、Git 某次Commit 有大文件，导致Github无法提交上去

​		解决方案是把这个大文件从历史的所有提交剔除，如下面的命令所示：

```shell
# 使用双引号将文件路径括起来
# 当你的路径存在空格的时候容易导致命令行识别错，可以把你要删除的路径的文件加上""
git filter-branch --force --index-filter 'git rm --cached -r --ignore-unmatch "your path"' --prune-empty --tag-name-filter cat -- --all

```

