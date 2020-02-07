
def User_Data(_name,_age,_work,_skills,_degree,_salary):
    user_dict = {"Name"   : _name,
                 "Age"    : _age,
                 "work"   : _work,
                 "Skills" : _skills,
                 "Degree" : _degree,
                 "Salary" : _salary
                 }
    return user_dict

listes = []

u1 = User_Data("waqas",23,"Developer","Pythanist","BSCS",80000)
u2 = User_Data("hammad",22,"Developer","Pythanist","BSCS",60000)
u3 = User_Data("Shahzaib",24,"Developer","Pythanist","BSCS",90000)

listes.append(u1)
listes.append(u2)
listes.append(u3)

print(listes)