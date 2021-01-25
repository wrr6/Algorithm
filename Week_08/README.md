# 学习笔记

## 1.位运算

- 左移  <<
- 右移  >>
- 与     &
- 或      |
- 非       ~
- 异或   ^



常用的方法：

- 获取x第n位的值:(x >> n)  &  1
- n & (n - 1)    清零最低位的1 
- 获取x的第n位的幂值: x & (1 << n)
- 判断奇数和偶数 x % 2 可以换成 x & 1
- x / 2 可以换成x >> 1



利用一个数字也能代替之前的数组，用位来表示状态



注意事项：

需要注意数据类型是否会溢出，是否为有符号数和无符号数，以及移位





## 2.布隆过滤器

布隆过滤器可以检索一个元素是否在集合当中，是一个很长的二进制向量和一系列随机映射函数，优点是空间效率和查询时间都远超一般的算法，缺点为删除困难和有一定的错误识别率。



python实现

```python
from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return "Nope"
        return "Probably"
    
bf = BloomFilter(50000, 7)
bf.add("dantezhao")
print(bf.lookup("dantezhao"))
print(bf.lookup("yyj"))
```





## 3.LRU 

两个要素：大小、替换策略

HashTable + Double LinkedList

O(1) 查询和O(1) 更新、修改



Python实现

```python
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        #key as the newest one
        self.dic[key] = v
        return v
    
    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                #self.dic is full
                self.dic.popitem(last = False)
            self.dic[key] = value
```



## 4.排序算法



- 比较类算法
  - 交换排序
    - 冒泡排序
    - 快速排序
  - 插入排序
    - 简单插入排序
    - 希尔排序
  - 选择排序
    - 简单选择排序
    - 堆排序
  - 归并排序
    - 二路归并排序
    - 多路归并排序
- 非比较排序
  - 计数排序
  - 桶排序
  - 基数排序