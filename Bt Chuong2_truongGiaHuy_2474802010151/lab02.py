# Dẫn nhập – Một số hàm về xử lý vector với Python
def scale(a,v):
  return [a*vi for vi in v]
v=[3,5,7]
print(scale(10,v))

def sumvector(v, w):
  return [vi+wi for (vi, wi) in zip(v, w)]
v = [3,5,7]
w = [2,4,6]
print(sumvector(v, w))
def dotvector(v, w):
  return sum([vi*wi for (vi, wi) in zip(v, w)])
print(dotvector(v, w))

def lenvector(v):
  return dotvector(v,v)
lenvector(w)
# Phân loại tuyến tính
import numpy as np
scores=np.array([-1,1,2,-3,5,-4])
print (scores)
print(scores >=0)
print(scores <0)
# Convert scores to strings before using np.select
a=np.select([scores >=0, scores < 0],['so duong', 'so am'], default='khong xac dinh')
print(a)
scores  = np.array([-1, 1, 2, 0, -3, 5, 0, -4])
b=np.select([scores >0, scores ==0, scores < 0],['so duong', 'so 0', 'so am'],default='khong xac dinh')
print(b)
# Phân loại tuyến tính
import numpy as np
scores=np.array([-1,1,2,-3,5,-4])
print (scores)
print(scores >=0)
print(scores <0)
# Convert scores to strings before using np.select
a=np.select([scores >=0, scores < 0],['so duong', 'so am'], default='khong xac dinh')
print(a)
scores  = np.array([-1, 1, 2, 0, -3, 5, 0, -4])
b=np.select([scores >0, scores ==0, scores < 0],['so duong', 'so 0', 'so am'],default='khong xac dinh')
print(b)
#Thực hành xử lý ma trận
# bài 1
import numpy as np
from scipy import linalg, sparse
D = np.asmatrix([ [3,4], [5,6] ])
print (D)
# bài 2
C=np.asmatrix(np.random.random((5,7)))
print (C)
# bài 3
A=np.asmatrix(np.random.random((2,2)))
print (A)
# bài 4
b = np.array([(1+5j, 2j, 3j),(4, 5, 6)])
B = np.asmatrix(b)
# bài 5
print(b)
print(B)
print(A.T)
# bài 6
print(A.I)
# bài 7
print(linalg.inv(A) )
# bài 8
M = np.array([[-1,3,2],[0,2,1],[1,5,-2]])
M_lower = np.tril(M)
print(M_lower)
# bài 9
M = np.array([[-1,3,2],[0,2,1],[1,5,-2]])
M_upper = np.triu(M)
print(M_upper)
# bài 10
M = np.array([[-1,3,2],[0,2,1],[1,5,-2]])
v_diag = np.diag(M) #vector
print (v_diag)
M_diag = np.diag(v_diag)
print (M_diag)
#Các phép biến đổi sơ cấp trên ma trận
import numpy as np
A = np.reshape(np.arange(36.0), (6,6))
print (A)
I6 = np.identity(6)
print (I6)
print(A.size)
print(np.matrix.diagonal(A))
A = A + I6
print (A)
vecB = np.array([1., 2., 3., 4., 5., 6.])
C = A.dot(vecB)
print (C)
D = np.array([[1., 2., 3., 4., 5., 6.], [1., 0., 1., 0., 1., 0.]])
print (D)
E = A.dot(D)
print(E)
F = np.array([[1., 1.], [2., 0.], [3., 1.], [4., 0], [5., 1], [6., 0.]])
G = A.dot(F)
print (F)
print(G)
a1=np.linalg.inv(A)
print(a1)
a2=np.linalg.inv(np.linalg.inv(A))
print(a2)
#Tính toán dãy Fibonacci
import numpy as np
A = np.array( [ [1,1], [1,0] ] )
b = np.array([1, 0])
n = 10

for i in range(n):
  b = A.dot(b)
print(b)
#Đếm số lượng xe vào khu vực trung tâm
import sympy as sp
from sympy import Symbol
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
x4 = Symbol('x4')
from sympy import solve
pt1 = x4+610-450-x1
pt2 = x1+400-x2-640
pt3 = x2+600-x3
pt4 = x3-x4-520
nghiem = sp.solve((pt1, pt2, pt3, pt4))
print(nghiem )
import numpy as np
from scipy import linalg
A = np.matrix([[-1,0,0,1],[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]])
print(A)
#Câu 1
import numpy as np

# 1
A1 = np.array([[1, -1], [2, 3]])
b1 = np.array([-2, 6])
sol1 = np.linalg.solve(A1, b1)
print(" vấn đề 1", sol1)
#  2
A2 = np.array([[1, -1, 0], [2, -1, -1], [1, 1, 1]])
b2 = np.array([2, 3, 6])
sol2 = np.linalg.solve(A2, b2)
print(" vấn đề 2 ", sol2)

# 3
A3 = np.array([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
b3 = np.array([4, 3, 4])
sol3 = np.linalg.solve(A3, b3)
print(" vấn đề 3", sol3)
#  4
A4 = np.array([[1, 0, 1], [1, 1, -2], [-2, 2, 1]])
b4 = np.array([1, -3, 0])
sol4 = np.linalg.solve(A4, b4)
print(" vấn đề 4", sol4)
# câu 2.1
import sympy as sp
from sympy import Symbol
x= Symbol('x ')
y= Symbol('y ')
from sympy import solve
pt1 = x - y + 2
pt2 = 2*x + 3*y - 6
sol = solve([pt1, pt2], (x, y))
print("Nghiệm của hệ là:", sol)
# 2,2
x= Symbol('x')
y= Symbol('y')
z= Symbol('z')
pt1 = x - y - 2
pt2 = 2*x - y - z - 3
pt3 = x + y + z - 6
sol2 = solve([pt1, pt2, pt3], (x, y, z))
print("Nghiệm hệ phương trình:", sol2)
# 2.3
a= Symbol('a')
b= Symbol('b')
c= Symbol('c')
pt4 = a + b + c - 4
pt5 = 4*a + 2*b + c - 3
pt6 = 9*a + 3*b + c - 4
sol3 = solve([pt4, pt5, pt6], (a, b, c))
print("Hệ số đa thức bậc 2:", sol3)
#2.4
pt7 = a + c - 1
pt8 = a + b - 2*c + 3
pt9 = -2*a + 2*b + c
sol4 = solve([pt7, pt8, pt9], (a, b, c))
print("Nghiệm phân tích phân thức:", sol4)
#câu 3
from sympy import Matrix
F = Matrix([[1, 1], [1, 0]])
k = 5
Fk = F**k
print(f"Ma trận F^{k}:")
print(Fk)
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
F_check = Matrix([
    [fib(k+1), fib(k)],
    [fib(k), fib(k-1)]
])
print("Ma trận Fibonacci từ công thức:")
print(F_check)