class student:
    def __init__(self,name,age,id):
        if type(name)!=str:
            raise TypeError("Name must be string")
        if type(age) != int:
            raise TypeError("Age must be an integer")
        if type(id) != int:
            raise TypeError("ID must be an integer")
        if age < 0:
            raise ValueError("Age must be positive")
        if id < 0:
            raise ValueError("ID must be positive")

        self.name = name
        self.age = age
        self.id = id

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def age(self):
            return self._age
        
s1=student("marwan","14",60095071)
#to check if the methods works
print(s1.name)
print(s1.age) 

