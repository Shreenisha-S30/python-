#Write a Python program that randomly selects one student’s name from a list.
#This program can be used by a teacher to randomly choose a student for answering a question or giving a presentation.
import random

students = ["Arun","Anu","Charan","Disha","Maya","Ajay","Vijay","Kashvi","Megha","Deepa"]
print("\nStudents list: ", students)
teacher = random.choice(students)
print(f"\n{teacher} have to answer the question.\n ")