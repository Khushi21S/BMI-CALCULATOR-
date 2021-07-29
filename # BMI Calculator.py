# BMI Calculator
Height=float(input("How tall are u?(in cm): "))
Weight=float(input("How much force earth exerts on u?(in kg): "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your BODY Mass Index is: ",BMI)
if(BMI>0):
        if(BMI<=16):
                print("You are severly underweight,you need to hospitalise!")
        elif(BMI<=18.5):
                print("You are underweight,you need doctor's advise")
        elif(BMI<=25):
                print("Woah,you are fit!")
        elif(BMI<=30):
                print("You are overweight,do some exercise!") 
        else: print("You are severly overweight,high cholestrol,you need to visit doctor")          
else:("enter valid details")        