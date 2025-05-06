marks = int(input("Enter your marks: "))

if marks>100:
    print("Uncountable marks!")

if marks<=100 and marks>=80:
    print("Yours great is : A+")
elif marks<80 and marks>=70:
    print("Your great is : A ")
elif marks<60 and marks>=50:
    print("Your great is : B")
elif marks<45 and marks>=40:
    print("Your great is : A-")
elif marks<33 and marks>=0:
    print("Oh your fail")