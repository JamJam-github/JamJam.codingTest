# 다리를 지나는 트럭
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
# 다리는 weight 이하까지의 무게를 견딜 수 있습니다.


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    # bridge.append(truck_weights.pop(0))

    # [0, 0] 다리에서 pop(0)하면 0번째가 없어지고, append 다음 트럭 후 [0, 7]
    # [0, 7] 다리에서 pop(0)하면 0번째가 없어지고, 다음 트럭은 초과되어 못들어가므로 append(0) [7, 0]
    # [7, 0] 다리에서 pop(0)하면 0번째가 없어지고, [0] 상태에서 다음 트럭을 append(4) [0, 4]
    while len(bridge):
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer


print(solution(bridge_length=2, weight=10, truck_weights=[7, 4, 5, 6]))
