#编写2个函数分别实现摄氏度转华氏度、华氏度转摄氏度
# 把摄氏度转成华氏度
def c_to_f(c):
    f = c * 1.8 + 32
    return f
# 把华氏度转成摄氏度
def f_to_c(f):
    c = (f - 32) / 1.8
    return c

#编写1个通用温度转换函数，能同时实现摄氏度转华氏度与华氏度转摄氏度
def temp_convert(value, from_unit):
    from_unit = from_unit.upper()
    if from_unit == 'C':
        return value * 1.8 + 32
    elif from_unit == 'F':
        return (value - 32) / 1.8
    else:
        raise ValueError
    
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

#-------任务2--------------
#编写函数 计算任意数量数字的和（要求可以传递任意数量实参）
def add_all(*args):
    return sum(args)

#编写函数实现个人信息管理，要求姓名和年龄为必要参数，其余可以接收任意数量的个人信息，返回完整的个人档案字典
def build_profile(name, age, **kwargs):
    profile = {'姓名': name, '年龄': age}
    profile.update(kwargs)
    return profile


