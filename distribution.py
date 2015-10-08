"""
distribution.py
Author: James Napier
Credit: http://stackoverflow.com/questions/27052625/python-variable-scope-and-parameters-issue/27065914#27065914, http://stackoverflow.com/questions/963161/python-display-string-multiple-times

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

stringCD=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+stringCD+'" is: ')

ChDis=stringCD.lower()
#letters=list(x for x in string.ascii_letters)
letlist=list(string.ascii_lowercase)
count=(x for x in letlist)
for x in letlist:
    mylist=((x)*ChDis.count(x))
    print(mylist)
        
