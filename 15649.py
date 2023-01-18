n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

#재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트
s = []

def dfs():
    #(함수 출력조건) 리스트 s안에 m개의 요소가 쌓인다면 출력해주도록 한다.
    if len(s) == m:
        print(s)
        #[1, 2, 3] > 1 2 3
        print("m==s ok")
        print(' '.join(map(str, s)))
        return #함수를 빠져나가는 방법

    for i in range(1, n + 1):
        print(f'i실행합니다용{i}')
        if visited[i]:
            continue # True이면, 아래 코드를 실행하지 않고 건너뜀
        visited[i] = True
        s.append(i)
        print(f'dfs실행 직전:{s}')

        dfs()
        #i=1부터 반복되는데 visited[1] = True이기 때문에 조건문에 걸려 continue 된다 s=[1]인상태 , i=2 때 s=[1,2]
        #재귀 함수 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.      s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
        print("i : %d " % (i))
        print(f'dfs실행 직후:{s}')
        print(visited)
        s.pop() #리스트의 맨 마지막 원소를 리턴하고 해당 원소는 삭제
        print(f'backTracking:{s}')
        visited[i] = False
        print(visited)

dfs()