money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0 # 1-ый месяц
while True:
    i = spend - salary
    if i > money_capital:
        break

    money_capital -= i
    spend *=increase + 1
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
