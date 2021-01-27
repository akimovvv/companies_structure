from company import Company
from structure_of_company import Structure_of_company, direction, department, unit1, unit2
from position import Position, position1, position2, position3
from employee import Employee, employee1, employee2, employee3, employee4, employee5, employee6


def main():

	main = Company("MegaCom", "г.Бишкек, ул.Абдрахманова 222")

	while True:

		action = input("Введите какую информацию вы хотите получить - \n"\
			"Название и адрес компании (1) \n"\
			"Структура компании (2) \n"\
			"Инфо о должностях (3) \n"\
			"Инфо о сотрудниках (4) \n"\
			"Выход (5) \n")




		if action == "1":
			main.show()




		elif action == "2":
			action = input("Введите какую информацию вы хотите получить\n"\
				"Дирекция (1) \n"\
				"Департамент (2) \n"
				"Отдел (3) \n")
			if action == "1":
				action = input("Введите отдел -\n"\
					"Отдел разработок (1) \n")
				if action == "1":
					direction.show()
				else:
					print("Error !")
			elif action == "2":
				action = input("Введите отдел -\n"\
					"Отдел разработок (1) \n")
				if action == "1":
					department.show()
				else:
					print("Error !")
			elif action == "3":
				action = input("Введите отдел -\n"\
					"Отдел разработок (1) \n"\
		 			"Колл - Центр (2) \n")
				if action == "1":
					unit1.show()
				elif action == "2":
					unit2.show()
				else:
					print("Error !")




		elif action == "3":
			action = input("Введите какую информацию вы хотите получить\n"\
				"Директор (1) \n"\
				"Програмист (2) \n"
				"Специалист Колл-Центра (3) \n")
			if action == "1":
				position1.show()
			elif action == "2":
				position2.show()
			elif action == "3":
				position3.show()
			else:
				print("Error !")




		elif action == "4":
			action = input("Введите какую информацию вы хотите получить\n"\
				"Директор (1) \n"\
				"Програмист (2) \n"
				"Специалист Колл-Центра (3) \n")
			if action == "1":
				name = input("Акимов Артур Русланович \n"\
					"Маметиса у. Намыс \n"\
					"Эрнст у. Мирлан \n"\
					"Сабралиев Бауржан \n"\
					"Введите ФИО сотрудника - \n")
				if name == "Акимов Артур Русланович":
					employee1.show()
				elif name == "Маметиса у. Намыс":
					employee2.show()
				elif name == "Эрнст у. Мирлан":
					employee3.show()
				elif name == "Сабралиев Бауржан":
					employee4.show()
				else:
					print("Введённое ФИО не верна или такого сотрудника не существует !")
			elif action == "2":
				name = input("Нурлан у. Илимбек \n"\
					"Введите ФИО сотрудника - \n")
				if name == "Нурлан у. Илимбек":
					employee5.show()
				else:
					print("Введённое ФИО не верна или такого сотрудника не существует !")
			elif action == "3":
				name = input("Турусбеков Улукман \n"\
					"Введите ФИО сотрудника - \n")
				if name == "Турусбеков Улукман":
					employee6.show()
				else:
					print("Введённое ФИО не верна или такого сотрудника не существует !")
			else:
				print("Error !")




		elif action == "5":
			break

main()