# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

hours, salary_per_hour, award = argv[1:]
hours, salary_per_hour, award = float(hours), float(salary_per_hour), float(award)
print(f"При ставке в час {salary_per_hour} и выработке {hours} часов, если премия = {award}, "
      f"зарплата составит {(hours * salary_per_hour) + award}")
