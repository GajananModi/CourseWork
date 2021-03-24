#from collections import deque 
import collections
from num2words import num2words
class Node:
    def __init__(self, data):
        self.data = int(data)
        self.l = None
        self.r = None

    def takeinput(self):
        data,datal = input().split(" ")
        datal = int(datal)
        self.data = data
        if datal != -1:
            self.l = Node(datal)
            #print ("assigned left child with ", datal)

        data,datar = input().split(" ")
        datar = int(datar)
        if datar != -1:
            self.r = Node(datar)
        #    print ("assgned right child with ", datar)

    def preorder(self):
        
        print(self.data)
        if self.l:
            self.l.preorder()
        if self.r:
            self.r.preorder()

    def printleaves(self):
        if self is None:
            return []
        if self.l is None and self.r is None:
            
            #count += self.data
            return [self.data]

        ret = []
        if self.l:
            ret += self.l.printleaves()
        if self.r:
            ret += self.r.printleaves()
        return ret

    def printleftboundary(self):
        if self.l is None and self.r is None:
            return []
        ret = [self.data]
        if self.l:
            ret += self.l.printleftboundary()
        elif self.r:
            ret += self.r.printleftboundary()

        return ret

    def printrightboundary(self):
        if self.l is None and self.r is None:
            return []

        ret = []
        if self.r:
            ret += self.r.printrightboundary()
        elif self.l:
            ret += self.l.printrightboundary()
        ret += [self.data]
        return ret
      

n = int(input())

if n <= 0:
   print("Total Amount : zero")
   print("Order : ")
   exit()

root = Node(0)

q = collections.deque([root])
first = True
count = 1
while len(q) > 0  and count < n:
    cur = q.popleft()
    cur.takeinput()
    if first == True:
        first = False
        root = cur

    if cur.l != None:
        q.append(cur.l)
        count += 1
    if cur.r != None:
        q.append(cur.r)
        count +=1

    '''print ("q is ", end = "")
    for i in q:
        print (i.data, end = " ")
    print()
    '''

#make sure root l and r exist
ret = [root.data]
ret += root.l.printleftboundary()
ret += root.l.printleaves()
ret += root.r.printleaves()
ret += root.r.printrightboundary()

amount = 0
for i in ret:
    amount += int(i)

print ("Total Amount : ", num2words(amount))
print ("Order : ", end = "")
for i in range(0,len(ret)):
    x = num2words(int(ret[i]))
    if (i == len(ret)-1):
        print (x,end="")
    else :
        print (x,end = ", ")
        

'''
PDF INPUT:
10
40 20
40 60
20 10
20 30
60 50
60 70
10 -1
10 5
30 -1
30 -1
50 -1
50 55
70 -1
70 -1
5 -1
5 45
'''
