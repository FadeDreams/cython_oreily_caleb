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


cpdef double tot(double[:] taxable_income):
    cdef double total_tax = 0
    cdef int i, n
    n = taxable_income.shape[0]
    for i in range(n):
        # print(income)
        # total_tax += income
        total_tax += tax_table(taxable_income[i])
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
