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

#def sort_list(list1, list2): 
  
    #zipped_pairs = zip(list2, list1) 
  
    #z = [x for _, x in sorted(zipped_pairs, reverse=True)] 
      
    #return z 

#Variables

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
    
#both = zip(alpha, alphaNum)
#for item_alpha, item_alphaNum in both:
    #myList = (list(item_alpha*item_alphaNum))
    #print(myList)

#bothList = (list(both))
# sorting
#result = (a[0] * a[1] for a in both)

#sorting = (sort_list(alpha, alphaNum)) 
#print(sorting)

printingList = list()
for x in alpha:
    while text.count(x) > 0:
        printingList.append(x)
    distribution = ((text.count(x))*x)

print(printingList)

