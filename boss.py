#coding:utf-8
import random

import math

from employee import Employee




'''
    Class: Boss
    Description: something
'''
class Boss:

    def __init__(self):
        self.name = 'Boss_blank'

    def set_name(self, name_val):
        self.name = name_val

    def get_name(self):
        return self.name

    '''
    ●招募employ0、开除expel()员工: 员工能力在1~10范围内随机，-年内不能开除
    '''
    def employ(self, company):
        employee = Employee()
        employee.set_ability(random.randint(1, 10))
        employee.set_name("ee " + str(random.randint(1024, 100086)))

        company.get_employee_list().append(employee)

    def expel(self, company):
        list(company.__employee_list).pop()


    '''
    ●运营operate(、管理manage()公司: 5w/年，1k* 1.5*/year (n为员工数)
    '''
    def operate(self, company):
        '''
        :param company: type -> Enterprise
        :return: company instance
        '''

        print("开工啦，企业剩余资金%f, 雇佣员工%d人, 工作量剩余%d \n"
              % (company.get_found(), len(company.get_employee_list()), company.get_workload()))
        # 招募员工
        self.employ(company)
        # 开除员工
        # (company)
        #计算员工工作利润
        employee_list = company.get_employee_list()

        # 工作量
        works_sum = 0
        #工资支出
        fee_sum = 0
        for employee in employee_list:
            works_sum += employee.get_required_work()
            fee_sum += employee.get_salary()


        #计算管理费

        fee_sum += self.manage(company)

        #修改公司资金
        # 1 计算利润 100 工作量=> 5000收入
        profit = works_sum * 50
        company.set_found( company.get_found() + profit )

        # 2 计算支出
        # 不进行非正数校验 ==> 负债也不能拖欠农民工工资呀
        company.set_found(company.get_found() - fee_sum)

        '''
        公司
        ●每100工作量对应5k收入，每年工作量上涨10%
        ●每年至少完成80%工作量，未完成工作量自动累积至下一-年
        #更新企业工作量

        '''
        workloads_remain = company.get_workload() * 0.8 - works_sum

        if workloads_remain > 0:
            company.set_workload(company.get_workload() * 1.1 + workloads_remain)
        else:
            pass

        print("年终啦，企业剩余资金%f, 雇佣员工%d人, 工作量剩余%d \n"
              %(company.get_found(), len(company.get_employee_list()), company.get_workload()))



    # 返回管理费
    '''
    ●运营operate(、管理manage()公司: 5w/年，1k* 1.5*/year (n为员工数)
    '''
    def manage(self, company):
        return 50000 + 1000 * math.pow(1.5, len(list(company.get_employee_list())))
