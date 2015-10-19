"""
distribution.py
Author: James Napier
Credit: http://stackoverflow.com/questions/27052625/python-variable-scope-and-parameters-issue/27065914#27065914, http://stackoverflow.com/questions/963161/python-display-string-multiple-times, https://docs.python.org/3/howto/sorting.html, http://stackoverflow.com/questions/4800811/accessing-a-value-in-a-tuple-that-is-in-a-list,http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value, http://stackoverflow.com/questions/13482313/sort-a-list-of-tuples-alphabetically-and-by-value, https://docs.python.org/3.1/library/operator.html, http://stackoverflow.com/questions/18595686/how-does-operator-itemgetter-and-sort-work-in-python, http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python

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
import string, random, operator

stringCD=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+stringCD+'" is: ')

ChDis=stringCD.lower()
#letters=list(x for x in string.ascii_letters)
letlist=list(string.ascii_lowercase)
count=(x for x in letlist)
mylistcount=[ChDis.count(x) for x in letlist]
mylist = [(x)*ChDis.count(x) for x in letlist]
for x in letlist:
    count = stringCD.count(x)
    if count > 0:
        needsort=(x)*count
        http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
#print(sorted(mylist))


####mylistcount=[ChDis.count(x) for x in letlist]

####MLLC=zip(mylistcount, mylist)
####MLLCr=sorted(MLLC, reverse=True)

#for x in MLLCr:
    #if x[0]>0:
       # print(x[1])
#if ([x[0] for x in MLLCr])>0:
    #print(int([x[]for x in MLLCr])+1) 
    #errors in two lines above. Not sure what is wrong
#else:
    #print("Lol")
#mylist = []
#for x in letlist:
    #mylist.append((x)*ChDis.count(x))

#SortMLLCr=(x[0] for x in MLLCr)
#print(SortMLLCr)
#print(sorted(MLLCr, key=lambda x:(x[0],-x[1])))

####temp = sorted(MLLCr, key=operator.itemgetter(0), reverse=True)

####temp2 = sorted( temp, key=operator.itemgetter(1))
    
####print(sorted(temp2, key=operator.itemgetter(0), reverse=True))
#find a way to order the tuples by alphabetical order and still keep numerical order
