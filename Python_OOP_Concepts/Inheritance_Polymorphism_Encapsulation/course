from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration
    @abstractmethod
    def course_details(self):
        pass
class ProgrammingCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Includes coding practice and real-world projects.")
class DesignCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Focuses on UI/UX, graphics, and creative tools.")
class MarketingCourse(Course):
    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Covers digital marketing and branding strategies.")
programming = ProgrammingCourse("Python Programming", "3 Months")
design = DesignCourse("Graphic Design", "2 Months")
marketing = MarketingCourse("Digital Marketing", "4 Months")
courses = [programming, design, marketing]
for course in courses:
    course.course_details()
    print()
