"""
(A*B*C*D*E....*Z) / MOD = A/MOD * B/MOD * C/MOD ...Z/MOD
인걸 이용해서 코드에서는 A~Z 까지 곱하고 나누면 연산이 커지기때문에 시간이 오래걸린다. 
따라서 매연산 마다 오른쪽 식 처럼 적용해서 계산을 하면 더 빠른 결과를 얻을 수 있다.
"""

import time

MOD = 10000000007
answer = 1
start = time.time()

for i in range(1, 100001):
    answer = (answer * i) % MOD

end = time.time()

print("결과", answer)
print(f"수행 시간: {end - start:.6f}")