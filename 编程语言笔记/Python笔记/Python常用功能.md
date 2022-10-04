# Python 常用功能

## 一、python高频常用

**1.1 Python简单main框架**

```python
import os
def func():
    print('func')
if __name__ =="__main__":
    # 遍历文件夹所有文件
    func()
```

**1.2 文件夹遍历**

```python
import os

def get_filelist(path):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            # 完整路径文件名列表
            Filelist.append(os.path.join(home, filename))
            # 文件名列表，只包含文件名
            #Filelist.append(filename)
    return Filelist

# 获取文件夹文件路径
Filelist = get_filelist('F:/data_all_apps/')
# 打印文件完整路径
for file in  Filelist :
    print(file)
```

**1.3 保留两位小数**

```python
# 方法一：格式化字符串
a = 12.345
b = 12.122276
print("%.2f %.2f" % (a,b))

# 方法二：round函数
a = 12.44476
print(round(a,2))
```

**1.4 python格式化字符串**

```python
str = "hello"
print("this is a string: %s" % str)
print("this is a string: %s, %s" % (str, str)) 
idx = 2.66788
print("this %.2f is a string: %s, %s" % (idx, str, str)) 
```

其他丰富样例：

```python
first = "持续学习"
second = "持续开发"
slogan = first + second
print(slogan)
banner = "*" * 16
print(banner)
slice = slogan[2:4]
print(slice)
print(""""学习" in slogan ： %s""" % ("学习" in slogan))
print(""""不学习" not in slogan ： %s""" % ("不学习" not in slogan))
print(r"""打印\n换行被当做普通字符输出了！""")
# 以上我们都可以看到%，很多次代码都有说到这个，但是并没有过多解释
print("%s" % slogan)  # 最常用了%s 格式化字符串
# print("%c"%'ccc')#TypeError: %c requires int or char
print("%c" % 'c')  # %c 通常用来强制检测待输出的字符串必须长度为1
print("%c" % '雷')  # %c 通常用来强制检测待输出的字符串必须长度为1
number = 102.40101
print("%%i 符号整数 %i" % number)
print("%%i 符号整数：%i" % -number)
print("%%d 符号整数 %d" % number)
print("%%d 符号整数 %d" % -number)
print("%%u 无符号整数：%u" % number)
print("%%u 无符号整数：%u" % -number)
#print("八进制 %o" % number)
print("%%o 八进制 %o" % 102)
print("%%x16进制 %x" % 102)
#print("16进制 %X" % 102)
print("%%e 自然常数 e进制： %e" % number)
#print("%E" % number)
print("%%f 浮点数 %f" % number)
#保证显示6微有效数字的前提下，灵活的选择小数方式，或者科学计数法
print("%%g 灵活的有效显示：%g" % number) 
#print("%G" % number)
#保证显示6微有效数字的前提下，灵活的选择小数方式，或者科学计数法
print("%%g 灵活的有效显示：%g" % (number*10001)) 
#下面两种写法需要注意执行顺序
#print("%g" % number*10001) #注意这种写法
#print("%g" % number**10) #注意这种写法
```

1.5 系统暂停

```python
os.system('pause')
```

