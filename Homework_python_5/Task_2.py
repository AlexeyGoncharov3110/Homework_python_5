# Задача_2
# # Напишите однострочный генератор словаря,
# # который принимает на вход три списка одинаковой длины:
# # имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# # В результате получаем словарь с именем в качестве ключа и 
# # суммой премии в качестве значения. 
# # Сумма рассчитывается как ставка умноженная на процент премии

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Alex", "Ivan", "Sergey"]
salaries = [150000, 95000, 100000]
bonuses = ["10%", "15%", "20%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)

