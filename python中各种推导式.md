# python的各种推导式（列表推导式、字典推导式、集合推导式）

推导式（又称解析式），是Python的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。共有三种推导，在Python2和3中都有支持：
列表(list)推导式
字典(dict)推导式
集合(set)推导式

## 一、列表推导式

### 1、使用[]生成list

基本格式

variable = [out_exp_res for out_exp in input_list if out_exp == 2]
  out_exp_res:　　列表生成元素表达式，可以是**有返回值的函数**。
  for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
  if out_exp == 2：　　根据条件过滤哪些值可以。

**例一：**

```python
test = [i for i in range(10) if i %2 ==0]
print(test)
# 输出结果为[0, 2, 4, 6, 8]
```

**例二：**

```python
def sub(x):
    return x+100
test = [sub(i) for i in range(30) if i%3 is 0]
print(test)
# 输出结果为:[100, 103, 106, 109, 112, 115, 118, 121, 124, 127]
```

### 2、使用()生成generator

将列表推导式的[]改成()即可得到生成器。

```Python
test = (i for i in range(30) if i %3==0)
print(test)
# 输出结果为:<generator object <genexpr> at 0x01E69B70>
```



# 二、字典推导式

字典推导和列表推导的使用方法是类似的，中括号该改成大括号。举例说明：

例子一：大小写key合并

```Python
test = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
res = {
    k.lower(): test.get(k.lower(), 0) + test.get(k.upper(), 0)
    for k in test.keys()  if k.lower() in ['a','b']
        }
print (res)
# 输出结果为:{'a': 17, 'b': 34}

```


例子二：快速更换字典的key和value

```Python
test = {'a': 10, 'b': 34}
res = {v: k for k, v in test.items()}
print (res)
# 输出结果为:{10: 'a', 34: 'b'}
```



# 三、集合推导式

它们跟列表推导式也是类似的。 唯一的区别在于它使用大括号{}。

例：

```Python
test = {i**2 for i in [1,2,3,4,1]}
print(test)
#输出结果为:{16, 1, 4, 9}
```

