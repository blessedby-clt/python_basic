## 숫자 야구 main 함수

* 최초 main 함수 작성 시 가장 어려웠던 부분은 

  - 숫자야구 3strike 완성 후, 재시작하도록 안내문 띄우는 부분
  - 어떤 단계에서든 "0" 입력 시 종료 처리하는 부분

* 이를 처리하기 위해 

  - 재시작 여부, 결과값, end_game(종료여부) 등을 초기값으로 세팅했고,
  - end_game이라는 변수를 만들어서 end 조건을 만족하면 end_game 을 1씩 추가시켜서 종료 여부를 구분하는 컬럼을 만들었음.

* 코드가 어떻게든 돌아가기는 하지만, 가독성과 직관성이 떨어지는 문제가 있음.

* state(상태) 라는 개념을 이용해서, 코드의 직관성을 높이는 방법에 대해 피드백 받음.

  ``` python
  while state != 게임종료 :
      ## 게임 단계별로 코드를 작성하면 가독성, 직관성도 높아짐.
      if state == 게임시작 :	
          random_number = input()
          state = 게임중
      elif state == 게임중
  		user_input = input()
          if 특정 조건값 만족
          	state == 게임클리어
          else :
              continue
      elif state == 게임클리어
      	one_more_input = input("게임 한 판 더??")
          if a == 'Y' :
              state == 게임시작
          elif a == 'N'
          	state == 게임종료
          else :
              ...
  print("게임 끝. 수고하셨습니다")
  ```

  

## for문

* 인덱스로 for문을 돌리는 것이 매번 헷갈려서 정리해둠.

* (1) index 없이 for문 돌리기

  ```python
  text = "Hello"
  for i in text :
      print(i)
  
  
  # Output
  # H
  # e
  # l
  # l
  # o
  ```

  * 이렇게 작성하게 되면, i에 각각 문자열 한 글자씩 담겨서 for문이 돌아가게 됨.

* (2) index로 for문 돌리기

  ```python
  text = "Hello"
  for i in range(len(text)) :
      print(text[i])
  # Output
  # H
  # e
  # l
  # l
  # o
  ```

* (3) enumerate 내장 함수를 이용하는 방법

  ```python
  arr = [1, 2, 4]
  for idx, val in enumerate(arr) :
      print(idx, val)
  
  ```

  

## 숫자 판별 함수

* isdigit : 3^2 같이 사람이 읽었을 때도 숫자로 인지되는 문자도 숫자로 판단. 
  단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수
* isdecimal : 0123456789 같이 즉시 숫자로 변환이 가능한 문자만 숫자로 판단.
* isnumeric : 1/2같이 숫자로 표현이 가능하면 True 반환

### 참고링크

- for문의 index 관련 : https://cjh5414.github.io/python-for-index/
- 파이썬의 숫자판별 함수 : https://soooprmx.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EC%88%AB%EC%9E%90%ED%8C%90%EB%B3%84%ED%95%A8%EC%88%98/

* isdigit 의 함정 : http://seorenn.blogspot.com/2011/04/python-isdigit.html
* 