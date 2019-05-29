#coding:utf-8
import math
import random
from employee import Employee
from enterprise import Enterprise
from boss import Boss

'''
私企运营:初始资金fund为100w,初始工作量workload为300
    Employee,包含姓名name、年龄age、 能力ability、 工资salary等
    ●能力: 1~10级， 第一-级可以完成的工作量为100,所需I资为3k,以后每级可完成的工作量为前一级的1. 1倍，所需工资为前一-级的1.2倍●主要职责:完成自己的工作work)

    老板Boss: 无工资收入
    ●招募employ0、开除expel()员工: 员工能力在1~10范围内随机，-年内不能开除
    ●运营operate(、管理manage()公司: 5w/年，1k* 1.5*/year (n为员工数)

    公司
    ●每100工作量对应5k收入，每年工作量上涨10%
    ●每年至少完成80%工作量，未完成工作量自动累积至下一-年
➢输出每年开销(工资、管理费等)，直到当公司净收入为200w或破产




'''

if __name__ == '__main__':
    print("Hello Word")
    boss = Boss()
    boss.set_name("Shubin GUO")

    company = Enterprise()

    # 公司盈利超过200W或亏损停止运营
    while company.get_found() > 0 and company.get_found() <= 2000000:
        boss.operate(company)
