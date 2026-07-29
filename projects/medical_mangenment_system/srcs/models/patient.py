
class Patient:
    def __init__(self,ID,name,age,gender,disease) -> None:
        """
        初始化患者
        :param name: 患者姓名
        :param ID: 患者ID
        :param age: 患者年龄
        :param gender: 患者性别
        :param disease: 患者疾病
        """
        self.name=name
        self.ID=ID
        self.age=age
        self.disease=disease
        self.gender = gender

    def show_info(self) -> None:
        """
        显示患者信息
        :return: None
        """
        print(
        f"患者ID:{self.ID}\n"
        f"患者姓名：{self.name}\n"
        f"年龄：{self.age}\n"
        f"性别：{self.gender}\n"
        f"疾病：{self.disease}"
        )

    def update_info(self) -> None:
        """
        更新患者信息
        :return: None
        """
        print("请输入患者信息：")
        self.name=input("姓名：")
        self.age=int(input("年龄："))
        self.gender=input("性别：")
        self.disease=input("疾病：")
        print("更新成功")

    def to_dict(self) -> dict:
        """
        将患者信息转换为字典
        :return: 患者信息字典
        """
        return {
            "ID":self.ID,
            "name":self.name,
            "age":self.age,
            "gender":self.gender,
            "disease":self.disease
        }


if __name__ == "__main__":
    patient=Patient("1001","张三",18,"男","高血压") 
    patient.show_info()