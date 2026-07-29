


# 用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过
# 1，添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    # 1.1输入学生姓名、语文成绩、数学成绩、英语成绩
    # 1.2检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不极加）
    # 1.3验证成绩范围（0-100分）
    # 1.4创建学生对象并添加到系统
# 2，修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    # 2.1输入要修改的学生姓名
    # 2.2根据姓名查找该学生，显示该生当前成绩信息
    # 2.3输入新的语文、数学、英语成绩
    # 2.4更新学生成绩数据
# 3，删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4。查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
# 4.1输出格式为：“姓名：张三|语文：85/数学：90/英语：88/总分：263"
# 5，展示全部学生成绩：展示出系统中所有学生的成绩信息，输出格式为：“姓名：张三,语文：85,数学：90,英语：88,总分：263"
import json
from pathlib import Path
#数据文件路径，用于存储学生信息
DATA_FILE = Path(__file__).with_name("students.json")


class Student:#学生类
    def __init__(self, name, math, english, chinese):
        """
        初始化学生对象
            params name: 学生姓名
            params math: 数学成绩
            params english: 英语成绩
            params chinese: 语文成绩
        """
        self.name = name
        self.math = math
        self.english = english
        self.chinese = chinese
    
    def __str__(self):
        """
        返回学生的成绩信息
        """
        return (
        f"学生姓名：{self.name},"
        f"语文成绩：{self.chinese},"
        f"数学成绩：{self.math},"
        f"英语成绩：{self.english},"
        f"总成绩：{self.chinese + self.math + self.english}"
        )
    
    #修改学生成绩
    def modify_score(self, math=None, english=None, chinese=None):
                """
                修改学生成绩
                params math: 数学成绩
                params english: 英语成绩
                params chinese: 语文成绩
                """
                if math is not None:
                    self.math = math
                if english is not None:
                    self.english = english
                if chinese is not None:
                    self.chinese = chinese  
                


class StudentManager:#学生管理类
    def __init__(self):
        self.students = []
        self.load_students()

    def save_students(self):
        """将学生信息保存到 JSON 文件"""
        data = []

        for student in self.students:
            data.append({
                "name": student.name,
                "math": student.math,
                "english": student.english,
                "chinese": student.chinese
            })

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_students(self):
        """程序启动时读取学生信息"""
        if not DATA_FILE.exists():
            return

        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            student = Student(
                item["name"],
                item["math"],
                item["english"],
                item["chinese"]
            )
            self.students.append(student)

    #添加学生成绩
    def add_student(self):

        """
        添加学生成绩"""
        name=input("请输入学生姓名：")
        #判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.students:
            if s.name == name:
                print("该学生已经存在，添加失败！")
                return
        chinese=int(input("请输入学生语文成绩："))   
        math=int(input("请输入学生数学成绩："))
        english=int(input("请输入学生英语成绩："))
    #判断分数是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, math, english, chinese)
            self.students.append(stu)
            self.save_students()
            print("学生信息添加成功~")
        else:
            print("各科成绩必须得在0-100之间")

    #修改学生成绩
    def update_score(self):
        """
        修改学生成绩
        """
        name = input("请输入要修改的学生姓名：")
        for s in self.students:
            if s.name == name:
                print(f"当前成绩：{s}")
                math = int(input("请输入新的数学成绩"))
                english = int(input("请输入新的英语成绩："))
                chinese = int(input("请输入新的语文成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.modify_score(
                    math=math,
                    english=english,#修改列表中的student对象的成绩
                    chinese=chinese
                    )
                    self.save_students()
                    print("修改成功")
                    print(f"修改成绩：{s}")
                    return
                else:
                    print("各科成绩必须得在0-100之间")
                    return
        print("未找到该学生！")

    #删除学生成绩
    def delete_score(self):
            """
            删除学生成绩"""
            name = input("请输入要删除的学生姓名：")
            for s in self.students:
                if s.name == name:
                    self.students.remove(s)
                    self.save_students()
                    print("删除成功")
                    return
            print("未找到该学生！")
            
    #查询学生成绩
    def query_score(self):
        """
        查询学生成绩
        """
        name=input("请输入学生姓名：")
        for s in self.students:
            if s.name == name:
                print(f"查询结果：{s}")
                print("查询成功")
                return
        print("未找到该学生！")
        
    #展示全部学生成绩
    def display_all_scores(self):
        """
        展示全部学生成绩
        """
        for s in self.students:
            print(s)
        print("展示成功")
# if __name__ == "__main__":  
#       # 测试学生类
#       stu1 = Student("张三", 80, 90, 85)
#       print(stu1)
#       stu1.modify_score(math=95, english=92)
#       print(stu1)
#       # 测试学生管理类
      