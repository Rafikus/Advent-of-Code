
ELFS_IN_GROUP = 3

def get_priority(item):
  return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(item) + 1

def find_shared_items(first_compartment: set, second_compartment: set):
  shared_items = set()
  for item in first_compartment:
    if second_compartment.__contains__(item):
      shared_items.add(item)
  return shared_items


with open('2022/d3/input.txt', 'r', encoding='utf-8') as infile:
  tot_priority = 0
  index = 0
  lines = []
  for line in infile:
    index = (index + 1) % ELFS_IN_GROUP
    lines.append(line.strip())
    if index % 3 == 0:
      shared_items = find_shared_items(lines[-1], lines[-2])
      final_shared = find_shared_items(shared_items, lines[-3])
      for item in final_shared:
        tot_priority += get_priority(item)
  print(tot_priority)
