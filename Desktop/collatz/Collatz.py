#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array of int
return true if that succeeds, false otherwise
"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0

    if i>j:
        i,j = j,i

    w = open("output.txt","w")
    
    cacheRange = 10000
    cache=[0]*cacheRange
    max = 0
    for x in range(i, j):

        w.write(str(x)+"\n")
        cycle = 1
        if x<cacheRange:
            if cache[x]!=0:
                cycle=cache[x]
        else:
            while x>1:
                cycle = cycle+1
                if x%2==0:
                    x=int(x/2)
                else:
                    x=int(3*x+1)
                if x<cacheRange:
                    cache[x]=cycle
        w.write("cyclye"+str(max)+"\n")
        if cycle>max:
            max = cycle
    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
prints the values of i, j, and v
w is a writer
i is the beginning of the range, inclusive
j is the end of the range, inclusive
v is the max cycle length
"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
