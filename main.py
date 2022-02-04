
def sorted_func(list, sum):
    """
    This function returns True if the sum of two numbers in the sorted input sequence is equal to input sum
    Big O ~ O(N)
    :param list: input sequence
    :param sum: input sum
    :return: True/False
    """
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




def func_comparison(list, sum):
    """
    This function returns True if the sum of two numbers in the sorted input sequence is equal to input sum
    Big O ~ O(N)
    :param list: input sequence
    :param sum: input sum
    :return: True/False
    """
    num_set = set(list)
    for num in num_set:
        if num == sum // 2:
            if list.count(num) >= 2:
                return True
        elif sum - num in num_set:
            return True
    else:
        return False


def func_dict(list, sum):
    """
    This function returns True if the sum of two numbers in the sequence is equal to input sum, algorithm uses dictionary
    Big O ~ O(N)
    :param list: input sequence
    :param sum: input sum
    :return: True/False
    """
    hash = {}
    for num in list:
        if num in hash:
            return True
        key = sum - num
        hash[key] = num
    return False




if __name__ == '__main__':
    a_1 = [3, 5, 7, 8, 11]
    a_2=[3, 5, 6, 8, 11]
    b=10

    print('Test 1:')
    print(sorted_func(a_1,b))
    print(func_comparison(a_1,b))
    print(func_dict(a_1,b))
    print('\n')

    print('Test 2:')
    print(sorted_func(a_2,b))
    print(func_comparison(a_2,b))
    print(func_dict(a_2,b))





