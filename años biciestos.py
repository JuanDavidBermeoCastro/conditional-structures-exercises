
year= int(input("write one year: "))


if (year%4==0):
    print(f"year {year} is biciesto")
else:
    print(f"no biciesto")


if (year>=1582%400==0):
    
    print(f"is {year} mayor a 1582 is biciesto ")
    
if (year<1582):
 print (f"no aplica a la regla de cada 400 años para saber si es biciesto") 
 
else:
    print(f"este año despues de {year} es no biciesto")
    
  
  