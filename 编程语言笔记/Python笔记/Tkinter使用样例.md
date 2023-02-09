## Tkinter(Python便捷GUI库)笔记

```python
import tkinter as tk  # 在代码里面导入库，起一个别名，以后代码里面就用这个别名
from tkinter import messagebox
import os
import shutil
import threading

def thread_it(fc):
    t = threading.Thread(target=fc)
    t.setDaemon(True)
    t.start()
    

def ShowFinish(e):
    '''创建弹窗'''
    messagebox.showinfo("窗口名称", "点击成功")

def copy_file(paths,patht):
    same_file_num = 0
    copy_file_num = 0
    for filename in os.listdir(paths):
        filename_s = paths + os.sep + filename
        filename_t = patht + os.sep + filename

        #avi2mp4(filename_s)

        # 如果是文件夹，那么递归处理
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)
            copy_file(filename_s,filename_t)
        else:
            if os.path.exists(filename_t):
                #print("[*] "+ filename_t + " already exists! ") 
                same_file_num = same_file_num + 1
            # 如果目标属于文件，且目标文件夹不存在，那么拷贝文件
            else:
                print("Copy Source :" + filename_s)
                print("To   Target :" + filename_t)
                copy_file_num = copy_file_num + 1
                try:
                    shutil.copyfile(filename_s, filename_t)
                except IOError as e:
                    print("Unable to copy file. %s" % e)
                    exit(1)
                except:
                    print("Unexpected error: exit")
                    exit(1)

    if(copy_file_num > 0):
        print(paths + ": sync file count = " + str(copy_file_num))

#--------------------------------------------------------------------------------
# Function         :  search_diff_file_and_del
# Description      ：  以paths为参考,删除patht与paths不同的文件                    
# Date             :  2023-02-09 loghzan
#--------------------------------------------------------------------------------
def search_diff_file(patht,paths,diff_list):
    same_file_num = 0
    copy_file_num = 0
    for filename in os.listdir(patht):
        filename_t = patht + os.sep + filename
        filename_s = paths + os.sep + filename
        # 如果是文件夹，那么递归处理
        if os.path.isdir(filename_t):
            if os.path.exists(filename_s):
                search_diff_file(filename_t,filename_s,diff_list)
            else:
                print("rm target path" + filename_t)
                # 递归删除文件夹
                #shutil.rmtree(filename_t)
        else:
            if os.path.exists(filename_s):
                #print("[*] "+ filename_t + " already exists! ") 
                same_file_num = same_file_num + 1
            # 如果目标属于文件，且源文件夹不存在，加入列表，最后删除
            else:
                #print("[*]  Source :" + filename_s)
                diff_list.append(filename_t)
                #print("[*]  Target :" + filename_t)
                copy_file_num = copy_file_num + 1

# 利用ffmpeg 将avi文件转换为mp4
def avi2mp4(path):
    if (path.find(".avi") == -1) and (path.find(".wmv") == -1):
        return
    # 输入视频路径
    video_path = path
    # 修改avi后缀为mp4
    out_video_path = video_path[0:len(video_path)-4] + ".mp4"

    cmd_str = ""
    if(path.find("avi") != -1):
        # 生成命令path
        cmd_str = "ffmpeg" + " -i " + "\"" + video_path + "\"" + " -c copy -map 0 "
        cmd_str = cmd_str +  "\"" + out_video_path + "\""
    if(path.find("wmv") != -1):
        cmd_str = "ffmpeg" + " -i " + "\"" + video_path + "\"" + "  "
        cmd_str = cmd_str +  "\"" + out_video_path + "\""  
        print(cmd_str)
        os.system(cmd_str)
        #os.remove(path)
        print("finsh convert avi to mp4") 
        return

    print(cmd_str)
    os.system(cmd_str)
    os.remove(path)
    print("finsh convert avi to mp4")


def sync_file(local,cloud):
    copy_file(local, cloud)
    # 找出目标文件夹存在，但是源文件夹不存在的文件
    diff_list = []
    search_diff_file(cloud,local,diff_list)
    # 删除源文件夹不存在的文件            
    for i in range(0, len(diff_list)):
        print("delete target : " + diff_list[i])
        os.remove(str(diff_list[i]))
    print("sync file finish")

def local2cloud(local,cloud):
    thread_it(lambda:sync_file(local, cloud))

def local2back(local, back):
    thread_it(lambda:sync_file(local, back))

# 从src端拷贝不同的文件到目标端
def copy_diff(src, dst):
    thread_it(lambda:copy_file(src, dst))

def cloud2local(cloud,local):
    copy_diff(cloud, local)
    print("cloud sycn local finish")

back  = "D:\\UBUNTU\\ubuntu\我的资料\我的收藏\\"
local = "F:\\我的收藏\\"
cloud = "I:\\115\\我的收藏\\"

# 这个库里面有Tk()这个方法，这个方法的作用就是创建一个窗口
root = tk.Tk()        
# 设置标题
root.title('磁盘同步工具GUI v1.0.0')
# (宽度x高度)+(x轴+y轴)
root.geometry("320x150+630+80") 


label1 = tk.Label(text="云端路径:")
label1.place(x = 10, y = 10)
label2 = tk.Label(text="本地路径:")
label2.place(x = 10, y = 30)
label3 = tk.Label(text="备份路径:")
label3.place(x = 10, y = 50)

label1["text"] = "云端路径: " + cloud
label2["text"] = "本地路径: " + local
label3["text"] = "备份路径: " + back


btn1 = tk.Button(text='本地同步云端', command = lambda:local2cloud(local, cloud))
btn1.place(x = 10, y = 100)

btn2 = tk.Button(text='云端同步本地', command = lambda:cloud2local(cloud, local))
btn2.place(x = 110, y = 100)

btn3 = tk.Button(text='本地同步备份', command = lambda:local2back(local, back))
btn3.place(x = 210, y = 100)

# 启动线程循环看到窗口
root.mainloop()  
```

