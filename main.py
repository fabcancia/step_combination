def combination_steps(number_of_step, answer, temp, steps, index):
    if number_of_step == 0:
        answer.append(list(temp))
        return
    for i in range(index, len(steps)):
        if (number_of_step - steps[i]) >= 0:
            temp.append(steps[i])
            combination_steps(number_of_step - steps[i], answer, temp, steps, i)
            temp.remove(steps[i])

def get_user_input():
    number_of_step = input("Number of Steps: ")
    try:
        number_of_step = int(number_of_step)
    except ValueError:
        print("Not an Integer, retry")
        return get_user_input()
    try:
        if number_of_step < 0:
            raise ValueError
    except ValueError:
        print("Not a positive Integer, retry")
        return get_user_input()
    return number_of_step


def get_combination():
    number_of_step = get_user_input()
    if number_of_step == 0:
        return 0
    else:
        answer = []
        temp = []
        steps = [1, 2]
        combination_steps(number_of_step, answer, temp, steps, 0)
        return answer
if __name__ == '__main__':
    print(get_combination())
