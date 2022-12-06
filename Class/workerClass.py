# my head is full of C language. 
class Workers:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.gae = age
        self.email = name + surname + "@gmail.com"
        self.fullname = name + " " + surname

    def __str__(self):
        return self.fullname + " " + self.email

    def __len__(self):
        return self.gae

    def display(self):
        print(self.name, self.surname, self.gae, self.email, self.fullname)


class Manager(Workers):
    def __init__(self, name, surname, age, staff):
        super().__init__(name, surname, age)
        self.staff = staff

    def __str__(self):
        return self.fullname + " " + self.email + " " + str(self.staff)


class Developer(Workers):
    def __init__(self, name, surname, age, staff):
        super().__init__(name, surname, age)
        self.staff = staff

    def __str__(self):
        return self.fullname + " " + self.email + " " + str(self.staff)


class Designer(Workers):
    def __init__(self, name, surname, age, staff):
        super().__init__(name, surname, age)
        self.staff = staff

    def __str__(self):
        return self.fullname + " " + self.email + " " + str(self.staff)

    def __repr__(self):
        return self.fullname + " " + self.email + " " + str(self.staff)


# display on screen

manager = Manager("John", "Smith", 30, 10)
developer = Developer("Jane", "Doe", 25, 5)
designer = Designer("Jack", "Black", 28, 7)
workers = [manager, developer, designer]

for worker in workers:
    worker.display()

