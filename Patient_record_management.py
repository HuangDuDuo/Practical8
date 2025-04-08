class Patients:
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name=name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
    def print_details(self):
        print(f'Name: {self.name}, Age: {self.age}, Date of latest admission: {self.date_of_latest_admission}, Medical history: {self.medical_history}')
patient01=Patients(name="example_name",age="example_age",date_of_latest_admission="example_date",medical_history="example_history")
print ("Patient Record:")
patient01.print_details()
