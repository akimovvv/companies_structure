from structure_of_company import Structure_of_company, direction, department, unit1, unit2

class Position:
	def __init__(self, name):
		self.__name = name


	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self):
		if len(name) >= 4:
			self.__name = name
		else:
			print("Error !")



class info_position(Position):

	def __init__(self, name, min_salary, max_salary, working_unit):
		Position.__init__(self, name)
		self.__min_salary = min_salary
		self.__max_salary = max_salary
		self.__working_unit = working_unit

	@property
	def min_salary(self):
		return self.__min_salary

	@min_salary.setter
	def min_salary(self):
		if min_salary > 0:
			self.__min_salary = min_salary
		else:
			print("Error !")


	@property
	def max_salary(self):
		return self.__max_salary

	@max_salary.setter
	def max_salary(self):
		if max_salary < 500000:
			self.__max_salary = max_salary
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
		print("Название должности -", self.name, "\n" + "Мин. зарплата -", self.min_salary, "\n" + "Макс. зарплата -", self.max_salary, "\n" + "Рабочий отдел -", self.working_unit)

position1 = info_position("Директор", 100000, 300000, direction.name)
position2 = info_position("Програмист", 100000, 222222, unit1.name)
position3= info_position("Специалист Колл-Центра", 30000, 100000, unit2.unit_name)