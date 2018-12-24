def generate_parens(n):
    if n <= 0:
        return []

    def generate_parens_helper(opened, closed):
        # base case: we must end with a close paren
        if opened == n and closed == opened - 1:
            return [')']

        res = []
        if opened < n:
            tails = generate_parens_helper(opened + 1, closed)
            res += ['(' + tail for tail in tails]

        if closed < opened:
            tails = generate_parens_helper(opened, closed + 1)
            res += [')' + tail for tail in tails]

        return res

    return generate_parens_helper(0, 0)