gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
greatest_common_divisor = lambda *args: reduce(gcd, args)
