import sys

n, m = map(int, input().split())

dict_words = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        if word not in dict_words:
            dict_words[word] = 1
        else:
            dict_words[word] += 1

sorted_words = sorted(dict_words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in sorted_words:
    print(word)