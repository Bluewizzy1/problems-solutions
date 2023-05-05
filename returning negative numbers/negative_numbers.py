

def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

# print(make_negative(1))
# print(make_negative(-5))
# print(make_negative(23455))
# print(make_negative(937947))
# print(make_negative(5789))
# print(make_negative(0))




# def negative_num( number ):
#     return -number if number>0 else number

# print(negative_num(60))
# print(negative_num(-7860))
# print(negative_num(0))
# print(negative_num(-9))


def make_negated( number ):
    negated = -abs(number)
    return negated

print(make_negated(77))
print(make_negated(-54))
print(make_negated(0))
print(make_negated(+-8))