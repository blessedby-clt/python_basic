# 문제 설명
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

# numbers	    result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	    [2,5,7,9,12]


answer = []
def solution(numbers):
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i < j :
                answer.append(numbers[i] + numbers[j])
    result = sorted(list(set(answer)))
    return result

# sort()를 사용하면 반환값은 None이 반환되고 원본 리스트가 정렬이 됩니다.
# 원본 리스트는 변하지 않고 정렬한 리스트를 새로 만들고 싶은 경우에는 sorted()를 사용합니다.
