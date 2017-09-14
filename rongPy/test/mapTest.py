income = [10, 30, 75]

def double_money(dollar):
    return dollar * 2

new_income = list(map(double_money, income))
print(new_income)