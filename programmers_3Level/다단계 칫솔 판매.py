from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    result = defaultdict(int)
    name = defaultdict()
    for en, re in zip(enroll, referral):
        name[en] = re

    def add_price(seller_name, refer_name, price):
        ten_price = int(price * 0.1)
        result[seller_name] += price - ten_price

        if price == 0 or ten_price == 0:
            return

        if refer_name != '-':
            add_price(refer_name, name[refer_name], ten_price)

    for sel, amt in zip(seller, amount):
        price = amt * 100
        add_price(sel, name[sel], price)

    for en in enroll:
        answer.append(result.get(en, 0))

    return answer


print(solution(enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               seller=["young", "john", "tod", "emily", "mary"],
               amount=[12, 4, 2, 5, 10]))


# 다른 사람의 풀이

def solution_other(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idx_list = {}
    for idx, name in enumerate(enroll):
        idx_list[name] = idx

    for idx, name in enumerate(seller):
        price = 100 * amount[idx]
        answer[idx_list[name]] += price
        while referral[idx_list[name]] != "-":
            answer[idx_list[name]] -= price // 10
            name = referral[idx_list[name]]
            answer[idx_list[name]] += price // 10
            price = price // 10
            if price == 0:
                break
        answer[idx_list[name]] -= price // 10
    return answer
