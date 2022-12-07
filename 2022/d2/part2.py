
o_options = {
  "Rock": "A",
  "Paper": "B",
  "Scissors": "C"
}

m_options = {
  "Rock": "X",
  "Paper": "Y",
  "Scissors": "Z"
}

o_optionsArray = ["A", "B", "C"]
m_optionsArray = ["X", "Y", "Z"]

def get_my_choice(oponent_choice, result_needed):
  option_index = o_optionsArray.index(oponent_choice)
  if result_needed == "Z": return m_optionsArray[(option_index + 1) % len(m_optionsArray)]
  if result_needed == "Y": return m_optionsArray[option_index]
  if result_needed == "X": return m_optionsArray[option_index - 1]

def get_result(oponent_choice, my_choice):
  if (oponent_choice == o_options["Paper"] and my_choice == m_options["Scissors"]) or (oponent_choice == o_options["Scissors"] and my_choice == m_options["Rock"]) or (oponent_choice == o_options["Rock"] and my_choice == m_options["Paper"]):
    return 6
  if (oponent_choice == o_options["Rock"] and my_choice == m_options["Rock"]) or (oponent_choice == o_options["Paper"] and my_choice == m_options["Paper"]) or (oponent_choice == o_options["Scissors"] and my_choice == m_options["Scissors"]):
    return 3
  return 0
  

def get_score(oponent_choice, my_choice):
  score = 0
  if my_choice == m_options["Rock"]: score += 1
  if my_choice == m_options["Paper"]: score += 2
  if my_choice == m_options["Scissors"]: score += 3
  score += get_result(oponent_choice, my_choice)
  return score
  

with open('d2/input.txt', 'r', encoding='utf-8') as infile:
  tot_score = 0
  for line in infile:
    oponent_choice, result_needed = line.strip().split(' ')
    my_choice = get_my_choice(oponent_choice, result_needed)
    print("🚀 ~ file: part2.py:45 ~ my_choice", my_choice)
    tot_score += get_score(oponent_choice, my_choice)
  print(tot_score)