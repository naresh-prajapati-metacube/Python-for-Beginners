from abc import ABC, abstractmethod

class TouchScreenLaptop(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def scroll(self):
        pass


class hp(TouchScreenLaptop):
    def scroll():
        return 'hp laptop scrolled'
    
    @abstractmethod
    def click(self):
        return super().click()
    

class dell(TouchScreenLaptop):
    def scroll():
        return 'dell laptop scrolled'
    
    @abstractmethod
    def click(self):
        return super().click()
    
class hpnotebook(hp):
    def click():
        return 'hpnotebook clicked'
    

class dellnotebook(dell):
    def click():
        return 'dellnotebook clicked'
    
print(hp.scroll())
print(dell.scroll())
print(hpnotebook.click())
print(dellnotebook.click())