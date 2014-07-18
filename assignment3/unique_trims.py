import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    seq_id = record[0]
    nucleotide = record[1]

    # Emit as key the trimmed nucleotide and the seq_id as value
    mr.emit_intermediate(nucleotide[:-10], seq_id)

def reducer(key, list_of_values):
    # key: trimmed seq
    # value: list of seqs
    
    # Just emit the trimmed nucleotide
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
