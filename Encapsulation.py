class Patient:
    def __init__(self, id, name, ssn):
        self.__id = id
        self.__name = name
        self.__ssn = ssn

    @property
    def getId(self):
        return self.__id

    @property
    def getName(self):
        return self.__name

    @property
    def getSSN(self):
        return self.__ssn
    
patient = Patient(1, 'Test Patient', '#test123')

id = patient.getId
print(id)

name = patient.getName
print(name)

ssn = patient.getSSN
print(ssn)