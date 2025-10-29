#将刚才编写的所有类写到一个类的模块文件中
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

