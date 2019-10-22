Python 2.5.4 (r254:67916, Dec 23 2008, 15:19:34) [MSC v.1400 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.4      
>>> import math

def ecuacion():

    print("Calculadora de polinomios")
    print("*************************")
    print("")
    print("Ax^2 + Bx + C = 0")
    
    num1 = input("A: ")
    num2 = input("B: ")
    num3 = input("C: ")

    sum = num2**2 - 4*num1*num3

    if(sum >= 0):
        
        result1 = (-num2 + math.sqrt(num2**2 - 4*num1*num3)) / 2*num1
        result2 = (-num2 - math.sqrt(num2**2 - 4*num1*num3)) / 2*num1

        rst1=str(result1)
        rst2=str(result2)

        print("La respuestas son " + rst1 +" y " + rst2 + ".")
    else:
        print("No se puede")
    
ecuacion()

>>> ================================ RESTART ================================
