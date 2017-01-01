from fractions import Fraction
def divide_pie(groups):
    pie = Fraction(1)
    count_groups = reduce(lambda x, y: abs(x) + abs(y), groups)
    for i in groups:
        if i > 0:
            pie -= Fraction(i, count_groups)
        else:
            pie -= Fraction(abs(i), count_groups) * pie
    return (pie.numerator, pie.denominator)
