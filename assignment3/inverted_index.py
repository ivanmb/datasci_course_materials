import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      # Emit that we can find the word w in the document with id key
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document with occurrence

    # Remove duplicates
    docids = list(set(list_of_values))
    mr.emit((key, docids))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
