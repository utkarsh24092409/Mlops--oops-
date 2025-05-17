
#simple inheretiance example 


class Collage:

    def __init__(self,name):
        self.name= name


    def name_of_collage(self):
        print(f"{self.name} is studting in the college ")


    
class student(Collage):

    def student_info(self):
        print(f"hello i am a student of Pccoe and my name is {self.name}")



college  = Collage("rahul")
college.name_of_collage()

stident_information = student("utkarshs")
stident_information.student_info()



    
