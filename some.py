

def calculate_total_marks(marks):
	"""Return the total marks obtained by the student."""
	return sum(marks)


def calculate_percentage(total_marks, number_of_subjects, marks_per_subject=100):
	"""Return the student's percentage."""
	maximum_marks = number_of_subjects * marks_per_subject
	return (total_marks / maximum_marks) * 100 if maximum_marks else 0


def assign_grade(percentage):
	"""Return a grade based on the percentage."""
	if percentage >= 90:
		return "A+"
	if percentage >= 80:
		return "A"
	if percentage >= 70:
		return "B"
	if percentage >= 60:
		return "C"
	if percentage >= 50:
		return "D"
	return "F"


def display_result(name, marks):
	"""Calculate and display the student's result."""
	total_marks = calculate_total_marks(marks)
	percentage = calculate_percentage(total_marks, len(marks))
	grade = assign_grade(percentage)

	print(f"\nStudent: {name}")
	print(f"Total Marks: {total_marks}/{len(marks) * 100}")
	print(f"Percentage: {percentage:.2f}%")
	print(f"Grade: {grade}")


def main():
	name = input("Enter student name: ")
	number_of_subjects = int(input("Enter number of subjects: "))
	marks = [
		float(input(f"Enter marks for subject {subject}: "))
		for subject in range(1, number_of_subjects + 1)
	]
	display_result(name, marks)


if __name__ == "__main__":
	main()
