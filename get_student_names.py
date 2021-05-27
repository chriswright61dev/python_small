# def get_student_names(students):
#     # students is a dictionary
#     student_list = list(students.values())
#     student_list.sort() // returns none of not used on it's own line
#     print(student_list)

def get_student_names(students):
	return sorted(students.values())    

get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
})
