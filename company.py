

class Company:
	def __init__(self, name, address):
		self.__name = name
		self.__address = address

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
	def address(self):
		return self.__address

	@address.setter
	def address(self):
		if len(address) >= 4:
			self.__address = address
		else:
			print("Error !")

	def show(self):
		print("Название компании -", self.name, "\n"+"Адрес компании -", self.address)