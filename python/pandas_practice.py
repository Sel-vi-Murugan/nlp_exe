import numpy as np
data=np.array([7,54,6,78,99,])
print(data)

a=np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
new_a=a.reshape(3,4)
print(new_a)

fla_a=a.flatten()
print(fla_a)

zero_mat=np.zeros((4,5))
print(zero_mat)

cons_mat=np.full((3,3),5)
print(cons_mat)

inden_mat=np.eye(5)
print(inden_mat)

print(a[ :1])
print(a[2: ])


