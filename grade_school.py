class School:

    def __init__(self):
        self.students: list[tuple(str, int)] = []
        self.students_added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        for name_added in self.students:
            if name == name_added[0]:
                self.students_added.append(False)
                return
        self.students.append((name, grade))
        self.students_added.append(True)

    def roster(self):
        if self.students == []:
            return []
        grades = [grade[1] for grade in self.students]
        grades = list(set(grades))
        students = []
        for grade in grades:
            names = [name[0] for name in self.students if name[1] == grade]
            names = sorted(names)
            for name in names:
                students.append(name)
        return students

    def grade(self, grade_number):
        names = []
        for index, value in enumerate(self.students):
            if value[1] == grade_number:
                names.append(self.students[index][0])
        names = sorted(names)
        return names

    def added(self):
        return self.students_added


if __name__ == "__main__":
    school = School()
    # school.add_student(name="Peter", grade=2)
    # school.add_student(name="Anna", grade=1)
    # school.add_student(name="Barb", grade=1)
    # school.add_student(name="Zoe", grade=2)
    # school.add_student(name="Alex", grade=2)
    # school.add_student(name="Jim", grade=3)
    # school.add_student(name="Charlie", grade=1)
    # print(school.roster())
    # school.add_student(name="Blair", grade=2)
    # school.add_student(name="James", grade=2)
    # school.add_student(name="James", grade=2)
    # school.add_student(name="Paul", grade=2)
    # print(school.added())

    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    print(school.grade(2))
