# Program #5: Course Info Grabber, Griffin Corniea, 10/21/25





course_list = {}

print("Enter course information:")


while True:
    course_id = input("Enter course ID (or 'done' to finish): ")

    if course_id == "done":
        break

    course_name = input("Enter course name: ")
    course_list[course_id] = course_name

search_subject = input("Enter subject to search for: ")
print("Courses with subject {search_subject}:")

found_count = 0

for course_id, course_name in course_list.items():
    subject = course_id.split()[0]

    if subject == search_subject:
        print(f"{course_id}: {course_name}")
        found_count += 1

if found_count == 0:
    print(f"No courses found with subject {search_subject}")