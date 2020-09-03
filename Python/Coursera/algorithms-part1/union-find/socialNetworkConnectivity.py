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
def earliestTimeAllConnected(members, log):

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



    return ""