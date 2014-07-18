import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

MAX_ROWS_A = MAX_COLS_B = 5

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if matrix == 'a':
      # If A, Emit i,k for every k in 1..N with index column
      for k in range(0, MAX_ROWS_A):
        mr.emit_intermediate((i,k), (matrix, j, value))
    else:
      # If B, Emit k,j for every k in 1..L with index row
      for k in range(0, MAX_COLS_B):
        mr.emit_intermediate((k, j), (matrix, i, value))

def reducer(key, list_of_values):
  val_a = dict()
  val_b = dict()

  for rec in list_of_values:
    if rec[0] == 'a':
      val_a[rec[1]] = rec[2]
    else:
      val_b[rec[1]] = rec[2]

  # Map over one dict items and multiply with the corresponding other
  value = sum(map(lambda (k,v): (v * val_b.get(k, 0)) , val_a.iteritems()))

  if value != 0:
    mr.emit((key[0], key[1], value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
