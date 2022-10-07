import numpy
# import taxcode
from taxcode import tot

taxable_income = numpy.random.uniform(5e3, 3e5, int(11e6))
# taxable_income = numpy.random.uniform(2e1, 2e1, int(11e6))

total_tax = tot(taxable_income)
print("total_tax:{:.2f} ".format(total_tax))
