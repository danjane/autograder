# Let's loop through the student files and check if they have correctly implemented factorial
import os
import importlib.util

# Where we find the student .py files
student_folder = os.path.join(os.getcwd(), "StudentFiles")
students = ["Einstein", "Leibniz", "Newton", "Gauss"]
project = "Factorial"


def py_file_name(student):
    return os.path.join(student_folder, project + "_" + student + ".py")


def check_for_banned_word(py_file, bad_word):
    with open(py_file, 'r') as searchfile:
        for line in searchfile:
            if bad_word in line.split():
                return True


def file_imports(py_file):
    return check_for_banned_word(py_file, "import")


def file_evals(py_file):
    return check_for_banned_word(py_file, "eval")


def check(file):
    if not os.path.isfile(file):
        print("File does not exist :(")
        return False
    if file_imports(file):
        print("File contains the banned keyword 'import' :(")
        return False
    if file_evals(file):
        print("File contains the banned keyword 'eval' :(")
        return False
    return True


def test(py_file):
    # Into the danger zone... we will load and run code from an unknown module.
    # https://stackoverflow.com/a/67692
    spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.MyClass()



if __name__ == '__main__':
    for student in students:
        print(f"\nChecking student : {student}")
        file = py_file_name(student)
        if check(file):
            test(file)

