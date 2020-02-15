pi = 3.14
def calcArea(_radiu):
    return pi*_radiu**2

# print(calcArea(8.7))

def checkVal(l,cv):
    for pos,i in  enumerate(l):
        if i == cv :
            return f"The GIven Value {cv} exist in a list at point {pos}"
    return "Not Exixtes!"

data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
# print(checkVal(data,"python"))
# print(checkVal(data,"html"))
# print(checkVal(data,"c"))
# print(checkVal(data,"shahzaib"))


def radius_of_circle():
    while True:
        r = input("Enter radius or write quite to exit : ")
        if r == "quite":
            break
        else: 
            print(calcArea(float(r)))
 
# radius_of_circle()
dict_user = {"name" : "Ali", "class" : "AI","marks" : {"math" : 50, "physics" : 80, "biology" : 90, "computer" : 67}, "date" : "1 Feb 2020", "nextClass" : True }  

def showDetails(**kwags):
    print(f"Hello { kwags['name'] } ")
    print(f"Here is youer result for class of {kwags['class']}")
    print(f"ClassMarks:")
    total = 0
    for k,v in kwags["marks"].items():
        print(f"{k} : {v}")
        total += v 
    print(f"Total marks are: {total}")
    print(f"Percentage is as follows {total/400 * 100}%")
    print(f"Maximum marks are in 'Biology'")
    print("Minimum marks are in 'Math'")
    print("You are promoted to next class.")
 
# showDetails(**dict_user)

def shiftItems (lists, num): 
    output_list = [] 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item])   
    return output_list 
   
print(shiftItems(data,3)) 