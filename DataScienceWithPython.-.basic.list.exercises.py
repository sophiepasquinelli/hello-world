
# coding: utf-8

# ##A. match_ends

# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

# In[22]:

def match_ends(words):
    count=0
    for i in words:
        if len(i)>=2 and i[0]==i[len(i)-1]:
            count=count+1
    return count


# In[31]:

list=["letter","abcbca","test","winter","xanadu","xax"]
print match_ends(list)


# ##B. front_x

# Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them before combining them.

# In[35]:

def front_x(words):
    words_in_X=[]
    other_words=[]
    for i in words:
        if i[0]=="x" or i[0]=="X":
            words_in_X.append(i)
        else:
            other_words.append(i)
    words_in_X.sort()
    other_words.sort()
    return words_in_X+ other_words


# In[36]:

print front_x(list)


# ##C. sort_last

# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
# 

# In[47]:

def key(tuple):
    return tuple[len(tuple)-1]

def sort_last(tuples):
    sort_tuple =sorted(tuples, key=lambda tuple: tuple[len(tuple)-1] )
    return sort_tuple


# In[48]:

list2= [(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
print sort_last(list2)


# ##Testing the A,B and C fuctions :

# In[49]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
main()


# ##D. remove_adjacent

# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.

# In[53]:

def remove_adjacent(nums):
    new_nums=[]
    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
    return new_nums


# In[54]:

list3=[1,1,1,2,3,3]
print remove_adjacent(list3)


# ##E. linear_merge

# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.
# 
# Note: the solution above is kind of cute, but unforunately list.pop(0) is not constant time with the standard python list implementation, so the above is not strictly linear time. An alternate approach uses pop(-1) to remove the endmost elements from each list, building a solution list which is backwards. Then use reversed() to put the result back in the correct order. That solution works in linear time, but is more ugly.
# 

# In[68]:

def linear_merge(list1, list2):
    for i in list1:
        list2.append(i)
    list2.sort()
    return list2


# In[66]:

list4=["abc","zer","diu"]
list5=["abc","kjt"]
print linear_merge(list4,list5)


# ##Testing the D and E functions

# In[69]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()


# In[ ]:



