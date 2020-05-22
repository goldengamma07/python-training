class Employee:
    def __init__(self,name,empid,peradd,curadd,mobno,blood_grp,pan_no,pf_ac_no,father_name):
        self.name = name
        self.employee_id = empid
        self.permanent_address = peradd
        self.current_address = curadd
        if len(mobno)==10:
            self.mobile_no = mobno
        else: 
            raise "invalid mobile numer"
        self.blood_group = blood_grp
        self.pan_no = pan_no
        self.pf_account_no = pf_ac_no
        self.fathers_name = father_name

    def get_info(self,empid):
        return{"name":self.name,"permanent address":self.permanent_address,"current address":self.current_address,"mobile no.":self.mobile_no,\
            "blood group":self.blood_group,"pan number:":self.pan_no,"pf account number:":self.pf_account_no,"fathers name:":self.fathers_name}

    def change_address(self, new_address):
        self.current_address = new_address
    
employee1 = Employee("Ganesh shyam",7777777777,"kalpakkam","chennai","98763210","o+ve",1212121212,3434343434,"mohandas")
employee2 = Employee("arumaiprakasam",8888888888,"gopichettypaalayam","coimbatore","1234567890","o-ve",2121212121,4343434343,"nambikkai kannan")

employee1.change_address("koramangala")
print(employee1.get_info(7777777777))


print(employee2.get_info(8888888888))