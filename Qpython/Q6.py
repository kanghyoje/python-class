courses = {
  "김민준": ["파이썬", "자료구조"],
  "이서연": ["파이썬", "인공지능"],
  "박지후": ["자료구조", "인공지능"],
  "최하은": ["파이썬", "자료구조"],
}

target = "김민준"
my_courses = courses[target]

similar_students = []
recommended = []

for 학생이름, 학생과목 in courses.items():
  if 학생이름 == target:
    continue

  for 과목 in 학생과목:
    if 과목 in my_courses:
      if 학생이름 not in similar_students:
        similar_students.append(학생이름)
    else:
      if 과목 not in recommended:
        recommended.append(과목)

print(similar_students)
print(recommended)