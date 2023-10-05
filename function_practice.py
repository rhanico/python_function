def max_num(num1, num2, num3):
    return max(num1, num2, num3)


def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def rev_string(input_str):
    return input_str[::-1]



def num_within(number, start_range, end_range):
    return start_range <= number <= end_range




def pascal(n):
    def generate_next_row(previous_row):
        next_row = [1]
        for i in range(1, len(previous_row)):
            next_row.append(previous_row[i - 1] + previous_row[i])
        next_row.append(1)
        return next_row

    triangle = []
    current_row = [1]
    for _ in range(n):
        triangle.append(current_row)
        current_row = generate_next_row(current_row)

    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == "__main__":

    print("Max of 3, 6, 2:", max_num(3, 6, 2))

    numbers_to_multiply = [2, 4, 5]
    print("Product of [2, 4, 5]:", mult_list(numbers_to_multiply))


    input_string = "Hello, World!"
    print("Reversed String:", rev_string(input_string))

    print("Is 3 within the range [2, 4]:", num_within(3, 2, 4))
    print("Is 3 within the range [1, 3]:", num_within(3, 1, 3))
    print("Is 10 within the range [2, 5]:", num_within(10, 2, 5))


    n_rows = 5
    print(f"Pascal's Triangle ({n_rows} rows):")
    pascal(n_rows)
