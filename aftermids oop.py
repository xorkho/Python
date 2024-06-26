# ---------------------------------------------DATE 27-MAY-------------------------------------------------
# ASSOCIATION IN CLASS EXERCISE
# CLASS DIAGRAM COPY ME HE

class medical_record:

    def __init__(self,dr_name,diagnosis,medication,date_of_visit):
        self.dr_name=dr_name
        self.diagnosis=diagnosis
        self.medication=medication
        self.date_of_visit=date_of_visit
    
    def print_medical_record(self):
        print(f"DR NAME IS {self.dr_name}\nPATIENT DIAGNOSIS IS {self.diagnosis}\n MEDICATION {self.medication}\n DATE OF VISIT IS {self.date_of_visit}")

class patient:

    def __init__(self,patient_id,patient_name):
        self.patient_id=patient_id
        self.patient_name=patient_name
        self.medical_records=[]

    def add_medical_record(self,dr_name,diagnosis,medication,date_of_visit):
        mr=medical_record(dr_name,diagnosis,medication,date_of_visit)
        self.medical_records.append(mr)
    
    def list_of_medical_record(self):
        print(f"Medical Record {self.patient_name}")
        for item in self.medical_records:
            item.print_medical_record()
   
class doctor:

    def __init__(self,dr_id,dr_name):
        self.dr_id=dr_id
        self.dr_name=dr_name
        self.patient_list=[]

    def add_patient(self,patient_name):
        self.patient_list.append(patient_name)

    def list_of_patient(self):
        print(f"patient of DR {self.dr_name}")
        for i in self.patient_list:
            print(i.patient_name)


class department:

    def __init__(self,dept_id,dept_name):
        self.dept_id=dept_id
        self.dept_name=dept_name
        self.doctors=[]
    
    def add_doctors(self,dr_name):
        self.doctors.append(dr_name)    #drname is an instance of doctor class 

    def list_of_doctors(self):
        print(f"Doctors in {self.dept_name}")
        for i in self.doctors:
            print(i.dr_name)

class Hospital:

    def __init__(self,name):
        self.hospital_name=name
        self.departments=[]

    def add_department(self,dept_id,dept_name):
        dept=department(dept_id,dept_name)
        self.departments.append(dept)

    def list_of_department(self):
        print(f"Department in {self.hospital_name} is:")
        for i in self.departments:
            print(i.dept_name) 