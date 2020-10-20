#Python中的二维数组实例(list与numpy.array)
>>import numpy as np
>>a=[[1,2,3],[4,5,6],[7,8,9]]
>>a
[[1,2,3],[4,5,6],[7,8,9]]
>>type(a)
<type 'list'>
>>b=np.array(a)"""List to array conversion"""
>>type(b)
<type 'numpy.array'>
>>b
array=([[1,2,3],
    [4,5,6],
    [7,8,9]])
    
>>a[1][1]
5
>>a[1]
[4,5,6]
>>a[1][:]
[4,5,6]
>>a[1,1]"""相当于a[1,1]被认为是a[(1,1)],不支持元组索引"""
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not tuple
>>a[:,1]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not tuple

>>b[1][1]
5
>>b[1]
array([4,5,6])
>>b[1][:]
array([4,5,6])
>>b[1,1]
5
>>b[:,1]
array([2,5,8])
