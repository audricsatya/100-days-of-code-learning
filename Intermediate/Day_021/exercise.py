class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("I am breathing")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    # def breathe(self):
        # super().breathe()
        # print("I am breathing underwater")

nemo = Fish()
nemo.breathe()