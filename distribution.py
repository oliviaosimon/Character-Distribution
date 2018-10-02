"""
distribution.py
Author: Olivia Simon
Credit: Null

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

text = input("Please enter a string of text (the bigger the better): ").lower()
print('The distribution of characters in "'+text+'" is:')
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Variables
letters = (text.count(x) for x in alpha)
print(list(letters))


a = text.count('a')
b = text.count('b')
c = text.count('c')
d = text.count('d')
e = text.count('e')
f = text.count('f')
g = text.count('g')
h = text.count('h')
i = text.count('i')
j = text.count('j')
k = text.count('k')
l = text.count('l')
m = text.count('m')
n = text.count('n')
o = text.count('o')
p = text.count('p')
q = text.count('q')
r = text.count('r')
s = text.count('s')
t = text.count('t')
u = text.count('u')
v = text.count('v')
w = text.count('w')
x = text.count('x')
y = text.count('y')
z = text.count('z')

#variable amounts
alphaNum = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

#functions
myList = ((y*x) for y in alpha for x in alphaNum)
print(''.join(list(myList)))
    

    
    
#b = text.count('b')
#if b>0:
#    print('b'*b)






