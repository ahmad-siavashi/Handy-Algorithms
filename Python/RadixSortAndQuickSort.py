# In his exalted name
# Algorithm: Radix Sort & Quick Sort Implementations
# Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
# Date: 11/9/2013

from random import *
from time import *

def radixSort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10
 
        if len(new_list[0]) == len_random_list:
            return new_list[0]
 
        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)
 


def quickSort(values):
    if values == []:
        return []
    else:
        pivot = values[len(values)/2-1]
        lesser = quickSort([x for x in values[1:] if x < pivot])
        greater = quickSort([x for x in values[1:] if x > pivot])
        return lesser + [pivot] + greater
            

random_data = []
for i in xrange(1000000):
    random_data.append(randrange(1,1000000))

random_data_quick = random_data[:]
tf = time()
quickSort(random_data_quick)
print 'Quick Sort : ', + (time()-tf)
random_data_radix = random_data[:]
tf = time()
radixSort(random_data_radix)
print 'Radix Sort : ', + (time()-tf)
