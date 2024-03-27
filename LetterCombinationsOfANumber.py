def possible_words(s, ans):
    # Base Case
    if not s:
        print(ans)
        return

    # Get the mapping of the first digit
    key = keypad[int(s[0])]

    # Recursive Step
    for char in key:
        # Recursively call the function with the remaining digits and updated combination
        possible_words(s[1:], ans + char)

# Corrected initialization of keypad
keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# Input handling
s = input("Enter a string of digits: ")

# Call the function to print possible letter combinations
print("Possible letter combinations:")
possible_words(s, "")
