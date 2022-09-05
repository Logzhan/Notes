# Pandas-Dataframe使用笔记

## 一、Dataframe的读取和保存

**1.1 Dataframe导出csv**

```python
# Dataframe转CSV
xlsx_file.to_csv('F:/XXX/XXX.csv', encoding="utf-8-sig",header=True)
```

**1.2 Pandas读取xlsx**

```python
# xlsx_file_name 如：'F:/XXX/XXX.xlsx'
# 一般xlsx默认的sheet_name是Sheet1
xlsx_file = pd.read_excel(xlsx_file_name, sheet_name='Sheet1')
```

**1.3 Dataframe的创建**

dataframe可以通过读取csv或者xlsx等方式创建，同时也可以通过数组创建

```python
import pandas as pd
# 创建数组
data_list = [[6,10,3],[1,5,4],[1,2,4],[1,15,24],[1,0,2],[3,7,9],[2,8,5]]
# 通过数组创建dataframe, columns并不是必须的, 如果不提供的话默认用0,1,...,n表示
df = pd.DataFrame(data_list,columns=['A','B','C'])
# 指定dataframe的行索引, 这也不是必须的, 如果不提供的话默认用0,1,...,n表示
df.index = ['G','H','I','J','K','L','M']
# 打印结果
print(df)
```

## 二、Dataframe的操作

**2.1 获取Dataframe和行数和列数**

```python
import pandas as pd
import numpy as np
# 创建dataframe
df = pd.DataFrame(np.arange(24).reshape(6,4), columns=['A', 'B', 'C', 'D'])
row_nums = df.shape[0]
col_nums = df.columns.size
print(row_nums)
print(col_nums)

# 获取特定行data.iloc[x,y]
```

**2.2 Dataframe删除行、列**

```python
import pandas as pd
import numpy as np
# 创建dataframe
df = pd.DataFrame(np.arange(24).reshape(6,4), columns=['A', 'B', 'C', 'D'])
print(df)
# 删除单行
df1 = df.drop(axis=0, index = 1, inplace=False)
print(df1)
# 删除多行
df2 = df.drop(axis=0, index = [1,2,4], inplace=False)
print(df2)
# 删除列
df3 = df.drop(axis=1, columns = ['A','D'], inplace=False)
print(df3)
```

注意删除多行的时候要确保index存在，一种非常隐蔽的错误是：

```python
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])
# ignore_index=True 保留原索引
new_df = pd.concat([df1,df2], ignore_index=False)
# 打印可以看到拼接之后索引只有0,1,2
print(new_df)
# 当我们调用删除行函数的时候会报错,因为没有index=3,虽然这个dataframe是6x4大小的
# 这是一个非常隐蔽的错误
df3 = new_df.drop(axis=0, index = 3, inplace=False)
```

**2.3 Dataframe的排序**

dataframe的排序有通过行列的名称进行排序，也有同行的数值或者列的数值进行排序。对于数值排序，采用sort_values函数。

```python
import pandas as pd
# 创建dataframe
data_list = [[6,10,3],[1,5,4],[1,2,4],[1,15,24],[1,0,36],[3,7,9],[2,8,5]]
df = pd.DataFrame(data_list,columns=['A','B','C'])
df.index = ['G','H','I','J','K','L','M']
# 对列A进行降序排列
# ascending表示是否升序排列, inplace表示在自身进行排序
df.sort_values(by='A',axis=0,ascending=False,inplace=True)
print(df)

df = pd.DataFrame(data_list,columns=['A','B','C'])
df.index = ['G','H','I','J','K','L','M']
# 对A列和B列进行升序排列,按照A、B的优先级进行排序
df_data_order = df.sort_values(by=['A','B'],ascending=[True,True])
print(df_data_order)
```

很多时候，对于一些默认行号的dataframe，排序之后会把把行号打乱。这个时候可以通过reset_index函数重置索引。

```python
import pandas as pd
data = [['a','3'],['b','1'],['c','2']]
df = pd.DataFrame(data)
df = df.sort_values(by = 1,axis = 0,ascending = False)
# 排序后的行号是乱的
print(df)
# 重置索引后行号按照0,1,2,...顺序
df = df.reset_index(drop=True)
print(df)
```

**2.4 Dataframe的拼接**

Dataframe的拼接有几个函数：merge、concat等函数

```python
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])
# 拼接df1和df2,默认的拼接方向axis=0垂直方向拼接
# ignore_index=True 忽略原索引
new_df = pd.concat([df1,df2], ignore_index=True)
print(new_df)
# ignore_index=True 保留原索引
new_df = pd.concat([df1,df2], ignore_index=False)
print(new_df)
```

**2.5 Dataframe数据筛选**

```python
import pandas as pd
# 创建数组
data_list = [['拖动',10,3],[1,5,4],['拖动',2,4],[1,15,24],['滑动',0,2],[3,7,9],[2,8,5]]
# 通过数组创建dataframe, columns并不是必须的, 如果不提供的话默认用0,1,...,n表示
df = pd.DataFrame(data_list,columns=['A','B','C'])
print(df)
# 去掉A列中包含拖动的数值
df1 = df[~(df['A']=='拖动')]
# 重建索引序号
df1 = df1.reset_index(drop=True)
print(df)
# 更加复杂的运算操作
# df=df[~((df['B']>7)|(df['D']==0))]

df1 = df[(df['A'].isin(['拖动','滑动']) == True)]
df1 = df1.reset_index(drop=True)
print(df1)

# 列筛选A列和B列
df = pd.DataFrame(data_list,columns=['A','B','C'])
df = df[['A','B']]
print(df)
```

对dataframe的字符串筛选也可以通过Dataframe的contain函数，这种方式可以允许子串的搜索，同时contain函数也支持正则表达式。

```python
import pandas as pd
# 创建数组
data_list = [['拖动',10,3],[1,5,4],['拖动',2,4],[1,15,24],['滑动',0,2],[3,7,9],[2,8,5]]
# 通过数组创建dataframe, columns并不是必须的, 如果不提供的话默认用0,1,...,n表示
df = pd.DataFrame(data_list,columns=['A','B','C'])
print(df)
# 去掉A列中包含动的数值
df=df[(df['A'].str.contains('动') == True)]
# 重建索引序号
df = df.reset_index(drop=True)
print(df)

# contains函数支持正则表达式
df = pd.DataFrame(data_list,columns=['A','B','C'])
parttern = r'.*?'
df=df[(df['A'].str.contains(parttern) == True)]
print(df)
```

**2.6 Dataframe NaN处理**

axis: default 0指行,1为列

how: {‘any’, ‘all’}, default **‘any’指带缺失值的所有行**;**'all’指清除全是缺失值的**

thresh: int,保留含有int个非空值的行

subset: 对特定的列进行缺失值删除处理

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [np.nan, 1, 2], 'B': [10, np.nan, 10], 'C': [10, 25, 15]})
print(df)
# any表示某一行或者某一列有NaN即被抛弃, all表示清除全部都是NaN
df = df.dropna(axis=0, how='any')
print(df)
# 删除pkg中存在NaN的列， subset=['pkg','xxx','xxxxx']
# df2 = df.dropna(axis='index', how='all', subset=['pkg'])
```

