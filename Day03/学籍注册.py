
db_file = "student_data.db"

def validated_phone(num):
    if num.isdigit():
        exit("手机号必须输入数字")
    if len(num) != 11:
        exit("手机号必须输入11位")
    return True
def register_api():
    stu_data = {}
    print("欢迎".center(50,"-"))
    print("请完成学籍注册")
    name = input("姓名:").strip()
    age = input("年龄：").strip()
    phone = input("手机号：").strip()
    if phone in phone_list:
        exit("该手机以注册")
    validated_phone(phone)
    id_num = input("身份证号：").strip()
    if id_num in id_num_list:
        exit("该身份证号以注册")
    course_list = ["Python开发","Linux云计算","网络安全","数据分析&机器学习","前端开发"]

    for index,course in enumerate(course_list):
        print(f"{index}.{course}")

    select_course = input("选择想学的课：")
    if select_course.isdigit():
        select_course = int(select_course)
        if select_course >= 0 and select_course < len(course_list):
            picked_course = course_list[select_course]
        else:
            exit("不合法的选项。。。")
    else:
        exit("非法输入")

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["id_num"] = id_num
    stu_data["course"] = picked_course

    return stu_data

def commit_to_db(filename,stu_data):
    f = open(filename,"a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}"
    f.write(row)
    f.close()

def load_validated_data(filename):
    f = open(filename)
    phone_list = []
    id_num_list = []
    for line in f:
        line = line.split(",")
        phone = line[2]
        id_num = line[3]
        phone_list = list.append(phone)
        id_num_list = list.append(id_num)

    return phone_list,id_num_list

phone_list,id_num_list = load_validated_data(db_file)

student_data = register_api()
print(student_data)

commit_to_db(db_file,student_data)