#创建学生信息数据字典（字典的嵌套）
students = {
    '001': {
        '姓名':'张三',
        '年龄':21,
        '性别':'男',
        '成绩':{
            'python':88,
            '数据结构':85,
            '机器学习':92,
            '数据库':88
        }
    },
    '002': {
        '姓名':'李四',
        '年龄':20,
        '性别':'女',
        '成绩':{
            'python':78,
            '数据结构':76,
            '机器学习':80,
            '数据库':74
        }
    },
    '003': {
        '姓名':'王五',
        '年龄':22,
        '性别':'男',
        '成绩':{
            'python':65,
            '数据结构':72,
            '机器学习':58,
            '数据库':68
        }
    },
}
print(students)

#添加键值对，学号004的同学信息
students['004'] = {
        '姓名':'王麻子',
        '年龄':21,
        '性别':'男',
        '成绩':{
            'python':90,
            '数据结构':80,
            '机器学习':65,
            '数据库':84
     }
}
print(students)

#将001同学的数据结构成绩修改为88
students['001']['成绩']['数据结构'] = 88
print(students)

#分别用两种不同的方法访问学号为001同学的信息
pt = students['001']
print(pt)

Pu = students.get('001')
print(Pu)

#遍历字典，打印所有同学的信息
for sid, stu in students.items():
    print(f"学号: {sid}")
    print(f"姓名: {stu['姓名']}")
    print(f"年龄: {stu['年龄']}")
    print(f"性别: {stu['性别']}")
    print("成绩:")
    for course, score in stu['成绩'].items():
        print(f"{course}: {score}")

#根据规则判定每位同学的等级
for sid, stu in students.items():
    scores = list(stu['成绩'].values())      # 所有课程分数
    avg = sum(scores) / len(scores)          # 平均分
    fail = sum(1 for s in scores if s < 60)  # 挂科门数（<60）

    if avg >= 85 and all(s >= 70 for s in scores):
        level = '优秀'
    elif avg >= 75 and all(s >= 60 for s in scores):
        level = '良好'
    elif avg >= 60 and fail <= 1:
        level = '中等'
    elif avg >= 60:
        level = '及格'
    else:
        level = '不及格'  

    print(f"{stu['姓名']}（{sid}）: 平均分={avg:.1f}，挂科={fail}门，等级：{level}")

#将每位同学的成绩等级添加到字典中
for sid, stu in students.items():
    scores = list(stu['成绩'].values())
    avg = sum(scores) / len(scores)
    fail = sum(1 for s in scores if s < 60)

    if avg >= 85 and all(s >= 70 for s in scores):
        level = '优秀'
    elif avg >= 75 and all(s >= 60 for s in scores):
        level = '良好'
    elif avg >= 60 and fail <= 1:
        level = '中等'
    else:                 # avg >= 60 兜底
        level = '及格'

    # 把等级写回字典
    stu['等级'] = level
# 验证
print(students)

#词频统计
import re
from collections import Counter

text = """Programming is the art of telling 
another human what one wants the computer to
do Programming is a creative process that 
involves problem solving and logical thinking
When we write code we are not just giving
commands to a machine we are expressing ideas 
and solutions in a language that both humans and 
computers can understandThe joy of programming
comes from the satisfaction of solving complex
problems and creating something useful from 
nothing It is like building with digital bricks
where each line of code contributes to the final
structure Programmers experience a unique sense
of accomplishment when their code runs successfully 
and produces the desired results"""

# 1. 分词
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# 2. 创建词频字典
freq_dict = Counter(words)          # 等价于手动累加，但更简洁

# 3. 三种排序法
by_alpha = dict(sorted(freq_dict.items()))                       # a-z
by_freq  = dict(sorted(freq_dict.items(), key=lambda kv: (-kv[1], kv[0])))
by_len   = dict(sorted(freq_dict.items(), key=lambda kv: (len(kv[0]), kv[0])))

# 4. 打印
print("字典序 a-z：", by_alpha)
print("词频从大到小：  ", by_freq)
print("单词长度从短到长：  ", by_len)

#给定字符串s，找出其中不含重复字符的最长子串的长度
def len_strin(s: str) -> int:
    left = 0                 # 窗口的左边界
    seen = set()             # 当前窗口内的字符
    max_len = 0

    for right, ch in enumerate(s):   # right 是右边界
        while ch in seen:            # 重复了就收缩左边界
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        max_len = max(max_len, right - left + 1)

    return max_len

print(len_strin("abcabcbb")) 
print(len_strin("bbbbb"))     
print(len_strin("pwwkew"))   