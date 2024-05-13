N = 30

attendance_list = [0] * (30)
for _ in range(N - 2):
    student_num = int(input())
    attendance_list[student_num - 1] = 1

for index, value in enumerate(attendance_list):
    if value == 0:
        print(index + 1)