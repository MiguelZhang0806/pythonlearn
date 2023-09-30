pid = input("请输入您的身份证号：")

if len(pid) == 18:
    print("打印个人信息")
    num = int(pid[17])
    if num % 2 == 0:
        print("性别:女性")
    else:
        print("性别:男性")
    jiGuanCode = pid[:6]
    print("jiGuanCode",jiGuanCode)
    if jiGuanCode == "100000":
        print("籍贯：北京")
    elif jiGuanCode == "120000":
        print("籍贯：天津")
    elif jiGuanCode == "310000":
        print("籍贯：上海")
    elif jiGuanCode == "50000":
        print("籍贯：重庆")
    else:
        print("不是直辖市")
else:
    print("输入位数有误！")
print("程序结束")