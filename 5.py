student={"Alice":85,"Bob":90,"Charlie":78,"David":92,"Eve":88,"John":80,"Emily":95,"Sarah":89,"Daniel":91}
name=input("Enter the student's name:")
if name in student:
    print(f"{name}'s marks: {student[name]}")
else:
    print("student not found")