#הגדול מבין 2 מספרים 
# רק אם הם שונים
#גירסה ראשונה
# a = int(input ("\na = "))
# a = int(input ("b = "))
# if a>b:
#     print(a,">",b)
# else:
#     print(b,">",a)

#הגדול מבין 2 מספרים 
# רק אם הם שונים
#גירסה שניה
# a = int(input ("\na = "))
# b = int(input ("b = "))
# print("The Biggest Numbe is : ",max(a,b))













# #הגדול מבין 3 מספרים
# # רק אם הם שונים
# #גירסה ראשונה
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b: 
#     if a>c:
#         print("   a is the biggest ",a)
#     else:
#         print("   c is the biggest ",c)
# else:
#     if b>c:
#         print("   b is the biggest ",b)
#     else:
#         print("   c is the biggest ",c)
 

#הגדול מבין 3 מספרים
# רק אם הם שונים
#גירסה שניה
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b and a>c:
#     print("   1a is the biggest ",a)    
# if a>b and a<c :
#     print("   c is the biggest ",c)  
# if a<b and b>c:
#     print("   b is the biggest ",b)  
# if a<b and b<c:
#     print("   c is the biggest ",c) 

#הגדול מבין 3 מספרים
# רק אם הם שונים
#גירסה שלישית
# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# print("\nThe Biggest Number is : ",max(a,b,c))            




#הגדול מבין 4 מספרים
# רק אם הם שונים
#גירסה ראשונה

# a = input ("\na = ")
# b = input ("b = ")
# c = input ("c = ")
# d = input ("d = ")

# if a>b and a>c and a>d:
#     print("a is the biggest ",a)    
# if a>b and a>c and a<d:
#     print("d is the biggest ",d)  
# if a>b and a<c and c>d:
#     print("c is the biggest ",c)  
# if a>b and a<c and d>c:
#     print("d is the biggest ",d)  
# if a<b and b>c and b>d:
#     print("b is the biggest ",b)  
# if a<b and b>c and b<d:
#     print("d is the biggest ",d)
# if a<b and b<c and c>d:
#     print("c is the biggest ",c)
# if a<b and b<c and c<d:
#     print("d is the biggest ",d)
 
##הגדול מבין 4 מספרים
#גירסה שניה
# 
# a = int(input ("\na = "))
# b = int(input ("b = "))
# c = int(input ("c = "))
# d = int(input ("d = "))        
        
# if a>b:
#     if a>c:
#         if a>d:
#             print(a)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)
# else:
#     if b>c:
#         if b>d:
#             print(b)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)

#הגדול מבין 4 מספרים
#גירסה שלישית
# a = int(input ("\na = "))
# b = int(input ("b = "))
# c = int(input ("c = "))
# d = int(input ("d = "))
# print("\nThe Biggest Number is : ",max(a,b,c,d)) 
# 
# 
# 
#            
#ממיינת בין 2 מספרים מי גדול יותר גם אם הם שווים

# a = int(input ("a = "))
# b = int(input ("b = "))
# if a>b:
#     print(a,">",b)
# elif a==b:
#     print(a,"=",b)
# else:
#     print(b,">",a)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# משווה יחסית למספר קבוע
# num = int(input(" ?בחר מספר.מהי הבחירה שלך"))      #קלט של מספר מהמשתמש
# x=10                                        # השמת ערך בתא איקס
# if num > x:                                 #אם המספר שהקליד המשתמש גדול מ 10 ... אז
# 	print(num,">",x)                        # פלט-המספר שבחרת גדול מ 10
# elif num < x:                               #אחרת- אם המספר שהקליד המשתמש קטן מ 10 ... אז
# 	print(num,"<",x)                        #פלט-המספר שבחרת קטן מ 10
# else:                                       # אחרת
# 	print(num,"=",x)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # משווה יחסית למספר קבוע
# print("Choose a Number ",)                        # פלט - הודעה
# choice1 = int(input("What is Your Choice?  "))    #קלט של מספר מהמשתמש
# x=10                                              # השמת ערך בתא איקס
# if choice1 > x:                                   #אם המספר שהקליד המשתמש גדול מ 10 ... אז
# 	print("your number is bigger than ",x)         # פלט-המספר שבחרת גדול מ 10
# elif choice1 < x:                                 #אחרת- אם המספר שהקליד המשתמש קטן מ 10 ... אז
# 	print("your number is smaller than ",x)        #פלט-המספר שבחרת קטן מ 10
# else:                                             # אחרת
# 	print("your number is equal to ",x) 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#התכנית תמיין שלשה מספרים רק אם הם שונים
# a = input ("a = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b:
#     if a>c :
#         if b>c:
#             print(" "*5,"a > b > c\n"," "*4,a,">",b,">",c)
#         else:
#             print(" "*5,"a > c > b\n"," "*4,a,">",c,">",b)
#     else:
#         print(" "*5,"c > a > b\n"," "*4,c,">",a,">",b)
# else:
#     if b>c:
#         if a>c:
#            print(" "*5,"b > a > c\n"," "*4,b,">",a,">",c) 
#         else:
#             print(" "*5,"b > c > a\n"," "*4,b,">",c,">",a)
#     else:
#         print(" "*5,"c > b > a\n"," "*4,c,">",b,">",a)        


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#שידרוג ?
# התכנית תמיין שלשה מספרים רק אם הם שונים
# a = input ("a = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b and a>c and b>c:
#     print(" "*5,"a > b > c\n"," "*4,a,">",b,">",c)
# if a>b and a>c and b<c:
#     print(" "*5,"a > c > b\n"," "*4,a,">",c,">",b)
# if a>b and a<c :
#     print(" "*5,"c > a > b\n"," "*4,c,">",a,">",b)
# if b>a and b>c and a>c:
#     print(" "*5,"b > a > c\n"," "*4,b,">",a,">",c)
# if b>c and a<c :
#         print(" "*5,"b > c > a\n"," "*4,b,">",c,">",a)
# if b>a and b<c:
#       print(" "*5,"c > b > a\n"," "*4,c,">",b,">",a)  
 


# # התכנית תבדוק אם שלשה מספרים שווים זה לזה
# a = input ("a = ")
# b = input ("b = ")
# c = input ("c = ")
# if a==b and a==c:
#     print("\n     equal")
# else:
#     print("\n     not equal")

#והתכנית תבדוק אם שלש התוצאות שוות זו לזה
# a = 4*256
# b = 8*128
# c = 16*64
# d = 32*32
# e = 2*512
# if a==b and a==c and a==d and a==e:
#     print("\n     תווש equal")
# else:
#     print("\n     תווש אל not equal")


#בודקת אם תו/אות נמצא בתוך מחרוזת
# name = "moti"
# if "j" in name:
#     print("good")
# else:
#     print("not good")

# a = input("\na = ")
# b = input("b = ")
# c = input("c = ")
# print("\n",sorted([a,b,c]))

