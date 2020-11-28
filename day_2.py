# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import floor

input = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    1,
    9,
    19,
    1,
    5,
    19,
    23,
    1,
    6,
    23,
    27,
    1,
    27,
    10,
    31,
    1,
    31,
    5,
    35,
    2,
    10,
    35,
    39,
    1,
    9,
    39,
    43,
    1,
    43,
    5,
    47,
    1,
    47,
    6,
    51,
    2,
    51,
    6,
    55,
    1,
    13,
    55,
    59,
    2,
    6,
    59,
    63,
    1,
    63,
    5,
    67,
    2,
    10,
    67,
    71,
    1,
    9,
    71,
    75,
    1,
    75,
    13,
    79,
    1,
    10,
    79,
    83,
    2,
    83,
    13,
    87,
    1,
    87,
    6,
    91,
    1,
    5,
    91,
    95,
    2,
    95,
    9,
    99,
    1,
    5,
    99,
    103,
    1,
    103,
    6,
    107,
    2,
    107,
    13,
    111,
    1,
    111,
    10,
    115,
    2,
    10,
    115,
    119,
    1,
    9,
    119,
    123,
    1,
    123,
    9,
    127,
    1,
    13,
    127,
    131,
    2,
    10,
    131,
    135,
    1,
    135,
    5,
    139,
    1,
    2,
    139,
    143,
    1,
    143,
    5,
    0,
    99,
    2,
    0,
    14,
    0,
]

# examples = [
#     [1, 0, 0, 0, 99],
#     [2, 3, 0, 3, 99],
#     [2, 4, 4, 5, 99, 0],
#     [1, 1, 1, 4, 99, 5, 6, 0, 99],
# ]
# expected_results = [
#     [2, 0, 0, 0, 99],
#     [2, 3, 0, 6, 99],
#     [2, 4, 4, 5, 99, 9801],
#     [30, 1, 1, 4, 2, 5, 6, 0, 99],
# ]


def run_program(item):
    current_index = 0
    while current_index <= len(item):
        if item[current_index] == 99:
            break
        if item[current_index] == 1:
            item[item[current_index + 3]] = (
                item[item[current_index + 1]] + item[item[current_index + 2]]
            )
            current_index += 4
            continue
        if item[current_index] == 2:
            item[item[current_index + 3]] = (
                item[item[current_index + 1]] * item[item[current_index + 2]]
            )
            current_index += 4
            continue
    return item[0]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    for noun in range(1, 100):
        for verb in range(1, 100):
            item = input.copy()
            item[1] = noun
            item[2] = verb
            result = run_program(item)
            if result == 19690720:
                print(100 * noun + verb)
                break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
