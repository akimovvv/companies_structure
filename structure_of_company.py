

class Structure_of_company:

	def __init__(self, name, manager):
		self.__name = name
		self.__manager = manager

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
	def manager(self):
		return self.__manager

	@manager.setter
	def manager(self):
		if len(manager) >= 4:
			self.__manager = manager
		else:
			print("Error !")

	def show(self):
		print("Имя дирекции -", self.name, "Имя директора -"+"\n", self.manager)


class direction(Structure_of_company):

	def __init__(self, name, manager, company_name):
		Structure_of_company.__init__(self, name, manager)
		self.__company_name = company_name

	@property
	def company_name(self):
		return self.__company_name

	def show(self):
		print("Имя дирекции -", self.name, "\n"+"Имя директора -", self.manager, "\n"+"Имя компании -", self.company_name)

class department(Structure_of_company):

	def __init__(self, name, manager, department_name):
		Structure_of_company.__init__(self, name, manager)
		self.__department_name = department_name

	@property
	def department_name(self):
		return self.__department_name

	def show(self):
		print("Имя департамента -", self.name, "\n"+"Имя директора -", self.manager, "\n"+"Имя дирекции -", self.department_name)

class unit(Structure_of_company):

	def __init__(self, name, manager, unit_name):
		Structure_of_company.__init__(self, name, manager)
		self.__unit_name = unit_name

	@property
	def unit_name(self):
		return self.__unit_name

	def show(self):
		print("Имя отдела -", self.name, "\n"+"Имя директора -", self.manager, "\n"+"Имя департамента -", self.unit_name)

direction = direction("It", "Акимов Артур Русланович","MegaCom")
department = department("ДРИТ", "Маметиса у. Намыс", direction.name)
unit1 = unit("Отдел разработок", "Эрнст у. Мирлан", department.name)
unit2 = unit("Колл - Центр", "Сабралиев Бауржан", "К-Ц")
