from collections import deque
def solution(priorities, location):
    priorities = list(enumerate(priorities))
    priorities = deque(priorities)
    ans = 1
    while 1:
        if len(priorities) == 1:
            return ans
        temp = priorities.popleft()
        if max(priorities, key=lambda e: e[1])[1] <= temp[1]:
            if temp[0] == location:
                return ans
            ans += 1
        else:
            priorities.append(temp)
