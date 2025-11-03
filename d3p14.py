import random
students = ["nisha","liki","kruti","preetu","gani","arjun","thejas"]
random.shuffle(students)
print("Shuffled List:",students)

winners = random.sample(students,3)
print("🎉 Lucky Draw Winners:",winners)