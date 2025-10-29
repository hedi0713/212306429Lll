#学生个人信息
student_name = "li si"
student_age = 18
student_height = 1.65
student_weight = 52.75
#学生成绩
student_english = 80
studnet_math = 85
student_china = 90

print(f"学生的姓名是：{student_name}")
print(f"学生的年龄是：{student_age}")
print(f"学生的身高是：{student_height}米")
print(f"学生的体重是：{student_weight}千克")
print(f"学生的英语成绩是：{student_english}")
print(f"学生的数学成绩是：{studnet_math}")
print(f"学生的语文成绩是：{student_china}")

#修改年龄
student_age = student_age + 2
print(f"修改后的年龄是：{student_age}")
#强制转换为字符串类型
age_str = str(student_age)
print(f"age_str的数据类型是{type(age_str)}")
#强制转换为整数类型
age_int = int(age_str)
print(f"age_int的数据类型是{type(age_int)}")

#使用round函数
student_height_round = round(student_height,1)
print(f"原身高为：{student_height},修改为：{student_height_round}")
student_weight_round = round(student_weight,1)
print(f"原体重为：{student_weight},修改为：{student_weight_round}")

#计算BMI
BMI = round(student_weight/(student_height ** 2),2)
print(f"BMI值为：{BMI}")

#学生成绩统计
total = student_china + student_english + studnet_math
print(f"学生的总成绩是：{total}")
avg = round(total/3,2)
print(f"学生的平均分是：{avg}")
max_score = max(student_china, student_english, studnet_math)
print(f"最高分是：{max_score}")
min_score = min(student_china, studnet_math, student_english)
print(f"最低分是：{min_score}")

#姓名分割
student_name = student_name.title()
print(f"修改后的姓名为：{student_name}")

studnet_first_last_name = student_name.split(" ")
first_name = studnet_first_last_name[0]
last_name = studnet_first_last_name[1]
print(f"学生的姓为：{first_name}, 学生的名为：{last_name}")

first_name = "Wu"
new_name = first_name + last_name
print(f"学生的新名字为：{new_name}")

#字符串反转
reversed_name = new_name[::-1]
print(f"学生的姓名反转为：{reversed_name}")
