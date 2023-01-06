from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)

# 在一个普通字典上使用setdefault
d = {}

d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

pairs = [('a', 1), ('a', 2), ('b', 4)]
# 手动创建多值映射字典
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

# 使用defaultdict创建多值映射字典
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)
