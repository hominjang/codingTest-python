from collections import deque


def solution(bridge_length, weight, truck_weights):
    qeue = deque()
    answer = 0
    count = 0

    for i in truck_weights:

        # 다리가 견딜 수 있는 무게
        if (sum(qeue) + int(i)) > weight:
            answer = answer + 1
            count = 0
            qeue.clear()
            qeue.append(i)

        # 다리에 올라갈 트럭 수
        if count == bridge_length:
            answer = answer + 1
            count = 0
            qeue.clear()

        count = count + 1
        answer = answer + 1
        qeue.append(i)

    return answer

