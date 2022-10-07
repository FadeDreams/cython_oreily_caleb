# cython: profile=True
# cpdef double means return type of the function should be double
cpdef double tax_table(double amount):
    if amount <= 18000:
        return 11
    elif amount <= 40000:
        return .2*amount
    elif amount <= 80000:
        return .5*amount
    return 0

# def tax_table(amount):
#     if amount <= 18000:
#         return 11
#     elif amount <= 40000:
#         return .2*amount
#     elif amount <= 80000:
#         return .5*amount
#     return 0
#
