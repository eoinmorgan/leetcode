nums_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letter_combinations(digits):
    memo = {}

    if len(digits) == 0:
        return []

    if digits in memo:
        return memo[digits]

    cur_digit_letters = [letter for letter in nums_to_letters[digits[0]]]

    if len(digits) == 1:
        memo[digits] = cur_digit_letters
        return cur_digit_letters

    rest = letter_combinations(digits[1:])

    res = []
    for letter in cur_digit_letters:
        for tail in rest:
            res.append(letter + tail)

    memo[digits] = res
    return res

    

    