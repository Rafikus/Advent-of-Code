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
    top3 = sorted(elfs)[-3:]
    top3_calories = 0
    for elf in top3:
        top3_calories += elf
    print(top3_calories)
