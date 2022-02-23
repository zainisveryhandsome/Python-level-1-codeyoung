import add
import sub
import mul
import div
print("Welcome to the 2d shape calculator!")
choice=int(input("Enter 1 for a square\n2 for a circle\n3 for a triangle\n4 for a rectangle\n"))
if(choice==1):
    a1=int(input("Enter the first value\n"))
    ab=add.addtwonos(a1,a1)
    ac=add.addtwonos(ab,ab)
    ad=mul.multwonos(a1,a1)
    print("\nPerimeter is",ac,"\nArea is",ad)
elif(choice==2):
    b1=int(input("Enter the radius:"))
    aa=mul.multwonos(b1,2)
    ab=mul.multwonos(aa,3.14159265359)
    ac=mul.multwonos(b1,b1)
    ad=mul.multwonos(ac,3.14159265359)
    print("Circumference is",ab,"\nArea is",ad)
elif(choice==3):
    c1=int(input("Enter the height:"))
    c2=int(input("Enter the base length:"))
    c3=int(input("Enter the hypotenuse length:"))
    aa=mul.multwonos(c1,c2)
    ab=div.divtwonos(aa,2)
    ac=add.addtwonos(c1,c2)
    ad=add.addtwonos(ac,c3)
    print("Perimeter is",ad,"Area is",ab)
elif(choice==4):
    a1=int(input("Enter the first value\n"))
    b1=int(input("Enter the second value\n"))
    aa=add.addtwonos(a1,b1)
    ab=add.addtwonos(a1,b1)
    ac=add.addtwonos(aa,ab)
    ad=mul.multwonos(a1,b1)
    print("\nPerimeter is",ac,"\nArea is",ad)
else:
    print("Please enter one of the following numbers and try again.")
           

        
    
