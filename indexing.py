import numpy as np
arr1=np.array([1,2,56,7])
print(arr1[0])
print(arr1[2])
print(arr1[2]*arr1[1])
print(arr1[2]-arr1[3])
arr2=np.array([[4,7,98],[3,2,5]])
print(arr2[1,2])
arr3=np.array([[[[1,5],[5,7]],[[78,45],[6.3]]]])
print(arr3[0,1,0])
print(arr2[0,-1])
print(arr1.ndim)
print(arr2.ndim,arr3.ndim)

