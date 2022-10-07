import numpy
import taxcode

taxable_income = numpy.random.uniform(5e3, 3e5, int(11e6))
# taxable_income = numpy.random.uniform(2e1, 2e1, int(11e6))

total_tax = 0
for income in taxable_income:
    # print(income)
    # total_tax += income
    total_tax += taxcode.tax_table(income)

print("total_tax:{:.2f} ".format(total_tax))
