from abc import ABC,abstractmethod
class Associates:
    count=0
    def __init__(self,etype="",aname="", mob=None, email=""):
        print("in Associates constructor")
        Associates.count=Associates.count+1
        self.__id=etype+str(Associates.count)
        self.__name=aname
        self.__email=email
        self.__mobile=mob
        
   
     #setter methods
    def set_pid(self,id):
        self.__id=id
        
    def set_aname(self,aname):
        self.__aname=aname
        
    def set_mobile(self,mob):
        self.__mobile=mob
        
    def set_email(self,email):
        self.__email=email
     
    #getter methods
    def get_pid(self):
        return self.__id
    
    def get_pname(self):
        return self.__aname
    
    def get_mobile(self):
         return self.__mobile
    
    def get_email(self):
        return self.__email
        
    def __str__(self):
        print("In Associates str method")
        return f"Id: {self.__id} Name: {self.__name} email:{self.__email} Mobile:{self.__mobile} \n"

class Vendor(Associates,ABC):
    def __init__(self, etype="",email="",aname="", product=[], mob=""):
        super().__init__("v",aname, email, mob)
        self.__product=product
        
    #setter method
    def set_credit_class(self,product):
        self.__product=product
    def set_mobile(self,mobile):
        self.__mobile=mobile
        

    #getter method
    def get_product(self):
         return self.__product
    
        
    def __str__(self):
        return super().__str__()+f"product: {self.__product}"


class Customer(Associates,ABC):
    def __init__(self, ctype="", aname="",email="", mob=None,credit_class=""):
        super().__init__("c",aname, email, mob)
        self.__credit_class=credit_class
        self.__ctype=ctype
        
    #setter method
    def set_ctype(self,ctype):
        self.__ctype=ctype
        
    def set_credit_class(self,credit_class):
        self.__credit_class=credit_class
        

    #getter method
    def get_credit_class(self):
         return self.__credit_class
    def get_ctype(self):
         return self.__ctype
     
      
        
    def __str__(self):
        return super().__str__()+f"credit_class: {self.__credit_class} Ctype={self.__ctype}\n"
    
class Individual(Customer):
    def __init__(self,ctype="",aname="",email="",mob="",credit_class=""):
        super().__init__("i",aname,email,mob,credit_class)
        
        
    #setter methods
    
    
    #getter method
    def get_mobile(self):
        return self.__mobile
     
    def __str__(self):
         return super().__str__()
    
    
        
class Company(Customer):
    def __init__(self, ctype="",aname="",email="",mob=[],credit_class="",relation_manager="",credit_line=0,extensions=-1):
        super().__init__("com",aname,email,mob,credit_class)
        self.__relation_manager=relation_manager
        self.__credit_line=credit_line
        self.__extensions=extensions
        
    #setter methods
    def set_relation_manager(self,relation_manager):
        self.__relation_manager=relation_manager
    def set_credit_line(self,credit_line):
        self.__credit_line=credit_line
    def set_extensions(self,extensions):
        self.__extensions=extensions
        
    def set_mobile(self,mob):
        self.__mobile=mob
     #getter method
    def get_relation_manager(self):
         return self.__relation_manager
    def get_credit_line(self):
         return self.__credit_line
    def get_extensions(self):
         return self.__extensions
    def get_mobile(self):
        return self.__mobile
    
    def __str__(self):
         return super().__str__()+f"relation_manager: {self.__relation_manager} credit_line: {self.__credit_line} extensions: {self.__extensions}" 
    
        
if __name__=="__main__": 
    i=Individual("i","Kishor","9876543210","sj@ex.com","A")
    c=Company("c","Kishor ltd",["9876543210","9876543211"],"sj@ex.com","A", "Kishor", 100000, 3)
    print(c)
    print("#"*69)
    print(i)
            
     