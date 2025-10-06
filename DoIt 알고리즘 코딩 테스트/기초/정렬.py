# tuple 기반 정렬
scores = [
    (80, 100),
    (100, 50),
    (70, 100),
    (80, 90),
]

scores.sort(key=lambda x: (-x[0], -x[1])) # 내림차순

for s in scores:
    print(f"english={s[0]}, math={s[1]}")

"""
result
english=100, math=50
english=80, math=100
english=80, math=90
english=70, math=100
"""

# dictionary 기반 정렬
scores = [
    {'english': 80, 'math': 100},
    {'english': 100, 'math': 50},
    {'english': 70, 'math': 100},
    {'english': 80, 'math': 90},
]

scores.sort(key=lambda x: (-x['math'], -x['english']))
for s in scores:
    print(s)