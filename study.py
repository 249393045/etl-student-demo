import random

"""基础"""
# print("请告诉我你的公司名：")
# name = input()
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# frowth_days = 7
# finally_stock_price = stock_price*stock_price_daily_growth_factor**frowth_days
# print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
# print("每日增长系数：%.1f,经过%d天的增长后，股价涨到了%.2f"%(stock_price_daily_growth_factor,frowth_days,finally_stock_price))

"""多重嵌套判断"""
# ff = int(input("""请选择你想吃的东西：
#     1.鸡腿
#     2.炒饭
#     3.面条
# 请选择编号："""))
# if ff == 1:
#      print("您是否确定选择鸡腿？(是or否)")
#      a = input()
#      if a == "是":
#          print("已下单鸡腿，请稍后。")
#      elif a == "否":
#          print("请重新选择。")
# elif ff == 2:
#     print("您是否确定选择炒饭？(是or否)")
#     a = input()
#     if a == "是":
#         print("已下单炒饭，请稍后。")
#     elif a == "否":
#         print("请重新选择。")
# else:
#     print("您是否确定选择面条？(是or否)")
#     a = input()
#     if a == "是":
#         print("已下单面条，请稍后。")
#     elif a == "否":
#         print("请重新选择。")

"""函数优化后"""
# def hanshu(food_name):
#     """函数确认是否下单商品"""
#     print(f"您是否确定选择{food_name}?(是or否)")
#     a = input()
#     if a == "是" :
#         print(f"已下单{food_name},请稍后。")
#     elif a == "否" :
#         print("请重新选择。")
#
# ff = int(input("""请选择您想吃的东西：
#     1.鸡腿
#     2.炒饭
#     3.面条
# 请选择编号："""))
# if ff == 1 :
#     hanshu("鸡腿")
# elif ff == 2 :
#     hanshu("炒饭")
# elif ff == 3 :
#     hanshu("面条")

"""多次判断"""
# num = random.randint(1,10)
# guess_number = int(input("请输入你猜测的数字:"))
# if guess_number == num:
#     print("恭喜，第一次就猜中了。")
# else:
#     if guess_number > num:
#         print("你猜的数字大了")
#     else:
#         print("你猜的数字小了")
#     guess_number = int(input("请再次输入你要猜的数字："))
#     if guess_number == num:
#         print("第二次猜对了")
#     else:
#         if guess_number > num:
#             print("你猜的数字大了")
#         else:
#             print("你猜的数字小了")
#         guess_number = int(input("请再次输入你要猜的数字："))
#         if guess_number == num:
#             print("第三次猜对了")
#         else:
#             print("三次都错了，你没机会了")

"""while循环"""
# sum = 0 ; i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

"""嵌套判断示例"""
# flag = True; i = 0
# num = random.randint(1,100)
# while flag:
#     guess_num = int(input("请输入你猜的数字："))
#     if guess_num == num:
#         print("恭喜你猜对了！")
#         flag = False
#         i = i + 1
#     elif guess_num > num :
#         print("你猜的大了")
#         i = i + 1
#     elif guess_num < num :
#         print("你猜的小了")
#         i = i + 1
# print(f"一共猜了{i}次")

"""while实现九九乘法表，循环嵌套"""
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t",end="")   #emd = ""代表输出不换行
#         j += 1
#     print()
#     i = i + 1

"""range函数"""
# range(num)
# for x in range(10):
#     print(x)

#range(num1,num2),从num1到num2 - 1
# for x in range(5,10):
#     print(x)

#range(num1,num2,step),从num1到num2 - 1,数字差step
# for x in range(5,10,2):
#     print(x)

# sum = 10000
# for x in range(1,21):
#     i = random.randint(1,10)
#     if i < 5:
#         print(f"员工{x},绩效{i},低于5，不发工资，下一位。")
#         continue
#     else:
#         if sum > 0:
#             sum -= 1000
#             print(f"向员工{x}发放工资1000元,账户余额还剩余{sum}")
#         else:
#             print("工资发完了，下个月领取吧。")
#             break

"""循环练习"""
# money = 5000000
# name = None
# name = input("请输入姓名：")
#
# def main_menu():
#     print("-----------主菜单-----------")
#     print(f"{name}，您好，欢迎使用ATM，请选择操作：")
#     print("""查询余额\t[输入1]
# 存款\t[输入2]
# 取款\t[输入3]
# 退出\t[输入4]""")
#     n = int(input("请输入您的选择："))
#     return n
#
# def deposit(m):
#     global money
#     print("-----------存款-----------")
#     money += m
#     print(f"{name}，您好，您存款{m}元成功")
#     check(False)
#
# def withdraw_money(m):
#     global money
#     print("-----------取款-----------")
#     money -= m
#     print(f"{name}，您好，您取款{m}元成功")
#     check(False)
#
# def check(show_header):
#     if show_header:
#         print("-----------查询余额-----------")
#     print(f"{name}，您好，您的余额剩余：{money}元")
#
# while True:
#     n = main_menu()
#     if n == 1:
#         check(True)
#         continue
#     elif n == 2:
#         m = int(input("你要存款金额的是："))
#         deposit(m)
#         continue
#     elif n == 3:
#         m = int(input("你要取款金额的是："))
#         withdraw_money(m)
#         continue
#     else:
#         print("感谢您的使用，再见。")
#         break

"""列表"""
# my_list = ["python",1232,"789"]     #列表从前数开头是0，从后数开头是-1
# my_list.insert(1,"学习")
# print(my_list)
# my_list.append([1,2,3])     #append在列表末尾加入新的元素，但是只加入1个
# print(my_list)
# my_list.extend([4,5,6])         #extend继承，可以将别的列表内容并入列表末尾
# print(my_list)
# del my_list[2]      #del仅仅只能删除元素
# print(my_list)
# n = my_list.pop(1)          #pop不仅能删除元素，还能将删除的元素提取出来
# print(n)
# print(my_list)
# list = [1,3,5,9,5,6,1,1,1]
# list.remove(5)      #remove删除匹配到的第一个符合的元素
# print(list)
# sum = list.count(1)     #统计列表中对应元素个数
# print(sum)
# m = len(list)       #统计列表内元素个数
# print(m)
# list.clear()        #清空列表
# print(list)
# list = [1,2,3]
# print(list*2)       #列表与数字相乘是复制


# t = tuple("hello", )        #元组定义单个元素时必须在后面加一个逗号，否则是str,元组可读不可修改，但是元组内的列表内容可以修改

"""字符串"""
# my_str = "itheima and itcast"
# new_my_str = my_str.replace("it","程序")      #replace是不会修改原有字符串的，字符串不可修改，只是得到了新的字符串
# print(new_my_str)

# str1 = "hello python itheima itcast"
# my_str_list = str1.split(" ")       #split将字符串按照分隔符切分为多个字符串存入列表
# print(my_str_list)

# my_str = "  itheima and itcast  "
# new_my_str = my_str.strip()     #不传入参数则为去除首位空格
# print(new_my_str)

# my_str = "12itheima and itcast21"
# new_my_str = my_str.strip("12")     #给入指定参数，则去除字符串前后的传入参数，传入12实际上为传入"1"和"2"2个小子串
# print(new_my_str)

# my_str = "itheima itcast boxuegu"
# num = my_str.count("it")
# print(f"{my_str}中it字符有{num}个")
# new_my_str = my_str.replace(" ","|")
# print(f"字符串{my_str}替换后为{new_my_str}")
# my_str_list = new_my_str.split("|")
# print(f"字符串{new_my_str}按照|切割后得到{my_str_list}")

"""数据容器读取"""
# my_list = [0,1,2,3,4,5,6,7,8,9]
# result1 = my_list[1:4]      #步长为1时可以省略
# print(f"结果1:{result1}")
# my_tuple = (0,1,2,3,4,5,6,7,8,9)
# result2 = my_tuple[1:]
# print(f"结果2：{result2}")
# my_str = "0123456789"
# result3 = my_str[::2]
# print(f"结果3:{result3}")
# result4 = my_str[::-1]      #等同于反转
# print(f"结果4:{result4}")

"""集合"""
# my_set = {"python","white","black","python","white","black"}        #集合内容不会重复，会自动去重，且集合内容为无序的用不了下标
# new_my_set = set()
# print(f"my_set的内容是:{my_set}，类型为：{type(my_set)}")
# print(f"new_my_set的内容是:{new_my_set}，类型为：{type(new_my_set)}")
# my_set.add("hello")
# my_set.add("python")
# print(f"my_set添加结果是:{my_set}")
# my_set.remove("hello")
# print(f"my_set移除结果是:{my_set}")
# set1 = my_set.pop()     #pop在集合中随机取出一个元素
# print(set1)

"""字典"""
# student = {"name":"张三","age":18,"gender":"男"}
# d = {}
# print(type(d))
# print(f"名字是：{student['name']}")     #注意：引号嵌套时要区分不能同类嵌套.这种取值如果key不存在，KeyError报错
# print(f"年龄是：{student.get('age')}")      #这样的key不存在返回None,不会崩溃,还可以设置默认值
# print(student.get("score", 0))      # 找不到score，返回默认值0

# teacher = {"name":"李四","age":20,"gender":"女"}
# teacher["score"] = 100     #字典的修改看key,key存在则修改对应value,不存在则新增键值对value
# teacher["age"] = 21
# print(teacher)
# teacher.update({"name":"王舞","age":18,"gender":"女"})     #批量删除/修改，没有提到的key不改变，提到的才变，注意要加上{}
# print(teacher)
# print(teacher.keys())       #拿到所有的key
# print(teacher.values())     #拿到所有的值
# print(teacher.items())      #拿到所有的键值对元组
# for k in teacher:       #遍历key输出字典内容
#     print(k,teacher[k])
# for k in teacher.keys():        #遍历key
#     print(k)
# for v in teacher.values():
#     print(v)
# for k,v in teacher.items():
#     print(f"键{k},值{v}")
# data = {i:i*2 for i in range(3)}        #字典推导式快速生成字典，特别注意字典中key是唯一的如果重复，后面的值会掩盖前面的值
# print(data)

# info = {"name":"小明","height":175,"weight":60}
# print(f"名字：{info.get('name')}")
# info["weight"] = 62
# info["age"] = 20
# del info["height"]
# for key,value in info.items():
#     print(f"{key}:{value}")

"""函数"""
# records = {}
# def shuru():
#     name =  input("请输入你的名字：(输入q退出)")
#     if name.lower() == "q":
#         return None,None
#     n = int(input("请输入猜的次数："))
#     return name,n
# while True:
#     name,n = shuru()
#     if n == None:
#         break
#     records[name] = n
# for k,v in records.items():
#     print(k,v)

# def calc_area(w,h):
#     return w*h
#
# def show_max(a,b,c):
#     max_num = a
#     if b > max:
#         max_num = b
#     if c > max:
#         max_num = c
#     return max_num
#
# def login():
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name == "admin" and password == "123456":
#         return True
#     else:
#         return False

# def test():
#     return 10,20,30     # 返回多个值，本质返回元组，括号可以省略,用一个变量接收则得到一个元组(10,20,30)

# def sum_all(*args):     #不定长位置参数 `*args`，接收任意数量位置参数，打包成**元组**
#     print(args)      # args是元组
#     total = 0
#     for i in args:
#         total += i
#     return total
#
# print(sum_all(1,2,3))
# print(sum_all(10,20,30,40))

# def print_info(**kwargs):       #不定长关键字参数 `**kwargs`，接收任意数量`key=value`，打包成**字典**
#     print(kwargs)       #字典
#
# print_info(name="小明",age=18)

# def calc_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(calc_sum(1,2))

# def user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# square = lambda x: x**2     #lambda是一次性小函数
# print(square(5))

# nums = [1,2,3,4]        #使用map+lambda练习
# result = list(map(lambda x: x ** 2, nums))
# print(result)

"""文件操作"""
# f = open("test.txt","w",encoding="utf-8")       #以 "w" 模式打开 → 创建/清空文件
# f.write("hello python\n")
# f.write("文件测试\n")
# f.close()
# f = open("test.txt","a",encoding="utf-8")       #以 "a" 模式打开 → 在末尾追加内容
# f.write("追加\n")
# f.close()
"""
    - .read()`：一次性读全部字符串
    - .readline()`：读取**一行**
    - .readlines()`：读取全部行，返回**列表**，每一行是列表一个元素
"""
# with open("test.txt","w",encoding="utf-8") as f:
#     f.write("第一行文字\n")
#     f.write("第二行文字")
# with open("test.txt","r",encoding="utf-8") as f:
#     content = f.read() # 一次性读取全部内容
# print(content)

# with open("student.txt","w",encoding="utf-8") as f:
#     f.write("小明\n")
#     f.write("小美\n")
#     f.write("小帅\n")
# with open("student.txt","r",encoding="utf-8") as f:
#     content = f.read()
# print(content)
# with open("student.txt","r",encoding="utf-8") as f:
#     line1 = f.readline()
#     print(line1)
# with open("student.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()       #`readlines()`拿到的每一行字符串末尾自带换行符`\n`
# print(lines)

# try:        #可能出错的代码
#     with open("stock.txt","r",encoding="utf-8") as f:
#         c =f.read()
# except:     #出错后
#     print("找不到文件！")
# else:       #正常
#     print(c)
# finally:    #无论如何都会执行
#     print("这一行必定执行！")

# try:
#     with open("student.txt","r",encoding="utf-8") as f:
#         c = f.read()
# except FileNotFoundError:
#     print("文件不存在！")
# else:
#     print(c)
# finally:
#     print("文件读取操作结束。")

"""模块import,模块就是别人写好的`.py`代码文件，拿来直接用。"""
# # 方式1：导入整个模块
# import time
# print(time.time())
#
# # 方式2：from 模块 import 工具，直接拿函数/类，不用写模块名
# from time import sleep
# sleep(2)   # 暂停2秒
#
# # 方式3：导入起别名
# import datetime as dt

# import json
# student = {"name":"小明","hobby":["看书","打球"]}
# json_str = json.dumps(student,ensure_ascii = False)
# print(json_str, type(json_str))
# data = json.loads(json_str)
# print(data, type(data))

"""面向对象OOP"""
# class Student:
#     # 构造方法：创建对象的时候自动执行
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         print(f"学生的姓名是：{self.name},年龄是{self.age}")
#
# s1 = Student("小明",18)
# s1.show_info()

# class Dog:
#     def __init__(self, dog_name, dog_age):
#         self.name = dog_name
#         self.age = dog_age
#     def brak(self):
#         print(f"{self.name}在汪汪叫")
#
# d1 = Dog("大狗",3)
# d1.brak()
# d2 = Dog("小狗",2)
# d2.brak()

"""继承OOP"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name}会吃东西。")
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def info(self):
#         print(f"{self.name},{self.age}岁")
# d = Dog("旺财", 1)
# d.info()
# d.eat()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say(self):
#         print(f"{self.name}在说话")
# class Student(Person):
#     def __init__(self, name, stu_id):
#         super().__init__(name)
#         self.stu_id = stu_id
#     def study(self):
#         print(f"{self.name}正在学习,学号:{self.stu_id}")
# student = Student("小明",18)
# student.say()
# student.study()

"""OOP的封装、多态"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self._age = 18      # _开头：约定私有，建议外部不要直接访问,调用方法读写即为封装
#     def getAge(self):
#         return self._age
#     def setAge(self, new_age):
#         if 0 < new_age < 120:
#             self._age = new_age
#         else:
#             print("年龄不合法")
# p = Person("小帅")
# print(p.getAge())
# p.setAge(20)
# print(p.getAge())

# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
# def make_sound(animal):
#     animal.speak()
# make_sound(Dog())
# make_sound(Cat())

"""常用标准库"""
# from datetime import datetime       #datetime库
# now = datetime.now()
# print(now)
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# str_time = "2026-09-04"
# dt = datetime.strptime(str_time, "%Y-%m-%d")
# print(dt)
#
# import os       #os库
# print(os.getcwd())

# from datetime import datetime
# now = datetime.now()
# str_time = datetime.strftime(now,"%Y-%m-%d %H:%M:%S")
# print(str_time)
# now_time = datetime.strptime(str_time,"%Y-%m-%d %H:%M:%S")
# print(now_time)

"""Numpy库,ndarray数组"""
# import numpy as np
# arr1 = np.array([1,2,3,4])      #列表转数组
# print(arr1,type(arr1))
# arr2 = np.array([[1,2],[3,4]])      #数组存数组
# print(arr2)
# zeros = np.zeros((2,3))
# print(zeros)
# ones  = np.ones((3,2))
# print(ones)
# arr3 = np.arange(0,10,2)
# print(arr3)
# print(zeros.shape)
# print(zeros.ndim)
# print(zeros.dtype)
# print(zeros.size)
# arr = np.array([1,2,3])     #数组和数字计算时每个元素全部参与计算
# print(arr+10)
# print(arr*2)
# a1 = np.array([1,2,3])      #数组计算时，对应位置元素运算
# a2 = np.array([10,20,30])
# print(a1+a2)
# print(a1*a2)

import numpy as np
# arr1 = np.array([2,4,6,8,10])
# print(arr1.shape)
# print(arr1.ndim)
# print(arr1.size)
# print(arr1+5)
# arr2 = np.ones((2,3))
# print(arr2)

# arr = np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[1:3])     # 切片 [1,3)，20 30
# print(arr[::2])     # 步长2，隔一个取

# arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d[0])
# print(arr2d[0,1])
# print(arr2d[1:,:2])      # 行：从1行往后；列：取前两列

# arr = np.array([1,2,3,4,5,6])
# mask = arr >3       ## 生成布尔掩码
# print(mask)
# print(arr[mask])

# arr2d = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(arr2d[2])
# print(arr2d[1][0])
# print(arr2d[1:,1:])
# mask = arr2d > 40
# print(arr2d[mask])

# data = np.array([[11,22,33],[44,55,66],[77,88,99]])
# print(np.sum(data))
# print(np.max(data))
# print(np.mean(data,axis = 1))       #axis=0按列,axis=1按行，注意数组计算就用numpy里的函数不要直接用sum()之类的

"""Pandas"""
"""Series一维带标签数组"""
import pandas as pd
# s1 = pd.Series([10,20,30])
# print(s1)
# s2 = pd.Series([100,200,300],index=['a','b','c'])
# print(s2)
# print(s2["a"])
# print(s2.loc["a"])      #标准写法
# print(s2[0])        # 通过位置访问（明确使用 iloc）,如果使用位置最好使用iloc!!不然会警告
# print(s2.iloc[0])
"""DataFrame⭐最重要！表格，类似 Excel 表"""
# df = pd.DataFrame({
#     "name":["小明","小美","小帅"],
#     "age":[18,19,20],
#     "city":["贵阳","昆明","上海"]
# })
# print(df)
# print(df.to_string())
# print(df.to_markdown())     #使用to_markdown()需要下载tabulate库
# print(df.head())
# print(df.columns)
# print(df.shape)
# print(df["name"])

# df = pd.DataFrame({
#     "name":["张三","李四","王五"],
#     "age":[21,22,21],
#     "score":[88,76,92]
# })
# # print(df)
# # print(df.shape)
# # print(df["score"])
# #loc:行标签，列名字
# print(df.loc[0])
# print(df.loc[0,"name"])     #索引0行，name列
# #iloc:数字位置，行号、列号
# print(df.iloc[1])
# print(df.iloc[:,1])     #全部列，第1行（age列）
# mask = df["score"] >80
# print(df[mask])

# df = pd.DataFrame({
#     "name":["张三","李四","王五"],
#     "age":[21,22,21],
#     "score":[88,76,92]
# })
# print(df.loc[0, "name"])
# print(df.iloc[:,[0,2]])         #`iloc`只能传数字下标，不能写列名字符串 `"name","score"`
# mask = (df["age"] == 21) & (df["score"] > 85)      # =是赋值，不是判断相等；and不能用,条件记得打(),布尔筛选要使用&或者|
# print(df[mask])
"""pandas读写文件"""
# df2 = pd.read_csv("student.csv",encoding="utf-8")
# print(df2)
# df2.to_csv("student.csv",index = False, encoding = "utf-8")      #`index=False` 不要把 pandas 行索引存进文件
# data = {
#     "name":["张三","李四","王五","赵六","孙七"],
#     "age":[21,22,21,23,20],
#     "score":[88,76,92,85,65],
#     "city":["贵阳","昆明","贵阳","成都","重庆"]
# }
# df = pd.DataFrame(data)
# df.to_csv("student.csv",index=False,encoding= "utf-8-sig")
# df2 = pd.read_csv("student.csv",encoding="utf-8-sig")
# print(df2)
"""
if 不能接收整列 Series,要使用np.where新增level列判断，np.where嵌套，先高分A，再B
np.where(条件, 满足条件的值, 不满足的值)
np.where(条件1,值1, np.where(条件2,值2,其他值))
dropna()只要这一行任意一列有缺失，整行删掉
fillna()填充缺失值，括号内为填充内容
df.groupby("分组列名")[聚合列].聚合函数()
- `mean()` 平均值
- `sum()` 求和
- `max()` 最大值
- `min()` 最小值
- `count()` 计数
`.reset_index()` 转成表格格式，方便导出 csv,把分组结果变回 DataFrame
"""
# df = pd.read_csv("student.csv",encoding = "utf-8-sig")
# mask = (df["score"]>=80)&(df["city"]=="贵阳")
# df = df[mask]
# df["level"] = np.where(df["score"]>=90,"A",
#                 np.where(df["score"]>=80,"B","C"))
# print(df)
# df.to_csv("result.csv",index=False,encoding = "utf-8-sig")
#同时算多个聚合
# res2 = df.groupby("city")["score"].agg(["mean","max","min","count"]).reset_index()
# print(res2)

# df = pd.read_csv("student.csv",encoding="UTF-8")
# df["score"] = df["score"].fillna(0)
# df["age"] = df["age"].fillna(df["age"].mean())
# df_group = df.groupby("city")["score"].agg(["mean","max"]).reset_index()
# df_group.columns = ["city","avg_score","max_score"]
# df.to_csv("group_result.csv",encoding="utf-8",index=False)
"""matplotlib可视化"""
# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']        # Windows黑体，解决中文
# plt.rcParams['axes.unicode_minus'] = False      # 解决负号乱码
#
# data = {
#     "name":["张三","李四","王五","赵六","孙七"],
#     "age":[21,22,21,23,20],
#     "score":[88,76,92,85,65],
#     "city":["贵阳","昆明","贵阳","成都","重庆"]
# }
# df = pd.DataFrame(data)
#
# # 先分组聚合
# df_city = df.groupby("city")["score"].mean().reset_index()

# 聚合后绘图，每个城市只1根柱子
# df_city.plot(kind="bar", x="city", y="score", label="城市分数统计")
# plt.title("城市分数统计")
# plt.xlabel("城市")
# plt.ylabel("平均分数")
# plt.legend()
# plt.xticks(rotation=0)  # x轴文字不旋转
"""
- `"city_score.png"`：保存的文件名，会保存到你的项目文件夹 study 下面；也可以写完整路径
- `dpi=150`：清晰度，数值越大图片越清晰
- `bbox_inches="tight"`：**把标题、坐标轴文字全部包含进去，防止文字被截断！做报告必加这个参数**
支持格式：`.png`、`.jpg`、`.pdf`
"""
# plt.savefig("city_bar.png",dpi=150,bbox_inches='tight')       # 保存图片，写在plt.show()之前！！
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False
#
# data = {
#     "name":["张三","李四","王五","赵六","孙七"],
#     "age":[21,22,21,23,20],
#     "score":[88,76,92,85,65],
#     "city":["贵阳","昆明","贵阳","成都","重庆"]
# }
# df = pd.DataFrame(data)
# df.to_csv("student_total.csv",encoding="utf-8-sig",index=False)
# df_nan = pd.read_csv("student_total.csv",encoding="utf-8-sig")
# df_nan.loc[0,"score"] = None
# df_nan.loc[2,"age"] = None
# df_nan["score"] = df_nan["score"].fillna(0)
# df_nan["age"] = df_nan["age"].fillna(df_nan["age"].mean())
# df_nan["level"] = np.where(df_nan["score"]>=90,"A",
#                        np.where(df_nan["score"]>=80,"B","C"))
# df_group = df_nan.groupby("city")["score"].agg(["mean","max"]).reset_index()
# df_group.columns = ["city","mean_score","max_score"]
# df_group.plot(kind="bar",x="city",y="mean_score",label="城市分数统计")
# plt.title("城市分数统计")
# plt.xlabel("城市")
# plt.ylabel("分数")
# plt.legend()
# plt.savefig("city_stat.png",dpi=150,bbox_inches="tight")
# plt.show()

"""MySQL+pymysql"""
# import pymysql
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# data = {
#     "name":["张三","李四","王五","赵六","孙七"],
#     "age":[21,22,21,23,20],
#     "score":[88,76,92,85,65],
#     "city":["贵阳","昆明","贵阳","成都","重庆"]
# }
# df = pd.DataFrame(data)
# df_nan = df.copy()
# df_nan.loc[0,"score"] = None
# df_nan.loc[2,"age"] = None
# df_nan["score"] = df_nan["score"].fillna(0)
# df_nan["age"] = df_nan["age"].fillna(df_nan["age"].mean())
# df_nan["level"] = np.where(df_nan["score"]>=90,"A",
#                            np.where(df_nan["score"]>=80,"B","C"))
# conn = pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="python_etl",
#     charset="utf8mb4"
# )
# cursor = conn.cursor()
# create_table_sql = """
# CREATE TABLE IF NOT EXISTS student (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(20),
#     age INT,
#     score INT,
#     city VARCHAR(20),
#     level CHAR(1)
# );
# """
# cursor.execute(create_table_sql)
# print("\n数据表已建立/已存在")
# cursor.execute("""TRUNCATE TABLE student;""")
# for _, row in df_nan.iterrows():
#     sql_insert = """
#     INSERT INTO student(name,age,score,city,level)
#     VALUES (%s,%s,%s,%s,%s)
#     """
#     cursor.execute(sql_insert,(row["name"],row["age"],row["score"],row["city"],row["level"]))
# conn.commit()       #提交事物，数据真实落库
# print("√数据插入成功")
# sql_query = "SELECT * FROM student;"
# df_from_mysql = pd.read_sql(sql_query,conn)
# print("\n从MySQL读取的数据：")
# print(df_from_mysql)
# sql_group = """
# SELECT city, AVG(score) as mean_score, MAX(score) as max_score
# FROM student
# GROUP BY city
# """
# df_sql_group = pd.read_sql(sql_group,conn)
# print("\nSQL分组统计结果:")
# print(df_sql_group)
# select_sql = """SELECT * FROM student WHERE score > 70 AND city = '贵阳';"""
# df_tset = pd.read_sql(select_sql,conn)
# print("查询结果:")
# print(df_tset)
# cursor.execute("""UPDATE student SET score = 78 WHERE name = '孙七';""")
# conn.commit()
# cursor.execute("""DELETE FROM student WHERE score = 0;""")
# conn.commit()
# after_df = pd.read_sql("""SELECT * FROM student;""",conn)
# print("\n最终结果:")
# print(after_df)
# cursor.close()
# conn.close()

# import pymysql
# import pandas as pd
# conn = pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="123456",
#     database="python_etl",
#     charset="utf8mb4"
# )
# cursor = conn.cursor()
# update_class_sql = """
# UPDATE student SET class_id = %s WHERE name = %s
# """
# cursor.executemany(update_class_sql,[
#     (1,"李四"),
#     (1,"王五"),
#     (2,"赵六"),
#     (3,"孙七")
# ])
# conn.commit()
# print("√学生班级ID分配完成")
# sql_inner="""
# SELECT s.name,s.score,c.class_name,c.teacher
# FROM student s
# INNER JOIN class_info c ON s.class_id = c.class_id;
# """
# df_inner = pd.read_sql(sql_inner,conn)
# print("\n内连接结果:")
# print(df_inner)
# sql_left = """
# select s.name,s.score,c.class_name,c.teacher
# from student s
# left join class_info c on s.class_id = c.class_id;
# """
# df_left = pd.read_sql(sql_left,conn)
# print("\n左连接结果:")
# print(df_left)
# #使用group by 不能直接查询`name、score`，MySQL 严格模式直接报错！group by 规则：**select 后面非聚合字段，必须全部出现在 group by 中
# sql_join_group = """
# select c.class_name, AVG(s.score) as avg_score, MAX(s.score) as max_score, COUNT(s.name) as stu_count
# from student s
# left join class_info c on s.class_id = c.class_id
# group by c.class_name;
#
# """
# df_group_join = pd.read_sql(sql_join_group,conn)
# print("\n班级分组统计:")
# print(df_group_join)
# df_left.to_csv("student.csv",index=False,encoding="utf-8")
# print("\n已导出文件")
#
# sql_test = """
# select c.class_name, AVG(s.score) as avg_score, count(s.name) as num_student
# from student s
# left join class_info c on s.class_id = c.class_id
# where s.score > 80
# group by c.class_name;
# """
# df_test = pd.read_sql(sql_test,conn)
# df_test.to_csv("high_score_class.csv",index=False,encoding="utf-8")
# print(df_test)
# cursor.close()
# conn.close()

# import pymysql
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# raw_data = {
#     "name":["张三","李四","王五","赵六","孙七","周八"],
#     "age":[20,21,None,22,23,21],
#     "score":[95,-5,72,88,None,66],
#     "class_id":[1,1,2,2,3,3]
# }
# df_raw = pd.DataFrame(raw_data)
# df_raw.to_csv("raw_student.csv",index=False,encoding="utf-8-sig")
# print("\n脏数据生成完成")
# df = pd.read_csv("raw_student.csv",encoding="utf-8-sig")
# df["age"] = df["age"].fillna(df["age"].mean())
# df["score"] = df["score"].fillna(0)
# df.loc[(df["score"]<0)|(df["score"]>100),"score"]=0
# df["level"] = np.where(df["score"]>90,"A",
#                        np.where(df["score"]>80,"B",
#                                 np.where(df["score"]>=60,"C","D")))
# print("\n数据清洗完毕")
# print(df)
# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="123456",
#     database="python_etl",
#     charset="utf8mb4"
# )
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS etl_class;")
# create_class_sql = """
# CREATE TABLE etl_class(
#     class_id INT PRIMARY KEY AUTO_INCREMENT,
#     class_name VARCHAR(30),
#     teacher VARCHAR(20)
# );
# """
# cursor.execute(create_class_sql)
# cursor.executemany("INSERT INTO etl_class(class_name, teacher) VALUES(%s, %s)", [
#     ("一班","王老师"),
#     ("二班","李老师"),
#     ("三班","张老师")
# ])
# cursor.execute("DROP TABLE IF EXISTS etl_student;")
# create_student_sql = """
# CREATE TABLE etl_student(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(20),
#     age INT,
#     score INT,
#     level CHAR(1),
#     class_id INT
# );
# """
# cursor.execute(create_student_sql)
# conn.commit()
# print("\n建表完成")
# insert_sql="""
# INSERT INTO etl_student(name,age,score,level,class_id)
# VALUES(%s,%s,%s,%s,%s);
# """
# for _,row in df.iterrows():
#     cursor.execute(insert_sql,(row["name"],row["age"],row["score"],row["level"],row["class_id"]))
# conn.commit()
# print("\n清洗后数据入库完成")
# join_sql = """
# SELECT c.class_name , AVG(s.score) as avg_score, MAX(s.score) as max_score, COUNT(s.name) as stu_count
# FROM etl_student s
# LEFT JOIN etl_class c ON c.class_id = s.class_id
# GROUP BY c.class_name;
# """
# df_report = pd.read_sql(join_sql,conn)
# print("\n完成JOIN班级统计报表")
# print(df_report)
# df_report.to_csv("class_score_report.csv",index=False,encoding="utf-8-sig")
# print("\n报表导出至 class_score_report.csv")
# plt.figure(figsize=(8,5))
# plt.bar(df_report["class_name"],df_report["avg_score"],color=["#4472C4","#ED7D31","#A5A5A5"])
# plt.title("各个班级平均分")
# plt.xlabel("班级")
# plt.ylabel("平均分")
# plt.grid(axis="y",alpha=0.3)
# plt.savefig("class_avg_score.png",dpi=150,bbox_inches="tight")
# plt.close()
# print("\n图表保存 class_avg_score.png")
# join_left_sql = """
# SELECT c.class_name , COUNT(s.name) as jige_count, AVG(s.score) as jige_avg
# from etl_student s
# left join etl_class c on c.class_id = s.class_id
# where s.score >= 60
# group by c.class_name;
# """
# test_insert = pd.read_sql(join_left_sql,conn)
# test_insert.to_csv("pass_class_report.csv",index=False,encoding="utf-8-sig")
# print(test_insert)
# cursor.close()
# conn.close()
# print("\n全部流程已完成")
