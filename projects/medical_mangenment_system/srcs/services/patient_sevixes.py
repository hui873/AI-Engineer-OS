from srcs.models.patient import Patient#导入患者类
class PatientServices:
    """
    患者服务类
    """
    def __init__(self) -> None:#初始化患者列表为空
        self.patients = []

    def add_patient(self, patient: Patient) -> None:#添加患者
        self.patients.append(patient)

    def get_patient(self, patient_id: int) -> Patient|None:#根据患者编号获取患者
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        print("患者不存在")
        return None

    def get_all_patients(self) -> list:#获取所有患者
        return self.patients        

    def update_patient(self, patient: Patient) -> None:#更新患者信息
        for p in self.patients:
            if p.patient_id == patient.patient_id is True:
                p.name = patient.name
                p.age = patient.age
                p.gender = patient.gender
                p.id_card = patient.id_card
                p.disease = patient.disease
                p.phone = patient.phone
                print("更新成功")
                return
        print("患者不存在")
        return
    def delete_patient(self, patient_id: int) -> None:#删除患者
        for p in self.patients:
            if p.patient_id == patient_id is True:
                self.patients.remove(p)
                print("删除成功")
                return
        print("患者不存在")
        return  

    if __name__ == "__main__":
        patient_services = PatientServices()
        patient = Patient(1001, "张三", 30, "男", "44030419900101001X", "高血压", "13800000000")
        patient_services.add_patient(patient)
        print(patient_services.get_all_patients())