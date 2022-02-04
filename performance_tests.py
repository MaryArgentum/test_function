import timeit

setup_1 = '''
def sorted_func(list, sum):

    #list.sort() - this list has been already sorted
    i = 0
    j = len(list)-1

    while i != j:
        s = list[i]+list[j]
        if s == sum:
            return True
        elif s < sum:
            i += 1
        else:
            j -= 1
    return False
'''




setup_2 = '''
def func_comparison(list, sum):

    num_set = set(list)
    for num in num_set:
        if num == sum // 2:
            if list.count(num) >= 2:
                return True
        elif sum - num in num_set:
            return True
    else:
        return False
'''

setup_3 = '''
def func_dict(list, sum):

    hash = {}
    for num in list:
        if num in hash:
            return True
        key = sum - num
        hash[key] = num
    return False

'''

stmt_1 = '''
a=[3, 5, 7, 8, 11]
b=10
sorted_func(a,b)
'''

stmt_2 = '''
a=[3, 5, 7, 8, 11]
b=10
func_comparison(a, b)
'''

stmt_3 = '''
a=[3, 5, 7, 8, 11]
b=10
func_dict(a,b)
'''

print('Sorted function is:', timeit.timeit(stmt_1,setup_1,number=10000))
print('Comparison function is:',timeit.timeit(stmt_2,setup_2,number=10000))
print('Function with dictionary is:',timeit.timeit(stmt_3,setup_3,number=10000))
