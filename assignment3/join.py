import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    order_id = record[1]

    # Emit as key to shuffle the order id, and the whole record
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of records with that order_id matched
    orders      = filter(lambda x:x[0] == 'order', list_of_values)
    line_items  = filter(lambda x:x[0] == 'line_item', list_of_values)

    # Cross Product
    joined_records = [o + l for o in orders for l in line_items]

    for r in joined_records:
      mr.emit(r)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
