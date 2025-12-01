from business.service_students import ServiceStudents
from infrastructure.repository_students import RepositoryStudents
from presentation.console import Console
from testing.tests import Test
from validation.student_validator import StudentValidator

test = Test()
test.test_create_student()
student_validator = StudentValidator()
students_repository = RepositoryStudents()
service_students = ServiceStudents(student_validator,students_repository)
console = Console(service_students)
console.run()