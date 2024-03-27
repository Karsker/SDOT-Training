def generate_parenthesis(n):
    result = []

    def generate_parenthesis_helper(open_count, close_count, current):
        nonlocal result
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            generate_parenthesis_helper(open_count + 1, close_count, current + "(")
        if close_count < open_count:
            generate_parenthesis_helper(open_count, close_count + 1, current + ")")

    generate_parenthesis_helper(0, 0, "")
    return result

# Get input from the user
n = int(input("Enter the value of n: "))
combinations = generate_parenthesis(n)
print(f"Combinations of well-formed parentheses for n = {n}:")
for combination in combinations:
    print(combination)
