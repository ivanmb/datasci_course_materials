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

    # Emit as key to shuffle the person and count 1 friend
    mr.emit_intermediate(person, 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend count
    
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
