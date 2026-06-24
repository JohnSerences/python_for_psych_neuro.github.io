class MyMath():
    
    def multiply(self, num1, num2):
        return num1 * num2
        
    def minus(self, num1, num2):
        return num1 - num2
    
    def add(self, num1, num2):
        return num1 + num2
    
    def divide(self, num1, num2):
        return num1 / num2 
    
    # of course we have a built-in ** operator 
    # to do this, but see how we can call another 
    # method in this class using self...
    def square(self, num1):
        return self.multiply(num1, num1)
