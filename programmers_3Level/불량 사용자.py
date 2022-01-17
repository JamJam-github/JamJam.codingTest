from itertools import permutations


def solution(user_id, banned_id):
    banned_lst = []

    def check_user(user, bann):
        for i in range(len(user)):
            if len(user[i]) != len(bann[i]):
                return False

            for j in range(len(user[i])):
                if bann[i][j] != '*' and bann[i][j] != user[i][j]:
                    return False

        return True

    all_list = list(permutations(user_id, len(banned_id)))
    for users in all_list:
        if check_user(users, banned_id):
            user_set = set(users)
            # print(users, '일치', user_set)
            if user_set not in banned_lst:
                banned_lst.append(user_set)

    return len(banned_lst)


print(solution(user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"],
               banned_id=["fr*d*", "*rodo", "******", "******"]))

# user_id = ["aaa", "bbb", "ccc"]
# outlist = []
# def dfs(user_id, visited, now_list, outlist, n):
#     if len(now_list) == n:
#         outlist.append(now_list)
#         return
#     for i in range(len(user_id)):
#         if not visited[i]:
#             new_list = now_list.copy()
#             new_visited = visited.copy()
#             new_list.append(user_id[i])
#             new_visited[i] = True
#             dfs(user_id, new_visited, new_list, outlist, n)
# dfs(user_id, [False]*len(user_id), [], outlist, 3)
# for o in outlist:
#     print(o)
