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


def get_result(oponent_choice, my_choice):
    if (oponent_choice == o_options["Paper"] and my_choice == m_options["Scissors"]) or (oponent_choice == o_options["Scissors"] and my_choice == m_options["Rock"]) or (oponent_choice == o_options["Rock"] and my_choice == m_options["Paper"]):
        return 6
    if (oponent_choice == o_options["Rock"] and my_choice == m_options["Rock"]) or (oponent_choice == o_options["Paper"] and my_choice == m_options["Paper"]) or (oponent_choice == o_options["Scissors"] and my_choice == m_options["Scissors"]):
        return 3
    return 0


def get_score(oponent_choice, my_choice):
    score = 0
    if my_choice == m_options["Rock"]:
        score += 1
    if my_choice == m_options["Paper"]:
        score += 2
    if my_choice == m_options["Scissors"]:
        score += 3
    score += get_result(oponent_choice, my_choice)
    return score


with open('2022/d2/input.txt', 'r', encoding='utf-8') as infile:
    tot_score = 0
    for line in infile:
        oponent_choice, my_choice = line.strip().split(' ')
        tot_score += get_score(oponent_choice, my_choice)
    print(tot_score)
