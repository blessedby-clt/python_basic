# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
#
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.

# 입출력 예
# n	return
# 12345	[5,4,3,2,1]

def solution(n):
    answer = []
    for number in str(n) :
        answer.append(int(number))
    return answer[::-1]

## map을 이용해 깔끔하게 정리한 코드도 기재
def reverse_digit(n) :
    return list(map(int, reversed(str(n))))

## reversed VS.reverse
## reverse의 경우 리스트 값 자체를 변경. list.reverse()는 None 값 반환
## reversed는 리스트 값 자체를 변환하지는 않지만, list 타입은 아님. listreverseiterator로 변환.
## reversed를 쓰고 싶다면 list(...)로 한 번 감싸줘야 함.
