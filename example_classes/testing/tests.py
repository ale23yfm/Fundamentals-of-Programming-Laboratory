from domain.student import Student


class Test:
    def __init__(self):
        pass

    def test_create_student(self):
        print("test_create_student")
        id_student = 23
        name = "Jordan"
        value = 9000.1
        epsilon = 0.0001
        student = Student(id_student,name,value)
        assert id_student == student.id_student
        assert name == student.name
        assert abs(value - student.value)<epsilon
        name = "MJ"
        value = 9000.2
        student.name = name
        student.value = value
        assert abs(value - student.value)<epsilon
        print("successful test_create_student")