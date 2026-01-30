monday_class = {"Alice", "Bob", "Charlie", "David"}
wednesday_class = {"Charlie", "David", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}")
print(f"Attended either classes: {monday_class | wednesday_class}")
print(f"Only Monday class: {monday_class - wednesday_class}")
print(f"Only One class: {monday_class ^ wednesday_class}")
allStudents = monday_class | wednesday_class
print("Is Monday subset of all students?", monday_class <= allStudents )
