# input = range(112233, 112234)
# input = range(123444, 123445)
# input = range(112111, 112112)
# input = range(111122, 111123)
input = range(152085, 670284)


def check_mult_length(agg, x, candidate):
    if x and x[0] == candidate:
        return check_mult_length(agg + 1, x[1:], candidate)
    return agg


def is_password_valid(password):
    if len(password) != 6:
        return False
    current_index = 0
    mult_lengths = []
    while current_index < 5:
        if password[current_index + 1] < password[current_index]:
            return False
        if password[current_index + 1] == password[current_index]:
            mult_length = check_mult_length(
                0, password[current_index:], password[current_index]
            )
            mult_lengths.append(mult_length)
            current_index += mult_length - 1
        else:
            current_index += 1
    return mult_lengths and min(mult_lengths) == 2


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    result = 0
    for j in input:
        if is_password_valid(str(j)):
            result += 1
    print(result)
