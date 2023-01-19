import sys

n, m = map(int, sys.stdin.readline().split())

s = [str(sys.stdin.readline()) for _ in range(n)] # 집합 s
cnt = 0

# 반복문을 통해 m개의 문자열을 확인
for i in range(m):
    word = str(sys.stdin.readline())

    # 집합 s에 문자열이 포함되어 있으면 카운트
    if word in s:
        cnt += 1

print(cnt)



# input().split()  >> 결과값: ['4', '4'] <class 'list'>

# map(function, iterable)
# 두 번째 매개변수로는 반복가능한 자료형(리스트, 튜플 등)이 옴
# map함수의 Return Value는 map object이기 때문에 해당 자료형을 list or tuple 형 변환 필요
# 함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수
# 즉, map(적용시킬 함수, 적용할 값들)
