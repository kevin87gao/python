'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
上面的构造器接受以下参数：
序号	参数及描述
1.	object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
2.	dtype 数组的所需数据类型，可选。
3.	copy 可选，默认为true，对象是否被复制。
4.	order C(按行)、F(按列)或A(任意，默认)。
5.	subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
6.	ndimin 指定返回数组的最小维数。
'''

import numpy as np


# 创建一个数组
a = np.array([1, 2, 3])
print(a)            # [1 2 3]
print(type(a))      # <class 'numpy.ndarray'>
'''
    数组属性，返回一个包含数组维度的元组。
    shape[0]表示返回数组第一维的长度
    若元组只有一个元素，则说明这个数组是一维数组：如元组(2,),表示一维数组，只含有2个元素
    若元组中有两个元素，则说明这个数组是二维数组：元组(2,3)，说明这是一个二维数组，其中第一个维度含有2个元素，第二个维度中每一个元素都含有3个元素.
    得出以下两个结论：
    1. 元组的元素的个数等于维度数
    2. 元组中每一个元素代表其中每一维度元素的个数(从左到右，依次为第一维度中元素的个数，第二维度中元素的个数...第N维度元素的个数)
'''
print(a.shape)      # (3,)
# 返回数组第一维的长度
print(a.shape[0])   # 3
# 返回数组的维数
print(a.ndim)       # 1
# 定义一个一维数组，内容为0到23
a = np.arange(24)
print(a.ndim)       # 1
'''
    改变数组的维度,有两种方式：
    1 a.shape = (2, 12)
    2 a = a.reshape(2, 12) 
'''
b = a.reshape(3, 4, 2)
print(b.ndim)       # 3
print(b.shape)      # (3, 4, 2) 元组有三个数，表示此数组是三维，第一维里面有3个元素，第二维里面有4个元素，第三维里面有2个元素
print(b)
'''
[[[ 0  1]
  [ 2  3]
  [ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]
  [12 13]
  [14 15]]

 [[16 17]
  [18 19]
  [20 21]
  [22 23]]]
'''
print("b.size = %d" % b.size)       # 24 数据元素的总个数
print("b.dtype: ", b.dtype)         # int32 ndarray对象的元素类型
print("b.itemsize: ", b.itemsize)   # 4 ndarray对象中每个元素的大小，已字节为单位
print("b.flags: ", b.flags)         # ndarrat对象的内存信息,输出内容为：
'''
    C_CONTIGUOUS : True             # 数据是在一个单一的C风格的连续段中
    F_CONTIGUOUS : False            # 数据是在一个单一的Fortran风格的连续段中
    OWNDATA : False                 # 数组拥有它所使用的内存或从另一个对象中借用它
    WRITEABLE : True                # 数据区域可以被写入，将该值设置为False，则数据为只读
    ALIGNED : True                  # 数据和所有元素都适当地对齐到硬件上
    WRITEBACKIFCOPY : False
    UPDATEIFCOPY : False            # 这个数组是其他数组的一个副本，当这个数组被释放时，原数组的内容将被更新
'''
#print("b.real: ", b.real)       # ndarray元素的实部
#print("b.image: ", b.image)     # ndarray元素的虚部
print(b[0][1][1])               # 3  直接以下标的形式访问数组元素。第一维数组里面的第0个元素下，二维数组里的第1个元素下，三维数组的第1个元素
print('*********************')


# 改变数组的维度
a = np.arange(6)
#a.shape = (2, 3)
a = a.reshape(2, 3)
print(a)
'''
[[0 1 2 ]
 [3 4 5]]
'''
print(a.shape)      # (2, 3)

# 最小维度
a = np.array([1, 2, 3, 4], ndmin=2)
print(a)            # [[1 2 3 4]]
print(a.shape)      # (1, 4)
print(a.ndim)       # 2

# dtype参数
a = np.array([1, 2, 3], dtype=complex)
print(a)            # [1.+0.j 2.+0.j 3.+0.j]
a = np.array([1, 2, 3], dtype=float)
print(a)            # [1. 2. 3.]
