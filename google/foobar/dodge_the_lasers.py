import decimal
from decimal import Decimal


def solution(s):
    n = int(s)
    decimal.getcontext().prec = 1000
    beta = Decimal(2) ** Decimal(0.5) - Decimal(1)

    def helper(n):
        if n == 0:
            return 0
        nprime = int(beta * n)

        return int((n * nprime) + (n * (n + 1) / 2) - (nprime * (nprime + 1) / 2) - helper(nprime))

    return str(helper(n))


print(solution(str(10**100)))


print(solution('77'))
print(solution('77'))
print(solution('5'))
