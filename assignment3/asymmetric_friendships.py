import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]

    # The key I choose is the normalized form of the edge tuple, sorted
    key = [person, friend]
    key.sort()

    # Emit as key to shuffle the person, passing the tuple to string to be hashable
    mr.emit_intermediate("%s--%s" % (key[0], key[1]), record)

def reducer(key, list_of_values):
    # key: normalized list with the two persons
    # value: list of records

    # If there's only one edge (the relation is asymmetric), emit it and the reversed
    if len(list_of_values) == 1:
    	for relation in list_of_values:
    		mr.emit((relation[0], relation[1]))
    		mr.emit((relation[1], relation[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
