class Report_card:
    def __init__(self, Name, Class, Roll_number, Marks):
        self.Name = Name
        self.Class = Class
        self.Roll_number = Roll_number
        self.Marks = Marks
        
    def show_detail(self):
        print(f"Name: {self.Name}")
        print(f"Class: {self.Class}")
        print(f"Roll_number: {self.Roll_number}")
        print(f"Subject and Marks")
        
        for Subject, Marks in self.Marks.items():
            print(f"{Subject}: {Marks}")
            
    def Average_marks(self):
        Total = sum(self.Marks.values())
        Subjects = len(self.Marks)
        return Total / Subjects
        
    def Get_grade(self):
        Average = self.Average_marks()
        
        if Average >= 90:
            return "Grade: A"
            
        elif Average >= 80:
            return "Grade: B"
            
        elif Average >= 70:
            return "Grade: C"
            
        elif Average >= 60:
            return "Grade: D"
            
        elif Average >= 50:
            return "Grade: E"
            
        elif Average >= 40:
            return "Grade: F"
            
        else:
            return "Fail !"
            
    def Add_subject(self, subject, marks):
        self.Marks[subject] = marks
        print(f"{subject} Subject added")
        
    def Remove_subject(self, subject):
        if subject in self.Marks:
            del self.Marks[subject]
            print(f"{subject} removed !")
            
        else:
            print(f"{subject} not found !")                                    

student = Report_card("Alice", 12, 107, {"Maths": 89, "Science": 55, "Computer": 75} )

student.show_detail()
print(student.Average_marks())
student.Add_subject("Art", 40)
student.Remove_subject("Science")
student.show_detail()
print(student.Get_grade())                             
            
            
                                          
                                          
        
    