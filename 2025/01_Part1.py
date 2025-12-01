def get_combination(rotations):
    result = 0
    dial = 50
    for line in rotations:
        if line[0] == 'R':
            dial = (dial + int(line[1:])) % 100
        else:
            dial = (dial - int(line[1:])) % 100
        
        if dial == 0:
            result += 1
            
    return result

def main():
    # Open and read input file
    input_path = "inputs/01.txt"
    with open(input_path, 'r') as f:
        input = f.readlines()

    # Calculate result
    result = get_combination(input)
    print(f'Combination is {result}')

if __name__ == "__main__":
    main()