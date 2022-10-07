# cython: profile=True
# cpdef double means return type of the function should be double
def tax_table(amount):
    if amount <= 18000:
        return 11
    elif amount <= 40000:
        return .2*amount
    elif amount <= 80000:
        return .5*amount
    return 0


def tot(taxable_income):
    total_tax = 0
    for income in taxable_income:
        # print(income)
        # total_tax += income
        total_tax += tax_table(income)
    return total_tax

# def tax_table(amount):
#     if amount <= 18000:
#         return 11
#     elif amount <= 40000:
#         return .2*amount
#     elif amount <= 80000:
#         return .5*amount
#     return 0
#
