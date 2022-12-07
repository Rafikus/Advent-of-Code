
def get_priority(item):
  return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(item) + 1

def find_shared_items(first_compartment: str, second_compartment: str):
  shared_items = set()
  for item in first_compartment:
    if second_compartment.__contains__(item):
      shared_items.add(item)
  return shared_items


with open('2022/d3/input.txt', 'r', encoding='utf-8') as infile:
  tot_priority = 0
  for line in infile:
    line = line.strip()
    first_compartment = line[:int(len(line)/2)]
    second_compartment = line[int(-len(line)/2):]
    shared_items = find_shared_items(first_compartment, second_compartment)
    for item in shared_items:
      tot_priority += get_priority(item)
  print(tot_priority)
