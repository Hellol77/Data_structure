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
  * pushBack(key) : key값을 갖는 노드를 가장 뒤에 삽입
  * popFront : 한방향 연결리스트의 첫 노드를 삭제한 후 그 key값을 리턴
  * popBack : 한방향 연결리스트의 마지막 노드를 삭제한 후 그 key값을 리턴
  * search(key) : 한방향 연결리스트에서 key값을 갖는 노드를 찾아 리턴 
  * remove(v) : 노드 v를 제거 
  * reverse(key) : key를 가지는 첫 노드에서 끝 노드까지 반대로 뒤집는 함수(숫자만 입력)
  * findMax :  최대값을 갖는 노드의 key값을 리턴
  * deleteMax : 최대값을 갖는 노드를 제거
  * insert(k,key) : head노드 부터 k번째 다음 노드에 key를 가지는 새로운 노드를 삽입 (k는 양수)
  * [관련내용](https://hellol77.tistory.com/3)
### doublyLinkedList.py
  * 양방향 연결리스트 구현
  * pushFront(key) : key값을 갖는 노드를 가장 앞에 삽입
  * pushBack(key) : key값을 갖는 노드를 가장 뒤에 삽입
  * popFront : 양방향 연결리스트의 첫 노드를 삭제한 후 그 key값을 리턴
  * popBack : 양방향 연결리스트의 마지막 노드를 삭제한 후 그 key값을 리턴
  * search(key) : 양방향 연결리스트에서 key값을 갖는 노드를 찾아 리턴
  * deleteNode(x) : 노트 x를 제거 (search랑 같이 사용)
  * deleteMax : 가장 큰 key를 가진 노드를 삭제하고 그 key값을 리턴, 빈 리스트라면 None 리턴
  * findMax : 가장 큰 key값을 리턴, 빈 리스트라면 None 리턴
  * sort : 오름차순으로 정렬한 후 양방향 연결리스트를 리턴
  * insertBefore(x,key) : 노드 x 이전에 key값을 가진 노드 삽입
  * insertAfter(x,key) : 노트 x 이후에 key값을 가진 노드 삽입
  
### hashFunction.py
  key와 value 를 저장하는 해쉬테이블
  *  find_slot(key) : key가 존재할 경우 해당 슬롯 번호를 리턴, 없다면 삽일될 슬롯 번호를 리턴
  *  remove(key) : key가 존재할 경우 지우고 key값 리턴, 없으면 None 리턴
  *  search(key) : key가 존재할 경우 key값 리턴, 없으면 None 리턴
  *  hash_function(key) : key%size
  *  set(key,value=none) : key가 테이블에 존재하면 value를 업데이트, key가 테이블에 존재하지 않는다면, key와 value 삽입, 테이블이 다 찼다면 None 리턴, 아니면 key값 리턴
### carrotMarket.py
  해쉬 테이블을 이용한 코드
  1. 두 줄의 숫자들을 입력한다. 중복이 가능하다.(예 : 1 2 4 5 7 8 2 2)
  2. 첫번째 출력은 중복된 숫자들을 출력한다. 중복되면 중복된 횟수만큼 그 숫자를 출력한다.
  3. 두번째 출력은 첫번째 출력과 다르게 중복된 횟수만큼 출력되지 않고 중복되면 단 한번만 출력한다.

### minHeap
