memo = {}

def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        key = (x, n)

        if (x, n) in memo:
            return memo[key]

        if n < 0:
            return 1/myPow(x, n * -1)

        if n == 0:
            memo[(x, 0)] = 1
            return 1

        if n % 2 != 0:
            x_n = x * myPow(x, n-1)
        else:
            x_n_minus_one = myPow(x, n/2)
            x_n = x_n_minus_one * x_n_minus_one
        
        memo[(x, n)] = x_n
        return x_n

# print myPow(2, 1)
# print myPow(2, -1)
# print myPow(2, 2)
print myPow(2.00000, -10)
# print myPow(2.10000, 3)
# print myPow(2.00000, -2)
# print myPow(1.00001, 123456)