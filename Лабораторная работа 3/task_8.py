money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while spend - salary <= money_capital:
    month += 1
    money_capital -= spend - salary
    spend *= 1 + increase

print(month)
