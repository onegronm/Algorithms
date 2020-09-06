#* Coursera - Algorithms Part I
#* Week 1 - Interview Questions - Union Find
#* Question 1: Social network connectivity
#*
#* Given a social network containing N members and a log file containing M
#* timestamps at which times pairs of members formed friendships, design an
#* algorithm to
#      determine the earliest time at which all members are connected
#      *(i.e., every member is a friend of a friend of a friend ... of a friend).
#
#* Assume that the log file is sorted by timestamp and that friendship is an
#* equivalence relation. The running time of your algorithm should be M log N or
#* better and use extra space proportional to N.
#
# 0 1 2015-08-14 18:00:00
# 1 9 2015-08-14 18:01:00
# 0 2 2015-08-14 18:02:00
# 0 3 2015-08-14 18:04:00

# members = [0, 1, 2, 3, ...]
# log = [[0, 1, '2015-08-14 18:00:00'],
#        [1, 9, '2015-08-14 18:01:00'] ,
#        [0, 2, '2015-08-14 18:02:00']]
# return type: string

# not doing a search
# verify when all nodes are connected
# that is, when they all have the same root
# we can use a quick-union algorithm
# quick union uses an array where the index is the node
# and the value is the node connected to i
# because we want to keep a m log n running time
# we need to use a weighted QU by size or by height


# QU requires the following operations:
# initialize(p,q)
# connected(p,q)
# union(p,q)

# keep a count of each successful connection
# if a connection already exists, skip
# return the timestamp of the node when count = N

# or...
# after each union, check the number of connected components
# if only one is left, then all nodes are connected

# implement and decide
class QuickUnionUF:

	arr = []
	size = []

	def __init__(self, n):
		self.arr = [0] * n
		self.size = [0] * n

		for i in range(0,n):
			self.arr[i] = i
			self.size[i] = 1

	# find the root
	def root(self, i):
		while i is not self.arr[i]: # when i == d[i], we have reached the root
			i = self.arr[i] # chase parent pointers until root is reached
		return i;

	def connected(self, p, q):
		return self.root(p) is self.root(q)

	def union(self, p, q):

		i = self.root(p)
		j = self.root(q)

		if self.size[j] >= self.size[i]:
			self.arr[i] = j
			self.size[j] += self.size[i] # don't have to worry about counting nodes in root()! Size is updated in place
		else:
			self.arr[j] = i
			self.size[i] += self.size[j]

		if self.size[i] == n or self.size[j] == n:
			return True
		else:
			return False

def socialNetworkConnectivity(n, log):

	u = QuickUnionUF(n)

	for i in range(0, len(log)):
		p = log[i][0]
		q = log[i][1]
		t = log[i][2]
		if not u.connected(p, q):
			if u.union(p, q):
				print(t) # return earlist time all nodes connected
			

n = 4
log = [	
	[0, 1, '2015-08-14 18:00:00'],
	[1, 2, '2015-08-14 18:01:00'],
	[2, 3, '2015-08-14 18:02:00']
]

socialNetworkConnectivity(n, log)

		






