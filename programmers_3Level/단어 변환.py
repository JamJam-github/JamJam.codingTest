from collections import deque


def bfs(begin, target, words, visited):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        curr, d = queue.popleft()

        if curr == target:
            return d

        for i in range(len(words)):
            if not visited[i]:
                cnt = 0
                for a, b in zip(words[i], curr):
                    if a != b:
                        cnt += 1
                # 중복되는 알파벳의 경우 set 처리 부족
                # if len(curr) - 1 == len(set(words[i]) & set(curr)):
                #     print(words[i], curr, '비교')

                if cnt == 1:
                    # print(words[i], curr, '한글자 차이나')
                    visited[i] = True
                    queue.append((words[i], d + 1))
                    print('큐에 담아::', words[i])


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    answer = bfs(begin, target, words, visited)

    return answer


# print(solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log"]))
# print(solution(begin="aaa", target="aab", words=["aab", "dot", "dog", "lot", "log", "cog"]))
