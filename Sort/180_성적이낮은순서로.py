# thisisCote implementation_성적이낮은순서로학생출력하기 p.180

n = int(input())

arr = []
for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))  # 튜플로 append

# key를 이용해 점수 기준 정렬
arr = sorted(arr, key=lambda x: x[1])

for student in arr:
    print(student[0], end=' ')
