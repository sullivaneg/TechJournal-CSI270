#NOT MY CODE

from collections import Counter
import timeit
import time

s1="listen"
s2="silent"
s3="abcdd"
s4="bcadd"
s5="abcda"
def test1():
    "-".join(str(n) for n in range(100))



start = time.time()
print (start)
for x in range(1, 10000):
    test1()

#end = time.time()
#print(end)
#y=end - start


#print(y)

#ANAGRAM 1
def anagram1(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return True
    else:
        return False




print("ANAGRAM1")
a11 = timeit.timeit('anagram1(s1,s2)', globals=globals())
a12 = timeit.timeit('anagram1(s3,s5)', globals=globals())
print(a11)
print(a12)
times = {'Anagram1':[a11, a12]}

print(times)

#ANAGRAM 2
def anagram2(word1, word2):
    #deal with length first
    if len(word1) != len(word2):
       return False
    #convert to lists
    worda=list(word1)
    wordb=list(word2)
    for letter in worda:
        #if a letter is not in the second word
        if letter not in wordb:
            return False
        else:
            #if it is , take it out of the second array to deal with repeats
            wordb.remove(letter)
    if len(wordb)== 0:
        return True
    else:
        return False

print("ANAGRAM2")
a21 = timeit.timeit('anagram2(s1,s2)', globals=globals())
a22 = timeit.timeit('anagram2(s3,s5)', globals=globals())
print(a21)
print(a22)
times.update({'Anagram2':[a21, a22]})
print(times)

#ANAGRAM 3
def anagram3(word1, word2):
    if Counter(word1) == Counter(word2):
        return True
    else:
        return False

print("ANAGRAM3")
a31 = timeit.timeit('anagram3(s1,s2)', globals=globals())
a32 = timeit.timeit('anagram3(s3,s5)', globals=globals())
print(a31)
print(a32)
times.update({'Anagram3':[a31, a32]})
print(times)

#ANAGRAM 4
def anagram4(word1, word2):
    #convert to lists
    worda=list(word1)
    wordb=list(word2)
    worda.sort()
    wordb.sort()
    if worda==wordb:
        return True
    else:
        return False

print("ANAGRAM4")
a41 = timeit.timeit('anagram4(s1,s2)', globals=globals())
a42 = timeit.timeit('anagram4(s3,s5)', globals=globals())
print(a41)
print(a42)
times.update({'Anagram4':[a41, a42]})
print(times)

#ANAGRAM 5
def anagram5(word1, word2) :
    # if the length of the two strings is not the same, they are not anagrams.
    if len(word1) != len(word2):
        return False

    # initialize the dictionary
    counts = {}

    # loop simultaneously through the characters of the two strings.
    for c1, c2 in zip(word1, word2):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1

    # Loop through the dictionary values.
    # if the dictionary contains even one value which is
    # different than 0, the strings are not anagrams.
    for count in counts.values():
        if count != 0:
            return False
    return True
print("ANAGRAM5")
print(timeit.timeit('anagram5(s1,s2)', globals=globals()))
print(timeit.timeit('anagram5(s3,s5)', globals=globals()))
a51 = timeit.timeit('anagram5(s1,s2)', globals=globals())
a52 = timeit.timeit('anagram5(s3,s5)', globals=globals())
print(a51)
print(a52)
times.update({'Anagram5':[a51, a52]})
print(times)



print(anagram1( s1,s2))
#print(anagram1( s3,s4))
print(anagram1( s3,s5))
#print(anagram2( s1,s2))
#print(anagram2( s3,s4))
#print(anagram2( s3,s5))
#print(anagram3( s1,s2))
#print(anagram3( s3,s4))
#print(anagram3( s3,s5))
#print(anagram5( s1,s2))
#print(anagram5( s3,s4))
#print(anagram5( s3,s5))

def time_analysis():
    percent_diff = ((a21-a11)/a11) * 100
    if(percent_diff > 0):
        print("ANAGRAM1 is more efficient than ANAGRAM2 by",round(percent_diff,2),"percent.")
    else:
        print("ANAGRAM1 is less efficient than ANAGRAM2 by", round(percent_diff, 2),"percent.")

time_analysis()

print(times.get('Anagram1')[0])
print(times.values())

x0 = times.get('Anagram1')[0]
x1 = times.get('Anagram2')[0]

eff = ((x1-x0)/x0) * 100
if(eff > 0):
    print("ANAGRAM1 is more efficient than ANAGRAM2 by", round(eff, 2), "percent.")
else:
    print("ANAGRAM1 is less efficient than ANAGRAM2 by", round(eff, 2), "percent.")
