class Student:
    count=0;
    def input(self):
        self.rno=input("Enter Roll no:");
        self.name=input("Enter name:");
        self.c_marks=int(input("Enter c marks:"));
        self.cpp_marks=int(input("Enter cpp marks:"));
        self.python_marks=int(input("Enter python marks:"));
        Student.count=Student.count+1;

    def calc_total(self):
        self.total=self.c_marks+self.cpp_marks+self.python_marks;

    def calc_percentage(self):
        self.percentage=self.total*100/300;

    def calc_grade(self):
        if(self.percentage <99 and self.percentage >=70):
            self.grade='A';
        elif(self.percentage <70 and self.percentage >=60):
            self.grade='B';
        elif(self.percentage <60 and self.percentage >=50):
            self.grade='C';
        elif(self.percentage <50 and self.percentage >=40):
            self.grade='D';
        else:
            self.grade='F';
        
    def show(self):
        print("Roll no: ",self.rno);
        print("Name: ",self.name);
        print("C Marks: ",self.c_marks);
        print("CPP Marks: ",self.cpp_marks);
        print("Python Marks: ",self.python_marks);
        print("Total: ",self.total);
        print("Percentage: ",self.percentage);
        print("Grade: ",self.grade);
s1=Student();
s1.input();
s1.calc_total();
s1.calc_percentage();
s1.calc_grade();
s1.show();

s1=Student();
s1.input();
s1.calc_total();
s1.calc_percentage();
s1.calc_grade();
s1.show();

print("Number of Student: ",Student.count);
