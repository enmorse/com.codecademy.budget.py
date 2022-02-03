# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill,
                internet_bill, cell_bill, rent):
    bills = food_bill + electricity_bill + internet_bill + \
          cell_bill + rent
    return True if budget < bills else False


# Uncomment these function calls to test your over_budget function:
print(over_budget(110, 20, 30, 10, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 10, 30))
# should print True
