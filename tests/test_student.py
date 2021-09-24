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
  #assert
  assert student.classes == ["Calculus", "Choir", "Photography", "AP History", "English"]

def test_get_num_classes_returns_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  # assert
  assert student.get_num_classes() == 4

def test_summary_method_returns_correct_string():
  samara = Student( "Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] )

  assert samara.summary() == "Samara is a junior enrolled in 6 classes"