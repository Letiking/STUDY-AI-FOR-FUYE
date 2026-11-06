###############################################################################
###############################################################################
###############################################################################
#学完之后用AI转换为MARKdown格式，形成目录层级
#W1.1 变量、数据类型、print / input、格式化输出 运算符 加减乘除取余取模 字符串拼接  String（字符串）List（列表）Tuple（元组）Set（集合）Dictionary（字典） 运算符
a=10
b=3.14
c="Hello, World!"
print(a)
print(b)
print(c)
#数据类型 String（字符串）List（列表）Tuple（元组）Set（集合）Dictionary（字典）
aa=type(a)
bb=type(b)
cc=type(c)
print(str(aa)+" "+str(bb)+" "+str(cc))
a1="Hello"
a2=[1,2,3]
a3=(4,5,6)
a4={7,8,9}
a5={"name": "Alice", "age": 30}
print(str(type(a1))+" "+str(type(a2))+" "+str(type(a3))+" "+str(type(a4))+" "+str(type(a5))) 
d=input("请输入一个数字：")
print(d)
d1=int(d)
print(d1)
print("a=%d,b=%.2f,c=%s" % (a,b,c))
print("a={},b={:.2f},c={}".format(a,b,c)) #最简洁
print(f"a={a},b={b:.2f},c={c}")
e=10
f=3
g=e+f
h=e-f
i=e*f
j=e/f
k=e%f
print("g={},h={},i={},j={},k={}".format(g,h,i,j,k)+"字符串拼接："+"Hello"+" "+"World!")
#运算符 都有哪些？
# +, -, *, /, %, **, //
# ==, !=, >, <, >=, <=
# and, or, not
# =, +=, -=, *=, /=, %=, **=, //=
# in,not in
# is, is not
# 三元运算符
x=5
y=1
z=x if x>y else y
print(z)
# z = (x > y) ? x : y;  # This is not valid Python syntax
# 列表生成
list1=[i for i in range(10)]
print(list1)
# 列表生成如果偶数保留，否则改为66
list2=[i if i%2==0 else 66 for i in range(10)]
print(list2)
# 列表生成如果偶数保留，否则舍弃，且只保留前3个
list3=[i for i in range(10) if i%2==0][:3]
print(list3)


###############################################################################
###############################################################################
###############################################################################
# w1.2 字符串、列表、字典	写命令行计算器（加减乘除）	计算器能正确算出结果，能处理异常情况
str1="Hello, World!"
print(f"{str1[0]} {str1[7]}") #H W
list1=[1,2,3,4,5]
print(f"{list1[0]} {list1[-1]}") #1 5
dict1={"name": "Alice", "age": 30}
print(f"{dict1['name']} {dict1['age']}") #Alice 30 #字典的键值访问要加双引号或单引号，字典结构和json类似
print(f"{dict1['name'][:5]} {str1[7:12]}") #Alice World  :5代表取前5个字符，7:12代表取第7到第11个字符，下标从0开始计数，左闭右开区间，所以是取第7个字符到第11个字符
#从后面取-1和:结合示例
print(f"{str1[-1]} {str1[-5:-1]} {str1[:-5]}") #! orld Hello, W

# 命令行计算器
def calculator():
    while True:
        try:
            num1 = input("请输入第一个数字（或输入'q'退出）：")
            # raise RuntimeError("手动测试异常") 
            if num1.strip().lower() == 'q':
                print("退出计算器。")
                break
            num1 = float(num1)
            operator = input("请输入运算符（+、-、*、/）：")
            num2 = float(input("请输入第二个数字："))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("错误：除数不能为零！")
                    continue
                result = num1 / num2
            else:
                print("错误：无效的运算符！")
                continue

            print(f"结果：{num1} {operator} {num2} = {result}")

        except ValueError:
            print("错误：请输入有效的数字！")
        except Exception as e:
            print(f"发生异常：{e}")

if __name__ == "__main__":
    calculator()


###############################################################################
###############################################################################
###############################################################################
# w1.3 if/elif/else、for/while 循环	给计算器加循环菜单与退出条件	菜单能循环不崩

def caculator_with_menu():
    while True:
        print("\n欢迎使用命令行计算器")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")

        choice = input("请选择操作（1-5）：")

        if choice == '5':
            print("退出计算器。")
            break

        if choice not in ['1', '2', '3', '4']:
            print("错误：无效的选择，请输入1-5之间的数字！")
            continue

        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))

            if choice == '1':
                result = num1 + num2
                operator = '+'
            elif choice == '2':
                result = num1 - num2
                operator = '-'
            elif choice == '3':
                result = num1 * num2
                operator = '*'
            elif choice == '4':
                if num2 == 0:
                    print("错误：除数不能为零！")
                    continue
                result = num1 / num2
                operator = '/'

            print(f"结果：{num1} {operator} {num2} = {result}")

        except ValueError:
            print("错误：请输入有效的数字！")
        except Exception as e:
            print(f"发生异常：{e}")

if __name__ == "__main__":
    caculator_with_menu()



###############################################################################
###############################################################################
###############################################################################
# w1.3 函数 def、参数与返回值 函数、模块、包	把计算器拆成多个函数	代码结构化可复用
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("除数不能为零")
    return num1 / num2

def calculator_with_functions():
    while True:
        print("\n欢迎使用命令行计算器")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")

        choice = input("请选择操作（1-5）：")

        if choice == '5':
            print("退出计算器。")
            break

        if choice not in ['1', '2', '3', '4']:
            print("错误：无效的选择，请输入1-5之间的数字！")
            continue

        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))

            if choice == '1':
                result = add(num1, num2)
                operator = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operator = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operator = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operator = '/'

            print(f"结果：{num1} {operator} {num2} = {result}")

        except ValueError as ve:
            print(f"错误：{ve}")
        except Exception as e:
            print(f"发生异常：{e}")

if __name__ == "__main__":
    calculator_with_functions()



# 既不需要侵入，也不需要函数重复执行
import time
def deco(func):
    def wrapper(): #闭包
        startTime = time.time()
        func()
        endTime = time.time()
        times = endTime - startTime
        print("time is %d s" %times) #如果这里改成return 那么下面就得写成
        print(func())
        return wrapper
@deco
def f():
    print("hello")
    time.sleep(1)
    print("world")
f() # type: ignore #这里f被赋值为func，执行f()就是执行func()



# 文件读写 open、JSON 模块	写记账脚本：输入存进 txt	数据能存、能读回
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

write_to_file('data.txt', 'Hello, this is a test.')
content = read_from_file('data.txt')
print(content)

def write_json_to_file(filename, data):
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json_from_file(filename):
    import json
    with open(filename, 'r') as file:
        return json.load(file)

write_json_to_file('data.json', {'name': 'Alice', 'age': 30})
json_content = read_json_from_file('data.json')
print(json_content)



# HTTP/API 概念、requests、API Key	调一个免费 API（如天气），打印返回 JSON	能拿到 JSON 数据
# API Key 是一个用于验证身份的密钥，通常用于访问需要身份验证的 API。它可以帮助 API 提供者识别和授权用户，确保只有合法用户才能访问其服务。API Key 通常是一个字符串，由字母、数字和特殊字符组成，用户在请求 API 时需要将其包含在请求头或请求参数中。
# requests.post 是 Python 中 requests 库的一个方法，用于向指定的 URL 发送 POST 请求。POST 请求通常用于向服务器提交数据，例如表单数据或 JSON 数据。使用 requests.post 方法时，可以传递 URL、请求头、请求体等参数，以便与服务器进行交互。
import requests
url = "https://uapis.cn/api/v1/translate/text"
# API Key 放在请求头中（标准做法）
headers = {"Authorization": "uapi-7jizkuwt6nIQnICSO3isqURwI2HVHkC3E4KydsIY"}
# to_lang 作为查询参数
params = {"to_lang": "zh"}
# text 作为 JSON 请求体
payload = {"text": "decorator"}
response = requests.post(url, headers=headers, params=params, json=payload)
print(response.json())

import requests
url = "https://uapis.cn/api/v1/misc/weather"
# API Key 放在请求头中（标准做法）
headers = {"Authorization": "uapi-7jizkuwt6nIQnICSO3isqURwI2HVHkC3E4KydsIY"}
# to_lang 作为查询参数
params = {"city": "长春"}

response = requests.get(url, headers=headers, params=params)
print(response.json())

# 大模型 API 文档、鉴权、基础参数	注册 DeepSeek / 通义，发第一条对话	返回正常文本
# 大模型 API 文档通常提供了如何使用 API 的详细说明，包括请求方法、请求参数、返回格式等。鉴权是指验证用户身份的过程，通常通过 API Key 或 OAuth 等方式进行。基础参数是指在调用 API 时必须提供的参数，例如模型名称、输入文本等。
# base_url (OpenAI)	https://api.deepseek.com
# base_url (Anthropic)	https://api.deepseek.com/anthropic
# api_key	申请一个 API key
# model	deepseek-flash(1)
# deepseek-v4-pro

# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
client = OpenAI(
     api_key='sk-3a7a7c5cc04a4dffbfbdd47c94c1cf89',
    base_url="https://api.deepseek.com",
     timeout=60.0)
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的助手"},
        {
            "role": "user",
            "content": "今天长春绿园区天气如何？请用简洁的语言告诉我天气、温度和风力情况。",
        },
    ],
    stream=False,
)
print(response.choices[0].message.content)