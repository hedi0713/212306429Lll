#编写2个函数分别实现摄氏度转华氏度、华氏度转摄氏度
# 把摄氏度转成华氏度
def c_to_f(c):
    f = c * 1.8 + 32
    return f
# 把华氏度转成摄氏度
def f_to_c(f):
    c = (f - 32) / 1.8
    return c
print("4℃ =", c_to_f(4), "℉")
print("97.5℉ =", f_to_c(97.5), "℃")

#编写1个通用温度转换函数，能同时实现摄氏度转华氏度与华氏度转摄氏度
def temp_convert(value, from_unit):
    from_unit = from_unit.upper()
    if from_unit == 'C':
        return value * 1.8 + 32
    elif from_unit == 'F':
        return (value - 32) / 1.8
    else:
        raise ValueError
print(temp_convert(4, 'C'))
print(temp_convert(97.5, 'F'))

#编写批量温度转换函数，接收温度列表作为参数，返回一个包含转换后温度值的新列表，不修改原始列表。
def all_temp_convert(temp_list, from_unit):
    from_unit = from_unit.upper()
    new_list = []
    if from_unit == 'C':
        for t in temp_list:
            new_list.append(t * 1.8 + 32)
    elif from_unit == 'F':
        for t in temp_list:
            new_list.append((t - 32) / 1.8)
    else:
        raise ValueError
    return new_list
old_1= [0, 50, 100]
new_1 = all_temp_convert(old_1, 'C')
print("原列表:", old_1)
print("新列表:", new_1)
old_2 = [0, 98.5, 100]
new_2 = all_temp_convert(old_2, 'F')
print("原列表:", old_2)
print("新列表:", new_2)

#编写批量温度转换函数，直接在传入的原始列表上进行修改，观察原始列表的变化，并演示如何避免原始列表被修改
#直接改原列表
def batch_temp_convert_inplace(temp_list, from_unit):
    from_unit = from_unit.upper()
    if from_unit == 'C':
        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i] * 1.8 + 32
    elif from_unit == 'F':
        for i in range(len(temp_list)):
            temp_list[i] = (temp_list[i] - 32) / 1.8
    else:
        raise ValueError
#想保留原列表
def batch_temp_convert_safe(temp_list, from_unit):
    temp_list_copy = temp_list[:]
    batch_temp_convert_inplace(temp_list_copy, from_unit)
    return temp_list_copy

original = [0, 50, 100]
print("原始列表:", original)
batch_temp_convert_inplace(original, 'C')
print("直接改完后的原列表:", original)

original2 = [0, 50, 100]
new_list = batch_temp_convert_safe(original2, 'C')
print("原始列表:", original2)
print("返回的新列表:", new_list)

#-------任务2--------------
#编写函数 计算任意数量数字的和（要求可以传递任意数量实参）
def add_all(*args):
    return sum(args)
print(add_all(9, 33, 4, 77))
print(add_all())

#编写函数实现个人信息管理，要求姓名和年龄为必要参数，其余可以接收任意数量的个人信息，返回完整的个人档案字典
def build_profile(name, age, **kwargs):
    profile = {'姓名': name, '年龄': age}
    profile.update(kwargs)
    return profile
print(build_profile('小红', 18))
print(build_profile('小明', 20, 城市='福州', 爱好='看电影', 电话='11111'))

#--------------任务3-----------------
#将任务1和任务2编写的函数存到一个模块内，在主程序中导入模块，依次调用每个函数
import code5
print("4℃ =", c_to_f(4), "℉")
print("97.5℉ =", f_to_c(97.5), "℃")

print(temp_convert(4, 'C'))
print(temp_convert(97.5, 'F'))

old_1= [0, 50, 100]
new_1 = all_temp_convert(old_1, 'C')
print("原列表:", old_1)
print("新列表:", new_1)
old_2 = [0, 98.5, 100]
new_2 = all_temp_convert(old_2, 'F')
print("原列表:", old_2)
print("新列表:", new_2)

original = [0, 50, 100]
print("原始列表:", original)
batch_temp_convert_inplace(original, 'C')
print("直接改完后的原列表:", original)

original2 = [0, 50, 100]
new_list = batch_temp_convert_safe(original2, 'C')
print("原始列表:", original2)
print("返回的新列表:", new_list)

print(add_all(9, 33, 4, 77))
print(add_all())

print(build_profile('小红', 18))
print(build_profile('小明', 20, 城市='福州', 爱好='看电影', 电话='11111'))

#尝试多种函数参数传递方式，传递位置实参和关键字实参
# 1. 纯位置实参
print('纯位置实参：', code5.add_all(1, 2, 3, 4))

# 2. 纯关键字实参（用 * 解包列表）
nums = [10, 20, 30]
print('关键字实参解包：', code5.add_all(*nums))

# 3. 混用：位置 + 关键字解包
new_nums = (5, 6)
print('位置+解包元组：', code5.add_all(7, *new_nums))

# 4. 位置实参给必填项，其余用关键字实参
p1 = code5.build_profile('李四', 28, 城市='上海', 爱好='画画')
print('关键字实参：', p1)

# 5. 先把零散信息收进字典，再一次性关键字解包
extra = {'城市': '福州', '爱好': '打篮球', '电话': '1385200000'}
p2 = code5.build_profile('王五', 19, **extra)
print('字典解包：**extra：', p2)

# 6. 极端混搭：位置 + 关键字 + 字典解包
p3 = code5.build_profile('赵六', 16, 邮箱='zhao@QQ.com', **{'微信': 'zhao123', 'QQ': '88888888'})
print('混搭解包：', p3)

#尝试多种导入方式：
#-只导入一个或多个需要使用的函数
from code5 import add_all
print('单函数导入：', add_all(1, 2, 3))

from code5 import add_all, build_profile
print('多函数导入：', add_all(10, 20), build_profile('Tom', 18))

#导入整个模块并使用点号语法
import code5 as mt
print('整模块导入：', mt.add_all(7, 8), mt.build_profile('Lucy', 22, 城市='南京'))
