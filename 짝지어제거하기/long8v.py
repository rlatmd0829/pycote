def solution(s):
    new_list = []
    s = list(s)
    for ss in s:
        new_list.append(ss)
        if len(new_list) < 2:
            pass
        else:
            if new_list[-2] == new_list[-1]:
                new_list.pop()
                new_list.pop()
    print(new_list)
    if new_list:
        return 0
    return 1
