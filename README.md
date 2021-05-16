## Data_structure with python
이곳은 파이썬으로 작성된 자료구조들이 저장되어 있습니다.

### myList.py

  * 파이썬의 리스트를 class로 구현해본 코드
  * 음수 인덱스도 허용할 수 있다.
### timeComplexity.py

  * 시간복잡도가 O(n^2),O(n)과 O(nlogn)인 코드를 실제로 실행해보면서 실행시간을 비교해보는 코드
  * 각 코드들은 리스트안에 중복이 있으면 NO를 출력하고 아니라면 YES를 출력한다. 하지만 중복이 없도록 설정했기 때문에 무조건 YES가 출력된다.
### infixPostfixCalculation.py

  * stack을 이용한 계산기
  * infix수식을 입력하면 postfix수식으로 바꾼 뒤 결과값을 출력한다.
  * [관련내용](https://hellol77.tistory.com/2)
### singlyLinkedList.py

  * 한방향 연결리스트 구현
  * pushFront(key) : key값을 갖는 노드를 가장 앞에 삽입
  * pushBack : key값을 갖는 노드를 가장 뒤에 삽입
  * popFront : 한방향 연결리스트의 첫 노드를 삭제한 후 그 key값을 리턴
  * popBack : 한방향 연결리스트의 마지막 노드를 삭제한 후 그 key값을 리턴
  * search(key) : 한방향 연결리스트에서 key값을 갖는 노드를 찾아 리턴 
  * remove(v) : 노드 v를 제거 
  * reverse(key) : key를 가지는 첫 노드에서 끝 노드까지 반대로 뒤집는 함수(숫자만 입력)
  * findMax :  최대값을 갖는 노드의 key값을 리턴
  * deleteMax : 최대값을 갖는 노드를 제거
  * insert(k,key) : head노드 부터 k번째 다음 노드에 key를 가지는 새로운 노드를 삽입 (k는 양수)
### doublyLinkedList.py

### hashFunction.py

### carrotMarket.py

### minHeap
