class Employee:
	def work(self):
		print("Employee is working")
	
class Manager(Employee):
	def work(self):
		print("Manager is managing")

class Developer(Employee):
	def work(self):
		print("Developer is developing")

def work(employee: Employee):
	employee.work()

work(Manager())
work(Developer())