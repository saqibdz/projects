class Student:
  def __init__(self, student_id, name, grade):
      self.student_id = student_id
      self.name = name
      self.grade = grade
      self.next_student = None

class StudentRecordSystem:
  def __init__(self):
      self.head = None

  def add_student(self, student_id, name, grade):
      new_student = Student(student_id, name, grade)
      if not self.head:
          self.head = new_student
      else:
          current = self.head
          while current.next_student:
              current = current.next_student
          current.next_student = new_student
      print(f"Student with ID {student_id} added.")

  def delete_student(self, student_id):
      current = self.head
      previous = None
      while current:
          if current.student_id == student_id:
              if previous:
                  previous.next_student = current.next_student
              else:
                  self.head = current.next_student
              print(f"Student with ID {student_id} deleted.")
              return
          previous = current
          current = current.next_student
      print(f"Student with ID {student_id} not found.")

  def search_student_by_id(self, student_id):
      current = self.head
      while current:
          if current.student_id == student_id:
              return current
          current = current.next_student
      return None

  def search_student_by_name(self, name):
      current = self.head
      found_students = []
      while current:
          if current.name == name:
              found_students.append(current)
          current = current.next_student
      return found_students

  def list_students(self):
      if not self.head:
          print("No students in the record.")
          return

      current = self.head
      print("Student Records:")
      while current:
          print(f"ID: {current.student_id}, Name: {current.name}, Grade: {current.grade}")
          current = current.next_student

def main():
  record_system = StudentRecordSystem()

  while True:
      print("\nOptions:")
      print("1. Add Student")
      print("2. Delete Student")
      print("3. Search Student by ID")
      print("4. Search Students by Name")
      print("5. List Students")
      print("6. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
          student_id = input("Enter Student ID: ")
          name = input("Enter Student Name: ")
          grade = input("Enter Student Grade: ")
          if not student_id.isdigit() or not grade.isdigit():
              print("Invalid input for ID or Grade. Please enter numeric values.")
              continue
          record_system.add_student(student_id, name, grade)
      elif choice == '2':
          student_id = input("Enter Student ID to delete: ")
          if not student_id.isdigit():
              print("Invalid input for ID. Please enter a numeric value.")
              continue
          record_system.delete_student(student_id)
      elif choice == '3':
          student_id = input("Enter Student ID to search: ")
          if not student_id.isdigit():
              print("Invalid input for ID. Please enter a numeric value.")
              continue
          student = record_system.search_student_by_id(student_id)
          if student:
              print(f"Student ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
          else:
              print(f"Student with ID {student_id} not found.")
      elif choice == '4':
          name = input("Enter Student Name to search: ")
          students = record_system.search_student_by_name(name)
          if students:
              print("Found Students:")
              for student in students:
                  print(f"ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
          else:
              print(f"No students with the name '{name}' found.")
      elif choice == '5':
          record_system.list_students()
      elif choice == '6':
          break
      else:
          print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  main()
