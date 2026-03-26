class  Utils:
    def __init__(self,numbers=None, text="" , password=""):
        self.numbers = numbers
        self.text = text
        self.password =password
    
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b
    
    def divide(self,a,b):
        if b ==  0:
            return "Undefined"
        else:
            return a/b
        
    def is_even(self,num):
        return num % 2 ==0
    
    def  is_odd(self,num):
        return num % 2 != 0
    
    def biggest(self):
        if not self.numbers:
            return None
        big =self.numbers[0]
        for n in self.numbers:
            if n > big:
                big =n
        return big
    
    def smallest(self):
       if not self.numbers:
           return None
       small =self.numbers[0]
       for n in self.numbers:
           if n < small:
               small = n 
       return small
    
    def reverse_text(self):
        return self.text[::-1]
    
    def is_palindrome(self):
        return self.text == self.text[::-1]
    
    def check_password(self):
       if len(self.password) >= 8:
           return "Strong"
       else:
           return "Weak"
utils = Utils(numbers=[6,7,8,3,10,15], text="madam", password="Sayat3625")




         
            
