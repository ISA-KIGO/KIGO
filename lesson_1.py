""" Абстракция """

class Vehicle:
    def start_engine(self):
        pass
    
    def stop_engine(self):
        pass

    def drive(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Двигатель автомобиля зааведен"

    def stop_engine(self):
        return "Двигатель автомобиля не заведен"

    def drive(self):
        return "Автомобиль едет"
    
#     $ git config --global user.name "John Doe"
# $ git config --global user.email johndoe@example.com
# ISA-KIGO
# dagors030@gmail.com
#     $ git config --global user.name "ISA-KIGO"
# $ git config --global user.email dagors030@gmail.com