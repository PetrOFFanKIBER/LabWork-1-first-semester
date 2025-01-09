class UserAccount:
    def __init__(self, username, email, password):
        self.username =  username
        self.email =  email
        self.password = password
        
    def set_password(self, new_password):
        self.password = new_password
        return print('Пароль успешно изменён')
        
    def check_password(self, password):
        if self.password == password:
            return True
        else: 
            return False
        
    
    
    
UserAccount = UserAccount('Triton', 'sea@mail.ru', '12345')
EXIT = UserAccount.check_password(input('Введите пароль: '))
if EXIT == True:
    UserAccount.set_password(input('Введите новый пароль: '))
    print(UserAccount.check_password(input('Повторите пароль: ')))
else:
    print('Пароль не верен')
    