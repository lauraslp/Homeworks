# Class Employee sukuria objektą pagal atributus name ir employee_list.
import json
from tabulate import tabulate

class Employee:

    def __init__(self, name, employee_list):
        self.name = name
        self.employee_list = employee_list

    # find_person - metodas, kuris pagal sukutą objektą grąžina visą informaciją apie jį.
    # Iš list of dict grąžinamas vienas dict pagal key=name
    def find_person(self): # šiai funkcijai galima parašyti dekoratorių, kuris jei funkcijos reikšmė None grąžina pranešimą, kitų atveju gražina reikšmę
        for person in self.employee_list:
            if person['name'] == self.name:
                return person

    # add_person - metodas, kuris iš nurodyto failo įrašo asmenį į pirminį asmenų sąrašą (primary_list)
    def add_person(self, primary_list): #primary_list - a list to which a new employee will be added
        if self.find_person():
            person = self.find_person()
            primary_list.append(person)
            print(f'{self.name} has been added to the list.')
        else:
            print(f'Error during adding person: there is no such person {self.name} in a list.')
        return

    # remove_person - metodas, kuris pašalina asmenį iš nurodyto sąrašo
    def remove_person(self):
        if self.find_person():
            person = self.find_person()
            self.employee_list.remove(person)
            print(f'{self.name} has been removed from the list.')
        else:
            print(f'Error during removing person: there is no such person {self.name} in a list.')
        return

    # update_salary - metodas, kuris atnaujina asmens salary pagal nurodytą parametrą salary
    def update_salary(self, salary):
        if self.find_person():
            person = self.find_person()
            person.update({'salary': salary})
            print(f'Salary was updated for {self.name}: {salary}')
        else:
            print(f'Error during updating salary: there is no such person {self.name} in the list')
        return

    # add_child - metodas, kuris į asmens vaikų sąrašą prideda vaiką su nurodytu vardu child_name ir perskaičiuoja asmens vaikų skaičių no_child
    def add_child(self, child_name):
        if self.find_person():
            person = self.find_person()
            child_list = person['children_names']
            no_child = len(child_list)
            child_list.append(child_name)
            person.update({'no_children': no_child + 1,'children_names': child_list})
            print(f'A child {child_name} has been added to {self.name} children list.')
        else:
            print(f'Error during adding a child: there is no such person {self.name} in the list.')
        return

    # remove_child - metodas, kuris iš asmens vaikų sąrašo pašalina vaiką su nurodytu vardu child_name ir perskaičiuoja asmens vaikų skaičių no_child
    def remove_child(self, child_name):
        if self.find_person():
            person = self.find_person()
            child_list = person['children_names']
            no_child = len(child_list)
            try:
                child_list.remove(child_name)
                person.update({'no_children': no_child - 1, 'children_names': child_list})
                print(f'A child {child_name} has been removed from {self.name} children list.')
            except ValueError:
                print(f'Error during removing a child: {self.name} does not have child named {child_name}.')
        else:
            print(f'Error during removing a child: there is no such person {self.name} in the list.')
        return

# atidaromi du json failai. employee.json - pirminis sąrašas (primary list). new_employee.json - naujų (pridedamų) asmenų sąrašas.
with open('employees.json', 'r') as employees_file, open('new_employees.json', 'r') as new_employees_file:
    employees_file_data = json.load(employees_file)
    new_employees_file_data = json.load(new_employees_file)
    print(employees_file_data)
    employee = Employee('Greta', employees_file_data)
    new_employee = Employee('Ona', new_employees_file_data)
    # print(employee.find_person()) #None. Padaryti, kad grąžintų ne None, bet pranešimą, kad tokio asmens neranda.
    # print(new_employee.find_person())
    employee.add_child('Marta')
    new_employee.add_person(employees_file_data)
    # new_employee.remove_child('Marta')
    # employee.remove_person()
    # employee.update_salary(1000)

with open('updated_employees.json', 'r+') as updated_file:
    json.dump(employees_file_data, updated_file, indent=2)
    updated_file.seek(0) #grįžta į failo pradžią
    updated_json_object = json.load(updated_file)

    print(tabulate(updated_json_object, headers='keys', tablefmt='github'))






