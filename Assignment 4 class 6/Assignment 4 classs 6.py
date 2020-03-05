class Circule:
    def __init__(self,raduis,pie= 3.144):
        self.raduis = raduis
        self.pie = pie
    #Find Area By Radius
    def AreaByRadius(self):
        return self.pie * self.raduis**2
    #Find Perimeter By Radius
    def PerimeterByRadius(self):
        return 2*self.pie*self.raduis

class String:
    def __init__(self,string=''):
        self.string = string
    def get_String(self):
        self.string =input("Enter the string :")
    def  print_String(self):
        print(f"The string You Enter Is '{self.string.upper()}'")

class string_Revers:
    def __init__(self,string):
        self.string = string
    def Reverse_string(self):
        return '.'.join(reversed(self.string.split()))

  