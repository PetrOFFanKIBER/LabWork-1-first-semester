#def describe_person(name, age=30):
    #age = input('Введите свой возраст: ')
    #if len(list(age)) == 0 or len(list(age)) > 2:
        #age = 30
    #print('Имя: ',name)
    #print('Возраст: ',age)

name = input('Vvedite imya')
age = int(input())
    
def describe_person(name, age=30):
    return f'Мое имя {name} мне {age} лет'


print(describe_person(name))