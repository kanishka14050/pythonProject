#mutiply two dimensional array
import numpy as matrix

in_num1 = matrix.array([[4,9,6] , [5,8,7]])
in_num2 = matrix.array([[5,9,6],[3,2,7]])

print("1st Input  number : ", in_num1)
print("2nd Input  number : ", in_num2)

out_num = matrix.multiply(in_num1, in_num2)
print("output number : ", out_num)