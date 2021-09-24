from school_schedule.student import Student

def test_student_class_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.name == "Trenisha"

def test_add_class_method_adds_correct_class_name():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  class_name = "English"

  student.add_class(class_name)

  assert student.classes == ["Calculus", "Choir", "Photography", "AP History", "English"]
