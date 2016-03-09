
# coding: utf-8

# ##A. donuts

# Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where  is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
# 

# In[84]:

def donuts(count):
    if count<10:
        return 'Number of donuts: ' +str(count)
    else:
        return 'Number of donuts: many'


# In[9]:

print donuts(2)
print donuts(23)


# ##B. both_ends

# Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.

# In[17]:

def both_ends(s):
    to_return=""
    if len(s)>=2:
        to_return=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    return to_return


# In[20]:

print both_ends("spring")
print both_ends("N")
print both_ends("abc")


# ##C. fix_start

# Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
# 
# e.g. 'babble' yields 'ba**le'
# 
# Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.
# 

# In[76]:

def fix_start(s):
    t=s[1:len(s)]
    print t
    new_t=t.replace(s[0],"*")
    new_t=s[0]+new_t
    return new_t


# In[75]:

print fix_start("babble")


# ##D. MixUp

# Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
# 'mix', pod' -> 'pox mid'
# 'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
# 

# In[86]:

def mix_up(a, b):
    new_a=b[0]+b[1]+a[2:len(a)]
    new_b=a[0]+a[1]+b[2:len(b)]
    return new_a + " " + new_b


# In[87]:

mix_up("dog", "pih")


# ## Testing A,B,C and D functions

# In[88]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

main()


# ##D. verbing

# Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.

# In[116]:

def verbing(s):
    if len(s)>=3:
        if s[len(s)-3:len(s)]=="ing":
            return s+"ly"
        else:
            return s+"ing"
    else:
        return s


# In[99]:

print verbing("play")
print verbing("adding")


# ##E. not_bad

# Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields: This dinner is good!
# 

# In[107]:

def not_bad(s):
    position_not=s.find("not")
    position_bad=s.find("bad")
    if position_bad>position_not:
        new_s=s[0:position_not]+"good"+s[position_bad+3:len(s)]
    else:
        new_s=s
    return new_s


# In[108]:

print not_bad('This dinner is not that bad!')


# ##F. front_back

# Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back
# 

# In[139]:

def front_back(a, b):
    if len(a)%2==0:
        front_a=a[0:len(a)/2]
        back_a=a[len(a)/2:len(a)]
    else:
        front_a=a[0:len(a)/2+1]
        back_a=a[len(a)/2+1:len(a)]
    if len(b)%2==0:
        front_b=b[0:len(b)/2]
        back_b=b[len(b)/2:len(b)]
    else:
        front_b=b[0:len(b)/2+1]
        back_b=b[len(b)/2+1:len(b)]
    return front_a+front_b+back_a+back_b


# In[140]:

print front_back("abcdefg","hijkl")


# ## Testing D, E and F functions

# In[141]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()
    


# In[ ]:



