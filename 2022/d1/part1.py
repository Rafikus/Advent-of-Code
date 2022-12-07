

with open('2022/d1/input.txt', 'r', encoding='utf-8') as infile:
  elfs = []
  current_elf = 0
  for line in infile:
    if line == "\n":
      current_elf += 1
      continue
    if len(elfs) == current_elf:
      elfs.append(0)
    elfs[current_elf] += int(line)
  print(max(elfs))
