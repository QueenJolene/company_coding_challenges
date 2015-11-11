import sys

class Registration():
	def __init__(self):
		self.classes = []
		self.students = []

class Class_room():
	def __init__(self, class_id, max_cap, time):
		self.id = class_id
		self.max_cap = max_cap
		self.time = time
		self.num_enrolled = 0
		self.students_enrolled = []

class Student():
	def __init__(self, student_id, max_classes, start_time, end_time):
		self.id = student_id
		self.max_classes = max_classes
		self.num_enrolled = 0
		self.start_time = start_time
		self.end_time = end_time
		self.times_available = range(int(start_time), int(end_time)+1)
		self.enrolled_classes = []

def add_class(class_id, max_cap, time):
	new_class = Class_room(class_id, int(max_cap), int(time))
	if school_registration.classes:
		class_object = _find_class(class_id)
		if class_object:
				return "Error adding class " + new_class.id
		else:
			school_registration.classes.append(new_class)
			return "Successfully added class " + new_class.id
	else:
		school_registration.classes.append(new_class)
		return "Successfully added class " + new_class.id

def info_class(class_id):
	if school_registration.classes:
		class_object = _find_class(class_id)
		if class_object:
			student_list = sorted(class_object.students_enrolled)
			if student_list:
				return "Class %s has the folloiwng students %s" % (class_id, str(" ".join(student_list)))
			else:
				return "Class " + class_id + " is empty."
		else:
			return "Class " + class_id + " does not exist"
	else:
		return "Class " + class_id + " does not exist"

def remove_class(class_id):
	if school_registration.classes:
		class_object = _find_class(class_id)
		if class_object.id == class_id:
			for student_id in class_object.students_enrolled:
				student_object = _find_student(student_id)
				if student_object:
					student_object.enrolled_classes.remove(class_id)
					student_object.num_enrolled -= 1
					student_object.times_available.append(class_object.time)
			class_object.students_enrolled = []
			school_registration.classes.remove(class_object)
			return "Successfully removed class " + class_id

		else: 
			print "class not found"
			return "Error removing class " + class_id

	else:
		return "Error removing class " + class_id

def add_student(student_id, max_classes, start_time, end_time):
	new_student = Student(student_id, int(max_classes), int(start_time), int(end_time))
	if school_registration.students:
		student_object = _find_student(student_id)
		if student.id == new_student.id:
			return "Error adding student " + new_student.id
		else:
			school_registration.students.append(new_student)
			return "Successfully added student " + new_student.id
	
	else:
		school_registration.students.append(new_student)
		return "Successfully added student " + new_student.id

def enroll_student(student_id, class_id):
	student_object = _find_student(student_id)
	if student_object:
		student_exists = True
		student_has_capacity = True if student_object.max_classes - student_object.num_enrolled > 0 else False
		student_times_available = student_object.times_available
		student_not_taking_class = True if class_id not in student_object.enrolled_classes else False
		
	class_object = _find_class(class_id)
	if class_object:
		class_exists = True  
		class_has_capacity = True if class_object.max_cap - class_object.num_enrolled > 0 else False
		class_room_time = class_object.time
	
	if class_object and student_object:
		student_can_take_class = True if class_room_time in student_times_available else False

		if (student_exists, student_has_capacity, class_exists, 
			class_has_capacity, student_can_take_class, student_not_taking_class) == (True, True, True, True, True, True):
			student_object.num_enrolled += 1
			student_object.enrolled_classes.append(class_id)
			student_object.times_available.remove(class_room_time)
			class_object.num_enrolled += 1
			class_object.students_enrolled.append(student_id)
			return "Number of free spots left in class " + class_id +": " + str(class_object.max_cap - class_object.num_enrolled)

		else:
			return "Enrollment of student %s in class %s failed." % (student_id, class_id)
	else:
		return "Enrollment of student %s in class %s failed." % (student_id, class_id)

def unenroll_student(student_id, class_id):
	student_exists, student_enrolled, class_exists = (False, False, False)
	for student in school_registration.students:
		student_object = _find_student(student_id)
		if student_object:
			student_exists = True
			student_enrolled = True if class_id in student.enrolled_classes else False

	for class_room in school_registration.classes:
		class_object = _find_class(class_id)
		if class_object:
			class_exists = True 

	if (student_exists, student_enrolled, class_exists) == (True, True, True):
		student_object.num_enrolled -= 1
		student_object.enrolled_classes.remove(class_id)
		student_object.times_available.append(class_object.time)
		class_object.num_enrolled -= 1
		class_object.students_enrolled.remove(student_id)
		return "Number of free spots left in class " + class_id +": " + str(class_object.max_cap - class_object.num_enrolled)
	else:
		return "Unenrollement of student %s in class %s failed." % (student_id, class_id)

def info_student(student_id):
	student_object = _find_student(student_id)
	if student_object:
		if student_object.num_enrolled > 0:
			return "Student " + student_id + " is taking the following classes " + ", ".join(student_object.enrolled_classes)
		else:
			return "Student %s is not taking any classes" % student_id

def remove_student(student_id):
	if school_registration.students:
		student_object = _find_student(student_id)
		if student_object:
			for class_id in student_object.enrolled_classes:
				unenroll_student(student_id, class_id)
			school_registration.students.remove(student_object)
			return "Successfully removed student %s" % student_id
			
		else:
			return "Error removing student %s" % student_id
	else:
		return "Error removing student %s" % student_id

#helper functions

def _find_class(class_id):
	for class_object in school_registration.classes:
		if class_object.id == class_id:
			return class_object

def _find_student(student_id):
	for student in school_registration.students:
		if student.id == student_id:
			return student

def process_command(command_list):
	command = command_list[0]
	if command == "ADDCLASS":
		class_id, max_cap, time = command_list[1:]
		print add_class(class_id, max_cap, time)
		
	if command == "INFOCLASS":
		class_id = command_list[1]
		print info_class(class_id)

	if command == "REMOVECLASS":
		class_id = command_list[1]
		print remove_class(class_id)

	if command == "ADDSTUDENT":
		#start and end times are inclusive
		student_id, max_classes, start_time, end_time = command_list[1:]
		print add_student(student_id, max_classes, start_time, end_time)

	if command == "REMOVESTUDENT":
		student_id = command_list[1]
		print remove_student(student_id)

	if command == "ENROLLSTUDENT":
		student_id, class_id = command_list[1:]
		print enroll_student(student_id, class_id)

	if command == "INFOSTUDENT":
		student_id = command_list[1]
		print info_student(student_id)

	if command == "UNENROLLSTUDENT":
		student_id, class_id = command_list[1:]
		print unenroll_student(student_id, class_id)

if __name__ == '__main__':

	school_registration = Registration()

	command_input = sys.stdin.readlines()
	while command_input:
		clean_data = command_input.pop(0).strip()
		command = clean_data.split(" ")
		process_command(command)



