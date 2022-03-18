#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# הגדול מבין 2 מספרים
from urllib.parse import MAX_CACHE_SIZE


def max2(a,b):
    if a > b:
        return a
    else:
        return b
  
#print(max2(5,6))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#הגדול מבין 3 מספרים
def max3(a,b,c):
   max_a_b = max2(a,b) #
   #המשתנה מקס אייבי מקבל את הגבוה מבין 2 מספרים- שהוא התוצאה של הפונקציה לעיל
   # שימוש בפונקציה שממיינת את הגדול מבין 2 מספרים
   max_all = max2(max_a_b,c)#
   #מיון בין התוצאה הגבוהה מבין 2 המספרים הראשונים - יחד עם השלישי
   # שימוש נוסף בפונקציה שממיינת את הגדול מבין 2 מספרים
   return max_all
  
# print(max3(5,60,7))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#הגדול מבין 4 מספרים
#קריאה לפונקציה מתןך פונקציה
#הכנתי 2 פונקציות:הראשונה ממיינת מספר גבוה מתוך 2 מספרים
#והשניה ממיינת מספר גבוה מתוך 3 מספרים
#כדי למצוא גבוה מתוך 4 מספרים ניתן לשלב
#שילוב של מיון 3 עם מיון 2
#גירסה ראשונה
def max4(a,b,c,d):
    max_a_b_c = max3(a,b,c)
    max_all = max2(max_a_b_c,d)
    return max_all

# print(max4(1,2,37,4))

#מיון 2 שלש פעמים:בין הראשון לשני
#בין השלישי לרביעי
#בין הגבוהים של 2 הקבוצות
#גירסה שניה
def max_4(a,b,c,d):
    max_a_b = max2(a,b)
    max_c_d = max2(c,d)
    max_all = max2(max_a_b,max_c_d)
    return(max_all)
# print(max_4(1,2,3,4))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#הגדול מבין 5 מספרים
#מיון 2 ארבע פעמים:בין הראשון לשני
#בין השלישי לרביעי,בין 2 הגבוהים מבין 2 הזוגות
#ופעם אחרונה בין הגבוהה ברביעייה הראשונה לבין המספר החמישי
def max5(a,b,c,d,e):
    max_a_b = max2(a,b)
    max_c_d = max2(c,d)
    max_a_b_c_d = max2(max_a_b,max_c_d)
    max_all = max2(max_a_b_c_d,e)
    return max_all
# print (max5(1,2,3,4,5))

#מיון 3 בין הראשון לשני לשלישי
#מיון 2 בין הרביעי והחמישי
# מיון 2 הגבוהים מבין 2 הקבוצות
#
def max_5(a,b,c,d,e):
    max_a_b_c = max3(a,b,c)
    max_d_e = max2(d,e)
    max_all = max2(max_a_b_c,max_d_e)
    return max_all
# print(max_5(1,22,3,4,5))

#מיון 4 בין הראשון לשני לשלישי לרביעי
# מיון 2 החמישי לבין הגבוה מהקבוצה הראשונה
def max__5(a,b,c,d,e):
    max_a_b_c_d = max4(a,b,c,d)
    max_all = max2(max_a_b_c_d,e)
    return max_all
# print(max__5(1,22,3,4,5))


def max10(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    max_first5 = max_5(a1,a2,a3,a4,a5)
    max_last5 = max_5(a6,a7,a8,a9,a10)
    max_all = max2(max_first5,max_last5)
    return max_all
print(max10(3,2,4,0,51,7,8,9,10,20))  











# def max2(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
 
# res = max2(5, 7)
# print(res)

# def max_4(a,b,c,d):
#     MAX = max(a,b,c,d)
#     return MAX
# res = max_4(59,30,6,2)
# print("\nThe LARGEST Number is : ",res)