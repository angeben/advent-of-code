def get_combination(intervals):
    result = 0
    
    for interval in intervals:
        bounds = interval.split('-')

        lower_bound = bounds[0]
        upper_bound = bounds[1]

        if len(lower_bound) % 2 == 0:
            half = len(lower_bound) // 2
            left_digits = lower_bound[0:half]
            current_digits = int(left_digits)
            current_double_digits = int(2*left_digits)

        else:
            zeros = len(lower_bound) // 2
            current_digits = int("1" + "0" * zeros)
            current_double_digits = int(2*str(current_digits))

        while current_double_digits <= int(upper_bound):
            if current_double_digits >= int(lower_bound):
                result += current_double_digits
            current_digits += 1
            current_double_digits = int(2*str(current_digits))
            
    return result

def main():
    # Open and read input file
    input_path = "inputs/02.txt"
    with open(input_path, 'r') as f:
        input = f.read()

    # Process input
    intervals = input.split(',')

    # Calculate result
    result = get_combination(intervals)
    print(f'Solution is {result}')

if __name__ == "__main__":
    main()