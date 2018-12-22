
def convert( s, num_rows):
    row = 0
    direction = -1
    rows = ['']  * num_rows
    for i in range(len(s)):
        rows[row] += s[i]
        if i % (num_rows - 1) == 0:
            direction = direction * -1
        row += direction
    return reduce(lambda row1, row2: row1 + row2, rows)

print(convert("PAYPALISHIRING", 3))