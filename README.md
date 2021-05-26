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
  * deleteNode(x) : 노드 x를 제거 (search랑 같이 사용)
  * deleteMax : 가장 큰 key를 가진 노드를 삭제하고 그 key값을 리턴, 빈 리스트라면 None 리턴
  * findMax : 가장 큰 key값을 리턴, 빈 리스트라면 None 리턴
  * sort : 오름차순으로 정렬한 후 양방향 연결리스트를 리턴
  * insertBefore(x,key) : 노드 x 이전에 key값을 가진 노드 삽입
  * insertAfter(x,key) : 노드 x 이후에 key값을 가진 노드 삽입
* splice(a,b,x) 함수 설명
  * 노드a 부터 노드b까지를 떼서 노드x뒤에 붙이는 함수이다. 다른 함수에 이용된다.
  * 조건
    * 노드a와 b가 동일하거나 a다음b 이어야한다.
    * head노드와 x는 a와 b사이에 있을 수 없다.
* [관련내용](https://hellol77.tistory.com/4)

### hashFunction.py
* key와 value 를 저장하는 해쉬테이블
  *  find_slot(key) : key가 존재할 경우 해당 슬롯 번호를 리턴, 없다면 삽일될 슬롯 번호를 리턴
  *  remove(key) : key가 존재할 경우 지우고 key값 리턴, 없으면 None 리턴
  *  search(key) : key가 존재할 경우 key값 리턴, 없으면 None 리턴
  *  hash_function(key) : key%size
  *  set(key,value=none) : key가 테이블에 존재하면 value를 업데이트, key가 테이블에 존재하지 않는다면, key와 value 삽입, 테이블이 다 찼다면 None 리턴, 아니면 key값 리턴
  *  
### carrotMarket.py
* 해쉬 테이블을 이용한 코드
  1. 두 줄의 숫자들을 입력한다. 중복이 가능하다.(예 : 1 2 4 5 7 8 2 2)
  2. 첫번째 출력은 중복된 숫자들을 출력한다. 중복되면 중복된 횟수만큼 그 숫자를 출력한다.
  3. 두번째 출력은 첫번째 출력과 다르게 중복된 횟수만큼 출력되지 않고 중복되면 단 한번만 출력한다.

### minHeap
* 최솟값이 root 노드인 트리
  *  insert(key) : 트리안에 key값을 삽입
  *  heapify_up(key) : 입력된 key값을 올라가면서 재배치하는 함수(insert와 update_key에 쓰인다.)
  *  heapify_down(key) : 입력된 key값을 내려가면서 재배치하는 함수(update_key에 쓰인다.)
  *  find_min : 빈 heap이면 None리턴, 아니면 제일 작은 key값을 리턴
  *  delete_min : 빈 heap이면 None리턴, 아니면 제일 작은 key값을 리턴 한 후 제거
  *  update_key(old_key,new_key) : old_key를 new_key로 바꾼후 재배치하는 함수,old_key가 heap안에 없으면 None리턴, 아니면 new_key값이 최종적으로 저장된 index리턴

### BinarySearchTree
*  tree의 노드v의 key값은 왼쪽 자손 노드들의 key값 보다 커야하고 오른쪽 자손 노드들의 key값 보다는 작아야한다.
  *  preorder(root node) : print middle node -> left subtree 순회(traversal) -> right subtree 순회(traversal) 
  *  inorder(root node) :  left subtree 순회(traversal) -> print middle node -> right subtree 순회(traversal) 
  *  postorder(root node) : left subtree 순회(traversal) ->  right subtree 순회(traversal) -> print middle node 
  *  find_loc(key) : insert함수, search함수 등에 사용되며 key값이 존재하면 해당 노드를 리턴하고, 없다면 key값이 삽입될 곳의 부모 노드를 리턴
  *  search(key) : key값을 갖는 노드를 리턴, 없으면 None 리턴
  *  insert(key) : key를 삽입하고 그 삽입된 노드를 리턴
  *  deleteByMerging(x) : 노드 x를 제거한다. 노드 x의 왼쪽 subtree와 오른쪽 subtree를 조정하는 방법을 이용,(사용할 때 search를 이용)
  *  deleteByCopying(x) : 노드 x를 제거한다. 노드 x의 왼쪽 subtree에서 가장 큰 값을 가지는 노드를 찾고 그 노드의 key값을 노드 x에 copy하는 방법,(사용할 때 search를 이용)
  *  succ(x) : 노드 x의 key값보다 바로 다음으로 큰 key를 갖는 노드를 리턴, 없다면 None 리턴,(사용할 때 search를 이용)
  *  pred(x) : 노드 x의 key값보다 바로 다음으로 작은 key를 갖는 노드를 리턴,없다면 None 리턴,(사용할 때 search를 이용)
  *  rotateRight(x) :  노드 x를 기준으로 오른쪽으로 회전하게 한다.
  *  rotateLeft(x) : 노드 x를 기준으로 왼쪽으로 회전하게 한다.


### AVL
