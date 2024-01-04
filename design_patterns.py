#!/usr/bin/python

from abc import ABCMeta, abstractmethod

# 这是第一版的写法
#if __name__ == "__main__":
#    str_num1 = input("please enter the first number: ")
#    str_operpate = input("please enter operpattion + - * / ")
#    str_num2 = input("please enter second number: ")
#
#    res = ""
#    
#    if str_operpate == "+":
#        res = int(str_num1) + int(str_num2)
#    if str_operpate == "-":
#        res = int(str_num1) - int(str_num2)
#    if str_operpate == "*":
#        res = int(str_num1) * int(str_num2)
#    if str_operpate == "/":
#        res = int(str_num1) / int(str_num2)
#
#    print(res)


# 第二版的写法

#def result():
#    try:
#        if str_operpate == "+":
#            return int(str_num1) + int(str_num2)
#        if str_operpate == "-":
#            return int(str_num1) - int(str_num2)
#        if str_operpate == "*":
#            return int(str_num1) * int(str_num2)
#        if str_operpate == "/":
#            return int(str_num1) / int(str_num2)
#    except Exception as e:
#        print(str(e))
#
#
#
#if __name__ == "__main__":
#    str_num1 = input("please enter the first number: ")
#    str_operpate = input("please enter operpattion + - * / ")
#    str_num2 = input("please enter second number: ")
#
#    res = result()
#    print(res)




# 第三版写法

#class Operation:
#    def __init__(self, str_num1, str_operpate, str_num2):
#        self.str_num1 = str_num1
#        self.str_operpate = str_operpate
#        self.str_num2 = str_num2
#
#    def get_result(self):
#        try:
#            if self.str_operpate == "+":
#                return int(self.str_num1) + int(self.str_num2)
#            if self.str_operpate == "-":
#                return int(self.str_num1) - int(self.str_num2)
#            if self.str_operpate == "*":
#                return int(self.str_num1) * int(self.str_num2)
#            if self.str_operpate == "/":
#                return int(self.str_num1) / int(self.str_num2)
#        except Exception as e:
#            print(str(e))
#
#
#
#
#
#if __name__ == "__main__":
#    str_num1 = input("please enter the first number: ")
#    str_operpate = input("please enter operpattion + - * / ")
#    str_num2 = input("please enter second number: ")
#
#    result = Operation(str_num1, str_operpate, str_num2)
#    res = result.get_result()
#    print(res)





# 第四版，写法，解耦

# 抽象类
class Operation(metaclass=ABCMeta):
    str_num1 = ""
    str_num2 = ""
    @abstractmethod
    def get_result(self):
        pass

class OperationAdd(Operation):
    def get_result(self):
        return int(str_num1) + int(str_num2)

class OperationSub(Operation):
    def get_result(self):
        return int(str_num1) - int(str_num2)

class OperationMul(Operation):
    def get_result(self):
        return int(str_num1) * int(str_num2)

class OperationDiv(Operation):
    def get_result(self):
        return int(str_num1) / int(str_num2)

class Factory:
    def __init__(self, oper):
        self.oper=oper

    def create_operate(self):
        if self.oper == "+":
            return OperationAdd()
        if self.oper == "-":
            return OperationSub()
        if self.oper == "*":
            return OperationMul()
        if self.oper == "/":
            return OperationDiv()


if __name__ == "__main__":
    try:
        str_num1 = input("please enter the first number: ")
        str_operpate = input("please enter operpation + - * / :")
        str_num2 = input("please enter second number: ")

        Operation.str_num1 = str_num1
        Operation.str_num2 = str_num2

        obj = Factory(str_operpate).create_operate()
        result = obj.get_result()

        print(result)
    except Exception as e:
        print(str(e))
