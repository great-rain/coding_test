# 1, 2, 3을 사용해서 2자리 수를 만드는 모든 경우의 수
# 단, 같은 숫자는 중복 사용 불가

def simple_backtrack():
    numbers = [1, 2, 3]
    result = []
    current = []  # 현재까지 선택한 숫자들
    
    def backtrack():
        # 2개를 다 선택했으면 완성!
        if len(current) == 2:
            result.append(current[:])  # 복사해서 저장
            print(f"완성: {current}")
            return
        
        # 1, 2, 3 중에서 하나씩 선택해보기
        for num in numbers:
            # 이미 사용한 숫자는 건너뛰기
            if num in current:
                print(f"  {num}은 이미 사용했으므로 건너뛰기")
                continue
                
            print(f"  {num} 선택 -> 현재: {current + [num]}")
            current.append(num)     # 숫자 선택
            
            backtrack()             # 다음 자리 숫자 선택하러 가기
            
            removed = current.pop() # 되돌아오기 (백트래킹!)
            print(f"  {removed} 제거 -> 되돌아감: {current}")
    
    print("=== 백트래킹 과정 ===")
    backtrack()
    print(f"\n=== 최종 결과 ===")
    print(f"만들 수 있는 2자리 수: {result}")

# 실행
simple_backtrack()