# 탐욕법
# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면
# 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

# routes에는 차량의 이동 경로가 포함되어 있으며
# routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
# routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
# 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.
# -30000 <= routes[0], routes[1] <= 30000

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for route in routes:
        if camera < route[0]:  # 진입보다 카메라가 전에 있으면
            answer += 1  # 카메라 증가
            camera = route[1]  # 진출 시점에 카메라 설치

    return answer


print(solution(routes=[[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
