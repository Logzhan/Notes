# Numpy使用笔记

​		NumPy 全称为 Numerical Python，是 Python 的一个以矩阵为主的用于科学计算的基础软件包。NumPy 和 Pandas、Matpotlib 经常结合一起使用，所以被人们合称为数据分析三剑客。Numpy 中有功能强大的 ndarray 对象，能创建 N 维的数组，另外还提供很多通用函数，支持对数组的元素进行操作、支持对数组进行算法运算以及提供常用的统计函数。

​		相比 List 对象，NumPy 数组有以下优势：

1. 这是因为列表 list 的元素在系统内存中是分散存储的，而 NumPy 数组存储在一个均匀连续的内存块中。这样数组计算遍历所有元素，不像列表 list 还需要对内存地址进行查找，从而节省了计算资源。
2. Numpy数组能够运用向量化运算来处理整个数组，速度较快；而 Python 的列表则通常需要借助循环语句遍历列表，运行效率相对来说要差。
3. NumPy 中的矩阵计算可以采用多线程的方式，充分利用多核 CPU 计算资源，大大提升了计算效率。
4. Numpy 使用了优化过的 C API，运算速度较快。

## 一、数组创建和使用

**1.1、创建zeros数组**

```python
import numpy as np
# 创建1维数组
x1 = np.zeros(20)
# 打印一维数组
print(x1)
# 数组的赋值, 从0开始
for i in range(0,20):
    x1[i] = i
    print(str(x1[i]))
# 2维数组的创建
# 创建一个 3x4 的数组且所有值全为 0
x3 = np.zeros((3, 4), dtype=int)
print(x3)
# 创建一个 3x4 的数组且所有元素值全为 1
x4 = np.ones((3, 4), dtype=int)
print(x4)
# 创建一个 3x4 的数组，然后将所有元素的值填充为 2
x5 = np.full((3, 4), 2, dtype=int)
print(x5)
```

**1.2、创建随机数组**

```python
import numpy as np
# 创建2*2随机数组
lux_br_arr = np.random.random((2,2))
# 打印结果
print(lux_br_arr)
```

1.3 通过array_list创建数组

```python
 import numpy as np
 x_list = [1,2,3,4]
 x = np.array(x_list)
 print(x)
```

