import add as a 
import sub as s 
import multiply as m 
import divide as d
try :
    n1 = int(input("Enter 1st number:"))
    n2 = int(input("Enter 2nd number:"))
    x = input("Enter operand(+,-,*,/):")
    if x == "+":
        a.sum(n1,n2)
    elif x == "-":
        s.sub(n1,n2)
    elif x == "*":
        m.pro(n1,n2)
    elif x == "/":
        d.div(n1,n2)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Invalid value is given")
except TypeError:
    print("Wrong type of input given")                
