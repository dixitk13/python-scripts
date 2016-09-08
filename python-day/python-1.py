#!/usr/bin/python
import re
from sys import argv
import heapq
import random
from os.path import exists


class Point():
	def __init__(self, _x, _y):
		self.x = _x
		self.y = _y

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __str__(self):
		return str(self.__dict__)

	def __repr__(self):
		return self.__str__()

	def __lt__(self, other):
		if self.x == other.x:
			return self.y < other.y
		else:
			return self.x < other.x

	def __ne__(self, other):
		return not self.__eq__(other)

	def __gt__(self, other):
		return other.__lt__(self)

	def __hash__(self):
		return hash(self.x) + hash(self.y)


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# indata = open("cover_letter.txt").read()

# with open("cover_letter.txt") as f:
# 	for line in f:
# 		print line


# lst = [11,12,31]

# for i,e in enumerate(lst):
# 	print i, e

# print exists("cover_letter.txt")
# print exists("cover_letter1.txt")

mylist = [x*x for x in range(3)]
mygenerator = (x*x for x in range(3))

p1 = Point(1,1)
p2 = Point(2.2, 2.2)
p11 = Point(1,1)
p3 = Point(1,3)

print p1, p2, p3
print p1 == p3
print p1 == p2

lst = []
lst.append(p1)
lst.append(p2)
lst.append(p3)

lst2 = [p1, p2, p3, p11]

print lst
print 'sorted on x => ', sorted(lst)
lst.sort()
print 'lst.sort() on lst', lst

print 'lambda sorted on y => ', sorted(lst, key=lambda x: x.y, reverse=True)
print 'lambda sorted on x => ', sorted(lst, key=lambda x: x.x, reverse=True)

print 'new lst ', lst2
lst3 = lst2
print 'before removing lst3 = ', lst3, ' lst2', lst2 
lst3.remove(p1)
print 'after removing lst3 = ', lst3, ' lst2', lst2 
lst_set = set(lst2) 
print 'new set ', lst_set

q = random.sample(range(10), 10)

# xrange(0, 10) iss same as range(10)
# for i in xrange(0, 10):
# 	q.append(i)

print q
heapq.heapify(q)
print q

heapq.heappush(q, 10)

print q
# print indata


student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'C', 10),
        ('1dave', 'D', 1),
]

def reverse3rd(t1, t2):
	return t1[2] - t2[2]


def reverse3rd2(t1, t2):
	return t2[2] - t1[2]


print sorted(student_tuples, key=lambda x : x[0], reverse = True)
print sorted(student_tuples, cmp=reverse3rd)
print sorted(student_tuples, cmp=reverse3rd2)


line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
