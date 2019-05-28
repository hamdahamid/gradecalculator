#Grade Calculater For 9th Class
chemistry = int(input("Enter Chemistry marks between the range of 0 and 100 : "))
biology = int(input("Enter Biology marks between the range of 0 and 100 : "))
english = int(input("Enter English marks between the range of 0 and 75 : "))
pakstudies = int(input("Enter Pakistan Studies marks between the range of 0 and 75 : "))
sindhi = int(input("Enter Sindhi marks between the range of 0 and 75 : "))
obt_marks = chemistry + biology + english + pakstudies + sindhi
print("\n" + "Obtained Marks = " + str(obt_marks) + " / 425")
percentage = int((obt_marks / 425) * 100)
print("Percentage = " + str(percentage) + " %")
if percentage >= 80:
    print("Grade = A+")
elif percentage >= 70:
    print("Grade = A")
elif percentage >= 60:
    print("Grade = B")
elif percentage >= 50:
    print("Grade = C")
elif percentage >= 45:
    print("Grade = D")
else:
    print("Grade = Fail")