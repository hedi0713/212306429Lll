#编写一个学生类，包含姓名、学号和年龄等属性，以及一个显示学生信息的方法；
class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age

    def display_student(self):
        print(f"姓名: {self.name}")
        print(f"学号: {self.student_id}")
        print(f"年龄: {self.age}")

#创建多个学生对象并测试方法
raw_data = [
    ("张三", "21230601", 22),
    ("李四", "21230602", 19),
    ("王麻子", "21230603", 21),
    ("小明", "21230604", 18),
]

students = [Student(name, student_id, age) for name, student_id, age in raw_data]

for stu in students:
    stu.display_student()

#编写一个本科生类，继承于学生类,
#在本科生类中，除了继承父类的属性和方法外，还需要创建新的属性和方法，如专业、选修课程等
class Undergraduate(Student):
    def __init__(self, name, student_id, age, major):
        super().__init__(name, student_id, age)
        self.major = major
        self.courses = []  # 已选课程，用列表保存课程名

    # ------------------- 业务方法 -------------------
    def add_course(self, course):
        """选课"""
        if course not in self.courses:
            self.courses.append(course)
            print(f"[+] 已添加课程：{course}")
        else:
            print(f"[!] 课程 {course} 已存在，请勿重复添加。")

    def drop_course(self, course: str):
        """退课"""
        if course in self.courses:
            self.courses.remove(course)
            print(f"[-] 已退选课程：{course}")
        else:
            print(f"[!] 课程 {course} 不存在，无法退选。")

    def list_courses(self):
        """查看已选课程"""
        if not self.courses:
            print("当前未选修任何课程。")
        else:
            print("已选课程：", " | ".join(self.courses))

    # 可选择性地重写父类方法，补充子类信息
    def display_student(self):
        super().display_student()
        print(f"专业: {self.major}")
        self.list_courses()

#测试
if __name__ == "__main__":
    stu = Undergraduate("Alice", "2021123456", 19, "计算机科学与技术")
    stu.display_student()
    print("-" * 20)
    stu.add_course("Python 程序设计")
    stu.add_course("数据结构")
    stu.add_course("Python 程序设计")  # 重复添加测试
    stu.drop_course("高等数学")        # 退选未选课程测试
    stu.drop_course("数据结构")
    print("-" * 20)
    stu.display_student()

#编写一个研究生类，继承于学生类,
#在研究生类中，需要增加以下属性：研究方向、导师姓名、发表论文数量、研究进度等,
#需要增加以下方法：更新研究进度、更新论文发表数量等
class Graduate(Student):
    def __init__(self,name,student_id,age,research_area,supervisor,
                 papers: int = 0,
                 progress: float = 0.0):
        super().__init__(name, student_id, age)
        self.research_area = research_area
        self.supervisor = supervisor
        self.papers = papers
        self.progress = progress

    #更新研究进度
    def update_progress(self, delta):
        self.progress = self.progress + delta
    #更新已发表的论文数量
    def publish_papers(self, n):
        self.papers = self.papers + n

    #覆盖输出方法
    def display_student(self):
        super().display_student()
        print(f"研究方向：{self.research_area}")
        print(f"导师：{self.supervisor}")
        print(f"论文数量：{self.papers} 篇")
        print(f"研究进度：{self.progress:.1f}%")

#新建研究生对象
g = Graduate("小新", "202306489", 24,
             research_area="科学",
             supervisor="王教授",
             papers=2,
             progress=30)

#更新
g.publish_papers(2)        # 已发表的论文新增两篇
g.update_progress(15.5)    # 进度向前推进 15.5%

#查看最终结果
g.display_student()

#修改研究生类，将研究方向信息独立为一个类
#研究方向信息
class ResearchDirection:
    def __init__(self, name, category):
        self.name = name
        self.category = category    #所属一级学科 (category)

    def describe(self):
         print(f"研究方向的名称：{self.name}")
         print(f"所属一级学科：{self.category}")

class Graduate(Student):
    def __init__(self,name,student_id,age,research_area: ResearchDirection,supervisor,
                 papers: int = 0,
                 progress: float = 0.0):
        super().__init__(name, student_id, age)
        self.research_area = research_area
        self.supervisor = supervisor
        self.papers = papers
        self.progress = progress

    #更新研究进度
    def update_progress(self, delta):
        self.progress = self.progress + delta
    #更新已发表的论文数量
    def publish_papers(self, n):
        self.papers = self.papers + n

    #覆盖输出方法
    def display_student(self):
        super().display_student()
        print(f"研究方向信息：（名称：{self.research_area.name},所属一级学科：{self.research_area.category}）")
        print(f"导师：{self.supervisor}")
        print(f"论文数量：{self.papers} 篇")
        print(f"研究进度：{self.progress:.1f}%")

#测试
#先创建一个研究方向对象
ai_ddd = ResearchDirection(
    name="学习",
    category="数字媒体",
)

#再用该对象实例化研究生
g = Graduate("小红", "20240444", 24,
             research_area=ai_ddd,
             supervisor="王教授",
             papers=2,
             progress=99.5)

# 3. 查看信息
g.display_student()

#修改研究生类，将导师相关信息独立为一个类
#导师类
class Supervisor:
    def __init__(self, name, title, college, contact):
        self.name = name
        self.title = title
        self.college = college
        self.contact = contact

    def describe(self):
         print(f"导师姓名：{self.name}")
         print(f"职称：{self.title}")
         print(f"所属学院：{self.college}")
         print(f"联系方式：{self.contact}")

class Graduate(Student):
    def __init__(self,name,student_id,age,research_area: ResearchDirection,supervisor:Supervisor,
                 papers: int = 0,
                 progress: float = 0.0):
        super().__init__(name, student_id, age)
        self.research_area = research_area
        self.supervisor = supervisor
        self.papers = papers
        self.progress = progress

    #更新研究进度
    def update_progress(self, delta):
        self.progress = self.progress + delta
    #更新已发表的论文数量
    def publish_papers(self, n):
        self.papers = self.papers + n

    #覆盖输出方法
    def display_student(self):
        super().display_student()
        print(f"研究方向信息：（名称：{self.research_area.name},所属一级学科：{self.research_area.category}）")
        self.supervisor.describe()
        print(f"论文数量：{self.papers} 篇")
        print(f"研究进度：{self.progress:.1f}%")
#测试
#创建研究方向对象
ai_dir = ResearchDirection(
    name="深度学习",
    category="计算机科学与技术",
)

#创建导师对象
prof_wang = Supervisor(
    name="王强",
    title="教授",
    college="计算机学院",
    contact="wangq@QQ"
)

#用以上两个对象实例化研究生
g = Graduate("李研", "2123064555", 24,
             research_area=ai_dir,
             supervisor=prof_wang,
             papers=3,
             progress=62.3)

#查看信息
g.display_student()

#重写研究生类，使用类的组合关系，将研究方向和导师信息实例化的对象作为研究生类的属性
class Graduate(Student):
    def __init__(self,name,student_id,age,research_area: ResearchDirection,supervisor:Supervisor,
                 papers: int = 0,
                 progress: float = 0.0):
        super().__init__(name, student_id, age)
        self.research_area = research_area
        self.supervisor = supervisor
        self.papers = papers
        self.progress = progress

    #更新研究进度
    def update_progress(self, delta):
        self.progress = self.progress + delta
    #更新已发表的论文数量
    def publish_papers(self, n):
        self.papers = self.papers + n

    #覆盖输出方法
    def display_student(self):
        super().display_student()
        print(f"研究方向信息：（名称：{self.research_area.name},所属一级学科：{self.research_area.category}）")
        self.supervisor.describe()
        print(f"论文数量：{self.papers} 篇")
        print(f"研究进度：{self.progress:.1f}%")

#测试
#创建研究方向对象
ai_rr = ResearchDirection(
    name="浅度学习",
    category="软件工程",
)

#创建导师对象
prof_ming = Supervisor(
    name="小明",
    title="教授",
    college="计算机学院",
    contact="Xm@QQ"
)

#用以上两个对象实例化研究生
g = Graduate("小李", "222222", 24,
             research_area=ai_rr,
             supervisor=prof_ming,
             papers=6,
             progress=64.1)

#查看信息
g.display_student()

#将刚才编写的所有类写到一个类的模块文件中
#在主程序中使用多种方式从模块中导入类，并使用类
#直接导入整个模块
import code7

ug1 = code7.Graduate(
        "张三", "2025001", 24,
        code7.ResearchDirection("图神经网络", "计算机科学与技术"),
        code7.Supervisor("李教授", "博导", "计算机学院", "li@edu"),
        papers=2, progress=30)
print("方式1:")
ug1.display_student()
print("-" * 40)

#从模块导入指定类
from code7 import Graduate, ResearchDirection, Supervisor

ai_dir = ResearchDirection("深度学习", "AI")
prof_wang = Supervisor("王教授", "博导", "AI学院", "wang@edu")
ug2 = Graduate("李四", "2025002", 25, ai_dir, prof_wang, papers=5, progress=62.3)
print("方式2:")
ug2.display_student()
print("-" * 40)

#导入并起别名（名字太长或冲突时）
from code7 import Graduate as G, Supervisor as Sup

ug3 = G("王五", "2025003", 23,
        ResearchDirection("区块链", "软件工程"),
        Sup("赵副教", "硕导", "软件学院", "zhao@edu"))
print("方式3:")
ug3.display_student()
print("-" * 40)

#星号导入
from code7 import *
ug4 = Graduate("陈六", "2025004", 24,
               ResearchDirection("量子计算", "物理学"),
               Supervisor("钱院士", "博导", "物理学院", "qian@edu"),
               papers=1, progress=80)
print("方式4：")
ug4.display_student()

#给定一个整数数组 nums ，找到其中最长严格递增子序列的长度。
from typing import List

def length_of_lis(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:         
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 测试
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  
print(length_of_lis([0, 1, 0, 3, 2, 3]))            