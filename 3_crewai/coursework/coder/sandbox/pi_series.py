from decimal import Decimal, getcontext


def main():
    terms = 1_000_000
    getcontext().prec = 30

    total = Decimal(0)
    sign = 1

    for i in range(terms):
        denom = 2 * i + 1
        term = Decimal(sign) / Decimal(denom)
        total += term
        sign *= -1

    result = total * 4
    print(result)


if __name__ == '__main__':
    main()
