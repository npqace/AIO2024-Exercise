# ward class
class Ward:
    def __init__(self, name):
        """
        Initializes a Ward object with a name and an empty list to store people.

        Args:
            name (str): The name of the ward.
        """
        self.name = name
        self._list_of_people = []

    def add_people(self, person):
        """
        Adds a person to the ward's list of people.

        Args:
            person (Person): The person object to be added.
        """
        self._list_of_people.append(person)

    def describe(self):
        """
        Prints information about the ward and all the people in it.
        """
        print(f'Ward name: {self.name}')
        print('People in the ward:')
        for person in self._list_of_people:
            person.describe()

    def count_doctor(self):
        """
        Counts the number of doctors in the ward.

        Returns:
            int: The number of doctors in the ward.
        """
        count = 0
        for person in self._list_of_people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        """
        Sorts the list of people in the ward by age (year of birth) in descending order.

        Uses a lambda function to sort by person's year of birth attribute with a private name convention.
        """
        self._list_of_people.sort(key=lambda person: person._yob, reverse=True)

    def compute_average(self):
        """
        Calculates the average year of birth of teachers in the ward.

        Returns:
            float: The average year of birth of teachers, or None if there are no teachers.
        """
        teachers = [
            person for person in self._list_of_people if isinstance(person, Teacher)]
        if not teachers:
            return None
        total_age = sum(teacher._yob for teacher in teachers)
        average_age = total_age / len(teachers)
        return average_age

# person class
class Person:
    """
        Initializes a Person object with a name and year of birth.

        Args:
            name (str): The name of the person.
            yob (int): The year of birth of the person.
        """
    def __init__(self, name, yob):
        self.name = name
        self._yob = yob

# student class
class Student(Person):
    """
        Initializes a Student object by inheriting from Person and adding a grade attribute.

        Args:
            name (str): The name of the student.
            yob (int): The year of birth of the student.
            grade (str): The grade level of the student.
        """
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        """
        Prints information about the student, including name, year of birth, and grade.
        """
        print(
            f'Student - Name: {self.name} - YoB: {self._yob} - Grade: {self._grade}')

# teacher class
class Teacher(Person):
    """
    Initializes a Teacher object by inheriting from Person and adding a subject attribute.

    Args:
        name (str): The name of the teacher.
        yob (int): The year of birth of the teacher.
        subject (str): The subject the teacher teaches.
    """
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        """
        Prints information about the teacher, including name, year of birth, and subject.
        """
        print(
            f'Teacher - Name: {self.name} - YoB: {self._yob} - Subject: {self.subject}')

# doctor class
class Doctor(Person):
    """
    Initializes a Doctor object by inheriting from Person and adding a specialist attribute.

    Args:
        name (str): The name of the doctor.
        yob (int): The year of birth of the doctor.
        specialist (str): The medical specialty of the doctor.
    """
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        """
        Prints information about the doctor, including name, year of birth, and specialty.
        """
        print(
            f'Doctor - Name: {self.name} - YoB: {self._yob} - Specialist: {self.specialist}')