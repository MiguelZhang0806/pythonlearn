height = float(input("请输入您的身高【单位是米】"))
weight = float(input("请输入您的体重【公斤】"))

BMI = weight/height**2

print(BMI)

if BMI < 18.5:
    print("偏瘦")
elif BMI > 18.5 and BMI < 24:
    print("正常")
elif BMI > 24 and BMI < 28:
    print("超重")
else:
    print("肥胖")