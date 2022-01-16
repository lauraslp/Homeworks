# ... write a script that would read the file and allow 2 operations: add_child(name), remove_child(name).
# ... Assume that all child names are known al the time (no_children == len(children_names) - keep them synchronized)
# ... Additional features (implement if you want): change salary, increase salary by some percentage, add employees, etc.
import json

# Function to find a person. Find dict in a dict list, by dict key value.
def find_person(key, name, list_of_dictionaries):
    for person in list_of_dictionaries:
      if person[key] == name:
        return person

# Function to add a person by name. Append list of dictionaries
def add_person(name, list_of_dictionaries):
  with open('new_employees.json') as new_person:
    new_data = json.load(new_person)
    if find_person('name', name, new_data):
        person = find_person('name', name, new_data)
        list_of_dictionaries.append(person)
        print(f'{name} has been added to the list.')
    else:
        print(f'Error during adding person: there is no such person {name} in a list.')
    return

# Function to remove a person by name. Append list of dictionaries
def remove_person(name, list_of_dictionaries):
    person = find_person('name', name, list_of_dictionaries)
    try:
        list_of_dictionaries.remove(person)
        print(f'{name} has been removed from the list.')
    except ValueError:
        print(f'Error during removing person: there is no such person {name} in a list.')
    return

# Function to update a person's salary by name.
# Find a dictionary in a list by person's name and update it by key 'salary'
def update_salary(name, updated_salary, list_of_dictionaries):
    person = find_person('name', name, list_of_dictionaries)
    try:
        person.update({'salary': updated_salary})
        print(f'Salary was updated for {name}: {updated_salary}')
    except ValueError:
        print(f'Error during updating salary: there is no such person {name} in a list')
    return

# Function to add person's children.
# Find a dict in a list by person's name and update it by keys 'no_children' and 'children_names'
def add_child(name, child_name, list_of_dictionaries):
    if find_person('name', name, list_of_dictionaries):
        person = find_person('name', name, list_of_dictionaries)
        children_list = person['children_names']
        no_children = len(children_list)
        children_list.append(child_name)
        person.update({'no_children':no_children + 1, 'children_names': children_list})
        print(f'A child named {child_name} has been added to {name} children list.')
    else:
        print(f'Error during adding a child: there is no such person {name} in a list.')
    return

# Function to remove person's children.
def remove_child(name, child_name, list_of_dictionaries):
    if find_person('name', name, list_of_dictionaries):
        person = find_person('name', name, list_of_dictionaries)
        try:
            children_list = person['children_names']
            no_children = len(children_list)
            children_list.remove(child_name)
            person.update({'no_children': no_children - 1, 'children_names': children_list})
            print(f'A child named {child_name} has been removed from {name} children list.')
        except ValueError:
            print(f'Error during removing a child: {name} does not have child named {child_name}.')
    else:
        print(f'Error during removing a child: there is no such person {name} in a list.')
    return

with open('employees.json') as my_file:
    data = json.load(my_file)
    add_person('Ona', data)
    remove_person('Jonas', data)
    update_salary('Petras', 1000, data)
    remove_child('Greta', 'Tomas', data)
    add_child('Petras', 'Tomas', data)

with open('employees.json', 'w') as updated_file:
    json.dump(data, updated_file, indent = 2)



