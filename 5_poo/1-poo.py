class Person: # Class se inicia con mayuscula
    def __init__(self, name, age): # Constructor
        self.name = name # self se utiliza para referirse a la instancia de la clase
        self.age = age
    
    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old') # la f es para que se pueda interpolar, interpolar es poner variables dentro de un string
        
        
person1 = Person('John', 36) # Instanciar la clase
person2 = Person('Jane', 25)

person1.greet()
person2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self, amount):
        if self.is_active: # 
            self.balance += amount
            print(f'${amount} se ha depositado. Nuevo balance: ${self.balance}')
        else:
            print('Cuenta inactiva')
    
    def withdraw(self, amount): # se llama a self para referirse a la instancia de la clase
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f'${amount} se ha retirado. Nuevo balance: ${self.balance}')
            else:
                print('Fondos insuficientes')
        else:
            print('Cuenta inactiva')
            
    def desactivate_account(self):
        self.is_active = False
        print('Cuenta desactivada')
        
    def activate_account(self):
        self.is_active = True
        print('Cuenta activada')
        
cuenta1 = BankAccount('John', 1000)
cuenta2 = BankAccount('Jane', 500)

# llamada a los metodos

cuenta1.deposit(500)
cuenta2.deposit(100)

cuenta1.desactivate_account()
cuenta1.deposit(200)
cuenta1.activate_account()
cuenta1.deposit(200)

cuenta1.withdraw(2500)