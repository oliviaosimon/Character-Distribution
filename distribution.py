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
    
a = text.count('a')
if a>0:
    print('a'*a)
b = text.count('b')
if a>0:
    print('b'*b)
c = text.count('c')
if c>0:
    print('c'*c)
d = text.count('d')
if d>0:
    print('d'*d)
e = text.count('e')
if e>0:
    print('e'*e)
f = text.count('f')
if f>0:
    print('f'*f)
g = text.count('g')
if g>0:
    print('g'*g)
h = text.count('h')
if h>0:
    print('h'*h)
i = text.count('i')
if i>0:
    print('i'*i)
j = text.count('j')
if j>0:
    print('j'*j)
    
    
#b = text.count('b')
#if b>0:
#    print('b'*b)






