def display_student(studentdata):
    print("-" * 100)
    print(" " * 30 + "................. Student Data .................")
    print("-" * 100)

    if not studentdata:
        print("                       NO data availabe here ")
        print("-" * 100)
        return

    for student in studentdata:
        for key, value in student.items():
            if key == "qualification":
                print(f"{key}:")
                for i in value:
                    print("    ", i)
            else:
                print(f"{key}: {value}")
        print("-" * 100)
    return studentdata
