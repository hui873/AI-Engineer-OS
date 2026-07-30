
class Patient:
    """
    患者类
    """

    def __init__(
        self,
        patient_id: int,
        name: str,
        age: int,
        gender: str,
        id_card: str,
        disease: str,
        phone: str
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.id_card = id_card
        self.disease = disease
        self.phone = phone

    def show_info(self) -> str:
        """
        显示患者信息
        :return: str
        """
        return (
        f"患者编号:{self.patient_id}\n" 
        f"患者姓名：{self.name}\n"
        f"年龄：{self.age}\n"
        f"性别：{self.gender}\n"
        f"身份证号：{self.id_card}\n"
        f"疾病：{self.disease}\n"
        f"手机号：{self.phone}\n"
        f"患者信息已显示"
        )


    def to_dict(self) -> dict:#将患者信息转换为字典
        return {
        "patient_id": self.patient_id,
        "name": self.name,
        "age": self.age,
        "gender": self.gender,
        "id_card": self.id_card,
        "disease": self.disease,
        "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":#从字典创建患者对象
        return cls(
        data["patient_id"],
        data["name"],
        data["age"],
        data["gender"],
        data["id_card"],
        data["disease"],
        data["phone"]
        )


if __name__ == "__main__":
    patient=Patient(1001,"张三",18,"男","44030419900101001X","高血压","13800000000")   
    patient.show_info()