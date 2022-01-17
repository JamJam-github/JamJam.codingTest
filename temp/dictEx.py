text = ['a', 'b', 'c', 'd']
text2 = ['z', 'x', 'y', 'w']
number = [1, 2, 3, 4]
data = dict()

# setdefault는 (key, value)를 구성한다.
for t in text:
    for t2 in text2:
        for n in number:
            data.setdefault((t, t2, n), list())
    # data[t] += 1
print(data)


import collections

s = ['a', 'b', 'c', 'd', 'a']
d = collections.defaultdict(int)

print(d)

for k in s:
    d[k] += 1

print(d)


d2 = collections.defaultdict(list)
print(d2)

for k in s:
    d2[k].append(1)

print('d2', d2)

d2 = collections.defaultdict(int)
for i in s:
    d2[i] += 1
print('d2-2', d2)


# 리스트의 인자들이 각각 몇 개씩 존재하는지 dict 형태로 반환
c = collections.Counter(s)
print(c)


d3 = dict()
d4 = collections.defaultdict(list)

for a in ['cpp', 'java', 'python', '-']:
    for b in ['backend', 'frontend', '-']:
        for c in ['junior', 'senior', '-']:
            for d in ['chicken', 'pizza', '-']:
                # d3[(a, b, c, d)].append('')
                d3.setdefault((a, b, c, d), list())
                d4[(a, b, c, d)]

print(d3)
print(d4)

# 단어 길이별로 중복되지 않는 단어만 필요한 경우
# defaultdict 생성자에 set 함수를 넘기면 중복을 허용하지 않는다.
grouper = collections.defaultdict(set)
for word in ['apple', 'banana', 'orange']:
    length = len(word)
    grouper[length].add(word)

print(grouper)
