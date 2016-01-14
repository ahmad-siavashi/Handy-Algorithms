# In his exalted name
# Algorithm: Counting Sort
# Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
# Date: 24/4/2014
def csort(A):
    B = [[]]*len(A)
    C = []
    for i in xrange(max(A)-min(A)+1):
        C.append(0)
    for j in A:
        C[j-min(A)] += 1
    for i in xrange(1,len(C)):
        C[i] += C[i-1]
    A.reverse()
    for j in A:
        B[C[j-min(A)]-1] = j
        C[j-min(A)] -= 1
    return B


A = [6,4,3,2,7,9]
print csort(A)
