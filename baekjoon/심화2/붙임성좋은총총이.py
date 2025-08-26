dancing = set()
dancing.add("ChongChong")

for _ in range(int(input())):
    f, s = input().split()
    if f in dancing:
        dancing.add(s)
    elif s in dancing:
        dancing.add(f)

print(len(dancing))
