

class Employee:

	def __init__(self, name, salary, position, working_unit):
		self.__name = name
		self.__salary = salary
		self.__position = position
		self.__working_unit = working_unit


	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self):
		if len(name) >= 4:
			self.__name = name
		else:
			print("Error !")


	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self):
		if salary > 0:
			self.__salary = salary
		else:
			print("Error !")


	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self):
		if len(position) > 0:
			self.__position = position
		else:
			print("Error !")


	@property
	def working_unit(self):
		return self.__working_unit

	@working_unit.setter
	def working_unit(self):
		if len(working_unit) > 0:
			self.__working_unit = working_unit
		else:
			print("Error !")

	def show(self):
		print("ФИО сотрудника -", self.name, "\n"+"Зарплата -", self.salary, "\n"+"Должность -", self.position, "\n"+"Отдел -", self.working_unit)

employee1 =Employee("Акимов Артур Русланович", 231000, "Директор", "It")
employee2 =Employee("Маметиса у. Намыс", 180000, "Директор", "ДРИТ")
employee3 =Employee("Эрнст у. Мирлан", 165000, "Директор", "Отдел разработок")
employee4 =Employee("Сабралиев Бауржан", 231000, "Директор", "К-Ц")
employee5 =Employee("Нурлан у. Илимбек", 140000, "Програмист", "Отдел разработок")
employee6 =Employee("Турусбеков Улукман", 55300, "Специалист Колл-Центра", "К-Ц")
