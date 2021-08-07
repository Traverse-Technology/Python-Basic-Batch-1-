mark= int(input("Enter your mark: "))
 
if mark > 0 and mark <40:
    print("F")
elif mark >= 40 and mark < 80:
    if mark < 60:
        print("P-")
    else:
        print("P+")
elif mark >= 80 and mark <=100:
    print("D")
else:
    print("Invalid")
    