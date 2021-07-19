# K번째 수
def solution(array, commands):
    temp = []
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        chk = commands[i][2] - 1
        temp = array[start:end]
        temp.sort()
        answer.append(temp[chk])

    return answer