'''
This script takes in a list of arguements as commandline arguements and prints
all possible words that can be formed with the specified length (specified in arguements).
It also creates a file named wordlist and saves the list of all the words in it.
'''

from sys import argv,exit

if len(argv)<2:
        exit("Usage: python combination.py <space separated alphabets> <length of each word>")

argv=argv[1:]

a=argv[:len(argv)-1]

try:
    repeat=int(argv[len(argv)-1])-1
except ValueError:
    exit("Last entered value should be an integer !")

def inc(i):
    return i%len(a)

l=[]

f=open('wordlist','w')

def ch_after(string,pos):
    if(pos==0):
        for i in range(len(a)):
            string=string[:repeat]+a[inc(i)]
            l.append(string)
            f.write(string+'\n')
    else:
        d=repeat-pos
        for i in range(len(a)):
            ch_after(string[:d]+a[inc(i)],pos-1)


ch_after(a[0]*(repeat+1),repeat)

print l
print "Total words = "+str(len(l))

f.close()
