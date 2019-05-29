#coding:utf-8
from boss import Boss

'''
    Class: Enterprise
'''

class Enterprise:

    def __init__(self):
        self.__employee_list = []
        self.__boss = Boss()
        self.__found = 1000000
        self.__workload = 300

    def get_employee_list(self):
        return self.__employee_list

    def get_found(self):
        return self.__found

    def set_found(self, found_val):
        self.__found = float(found_val)

    def get_workload(self):
        return self.__workload

    def set_workload(self, workload_val):
        self.__workload = int(workload_val)

