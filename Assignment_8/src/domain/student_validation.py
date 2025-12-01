from configobj.validate import is_integer

class StudentValidation:
    @staticmethod
    def validate(student):
        error =[]
        if student.id_student < 0 or not(is_integer(student.id_student)):
            error.append("Student ID is invalid. It must be a posivite integer.")
        if student.group < 0 or not(is_integer(student.group)):
            error.append("Student group is invalid. It must be a posivite integer.")
        if len(student.name.strip()) == 0:
            error.append("Name cannot be empty")

        if error:
            raise Exception("\n".join(error))