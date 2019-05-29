#coding:utf-8
import math
'''
    Class: Employee


'''

class Employee:

    def __init__(self):
        self.name = "blank_name"
        self.age = 18
        self.ability = 1

        self.__base_salary = 3000
        self.__base_required_work = 100

    def set_name(self, name_val):
        self.name = name_val

    def get_name(self):
        return self.name

    def set_age(self, age_val):
        self.age = age_val

    def get_age(self):
        return self.age

    def set_ability(self, ability_val):
        self.ability = ability_val

    def get_ability(self):
        return self.ability

    def get_required_work(self):
        return self.__base_required_work * math.pow(1.1, self.ability - 1)

    def get_salary(self):
        return self.__base_salary * math.pow(1.2, self.ability - 1)

    def work(self):
        print("Employee %s doing his work, %f \n" % (self.name, self.get_required_work()))
        return self.get_required_work()
