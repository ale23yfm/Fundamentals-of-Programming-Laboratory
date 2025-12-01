from errors.exceptions import ValidationError


class StudentValidator:

    def validate_student(self,student):
        errors = ""
        if student.id_student<0:
            errors += "Student ID must be greater than or equal to 0.\n"
        if student.name == "":
            errors += "Student name cannot be empty.\n"
        if student.value <= 0.0:
            errors += "Student value must be greater than 0.\n"
        if len(errors)>0:
            raise ValidationError(errors)