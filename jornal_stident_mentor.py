import statistics


class GraderMixin:
    def middle_score(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return statistics.mean(all_grades)
        return 0


class Student (GraderMixin):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and ((course in
                                              lecture.courses_attached)
                                              and (course in
                                                   self.courses_in_progress)):
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.middle_score() < other.middle_score()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.middle_score() <= other.middle_score()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.middle_score() > other.middle_score()

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.middle_score() >= other.middle_score()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.middle_score() == other.middle_score()

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.middle_score() != other.middle_score()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.middle_score()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, GraderMixin):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() < other.middle_score()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() <= other.middle_score()

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() > other.middle_score()

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() >= other.middle_score()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() == other.middle_score()

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_score() != other.middle_score()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.middle_score()}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in
                                             student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return statistics.mean(total_grades)
    return 0


def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return statistics.mean(total_grades)
    return 0


best_student = Student('Adam', 'Red', 'boy')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в програмирование']

another_student = Student('Alice', 'Brown', 'girl')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Kate', 'Green')

lecture_1 = Lecturer('Den', 'Black')
lecture_1.courses_attached += ['Python', 'Git', 'Введение в програмирование']

lecture_2 = Lecturer('Mike', 'White')
lecture_2.courses_attached += ['Python', 'Введение в програмирование']

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Git', 9)
reviewer_1.rate_hw(best_student, 'Python', 10)

reviewer_1.rate_hw(another_student, 'Python', 9)
reviewer_1.rate_hw(another_student, 'Python', 8)

best_student.rate_lecturer(lecture_1, 'Python', 10)
best_student.rate_lecturer(lecture_1, 'Git', 9)
best_student.rate_lecturer(lecture_1, 'Введение в програмирование', 10)

another_student.rate_lecturer(lecture_2, 'Python', 8)
another_student.rate_lecturer(lecture_2, 'Введение в програмирование', 8)

print(best_student)
print(another_student)
print(reviewer_1)
print(lecture_1)
print(lecture_2)

# Подсчет средней оценки за домашние задания по всем студентам в рамках курса
students_list = [best_student, another_student]
average_hw_grade_python = average_student_grade(students_list, 'Python')
print(f'Средняя оценка за домашние задания по курсу '
      f'Python: {average_hw_grade_python}')

# Подсчет средней оценки за лекции всех лекторов в рамках курса
lecturers_list = [lecture_1, lecture_2]
average_lecture_grade_python = average_lecturer_grade(lecturers_list, 'Python')
print(f'Средняя оценка за лекции по курсу '
      f'Python: {average_lecture_grade_python}')
