
class Employee:
    company="YT"
    salary=2000
    salaryIncreamnt=2
    
    @property
    def salaryAfterIncreament(self):
        return self.salary*self.salaryIncreamnt

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,salaryAfterIncreament):
        self.salaryIncreamnt=salaryAfterIncreament/self.salary

z=Employee()
print(z.salaryAfterIncreament)
z.salaryAfterIncreament=4000
print(z.salaryIncreamnt)

