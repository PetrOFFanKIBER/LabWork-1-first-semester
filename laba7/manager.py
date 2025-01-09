class Employe:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def get_info(self):
        return "Имя: {} ,ID: {}".format(self.name, self.ID)
    
class Manager (Employe):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.department = department
    def manage_project(self):
        return 
    
class Technician:
    def __init__(self, specialization):
        self.specialization = specialization
    def perform_maintenance(self):
        return

class TechManager (Technician, Manager):
    def __init__(self, name, ID, department, specialization):
        Technician.__init__(self, specialization)
        Manager.__init__(self, name, ID, department)
    def perform_maintenance(self):
        return 
    def manage_project(self):
        return    
    def add_employee(self):
        Employelist.append(self.name)
        IDiist.append(self.ID)
        departmentlist.append(self.department)
        empspecial.append(self.specialization)
        return 'Сотрудник добавлен'
    def get_team_info(self):
        print('Список сотрудников: ')
        for i in range(len(Employelist)):
            print(f"Имя: {Employelist[i]} ,ID: {IDiist[i]}, Отдел: {departmentlist[i]}, Специализация: { empspecial[i]}")


Employelist = ['Boris', 'Vasiliy']
IDiist= [485632, 856951]
departmentlist = ['IT', 'service']
empspecial = ['programmer', 'loader']

Employer = Employe(Employelist[0], IDiist[0])
print(Employer.get_info())

human = input('Введите имя сотрудника: ')
namber = input('Введите ID сотрудника: ')
dep = input('Введите отдел сотрудника: ')
special = input('Введите специализацию сотрудника: ')
techMan = TechManager(human, namber, dep, special)
print(techMan.add_employee())

techMan.get_team_info()