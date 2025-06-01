r = float(input("Enter your radius of your circle right here :"))
circumference = (math.pi *r )  
area_of_circle = math.pi * pow(r , 2 ) # pow คือการยกกำลัง
print(f"circumference of your circle is {round(circumference , 3 )} cm.") # , 3 คือการปัดทศนิยมให้เหลือ 3 ตำแหน่ง 
print(f"area of your circle is {round(area_of_circle , 3 )} cm^2.")
