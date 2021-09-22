# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"


# 문제 풀이
# 공백을 기준으로 문자열을 리스트로 나누고
# 리스트 안에서 짝수면 대문자로, 홀수면 소문자로 바꾸고
# 다시 리스트로 취합하는 형태로 풀었음.

def solution(s):
    result = []
    test_list = s.split(" ")
    for char in test_list :
        answer = ''
        for j in range(len(char)) :
            if j % 2 == 0 :
                answer = answer + char[j].upper()
            else :
                answer = answer + char[j].lower()
        result.append(answer)

    return ' '.join(result)

# 처음에는 자꾸 오류가 났는데 split() 사용 시 공백 처리 때문이었음.
# 관련 참고 링크(https://stackoverflow.com/questions/62013468/is-there-a-difference-between-split-vs-split)
# For example (note there are two spaces between A and B and one at the start and end):
# >>> s = " A  B "
# >>> s.split()
# ['A', 'B']
# >>> s.split(" ")
# ['', 'A', '', 'B', '']
#
# Additionally, consecutive whitespace means any whitespace characters, not just spaces:
#
# >>> s = " A\t  \t\n\rB "
# >>> s.split()
# ['A', 'B']
# >>> s.split(" ")
# ['', 'A\t', '', '\t\n\rB', '']

## pythonic code로 한 번에 깔끔하게 처리한 코드도 공부할 겸 첨부
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
