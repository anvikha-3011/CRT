'''
#string: Collection of characters enclosed ' ', " ", or ''' '''.
s = "python"
print(s[2])
print(s[-1])
print(s[1:])

print(s.capitalize())
print(s)

s.replace('p', 'P')
print(s)
'''
'''
#Reverse a string without using built-in functions and slicing.
st = input()
res = ""
stop = -1 * (len(st) + 1)
for i in range(-1, stop, -1):
    res += st[i]
print(res)
'''
'''
#Methodd-2: Using a loop 
s = input()
res = ""
for ch in s:
    res = ch + res
print(res)
'''
'''
#Using functions to reverse a string
def reverse_string(s):
    res = ""
    for ch in s:
        res = ch + res
    return res
print(reverse_string("python"))

def is_palindrome(s):
    return s == reverse_string(s)
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

def frequency_count(s):
    pass 
print(frequency_count("abcabc"))
'''
'''
def frequency_count(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d
print(frequency_count("abcabc"))
def is_anagram(s1, s2):
    return frequency_count(s1) == frequency_count(s2)

print(is_anagram("space", "paces"))
print(is_anagram("abc", "abcabc"))
'''
#3,13,28*,38,43*,65,151,165*,242,389*,771
