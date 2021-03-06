# Graph
### 1. 가장 먼 노드 (furthest_node.py)
---
문제 설명

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
> * 노드의 개수 n은 2 이상 20,000 이하입니다.
> * 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
> * vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

입출력 예

|n|vertex|return|
|:-:|:--:|:----:|
|6|[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]|3|

입출력 예 설명

예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.

![image](https://user-images.githubusercontent.com/57613321/130767906-82680f12-07b5-4ed6-b28b-d8d0a1262514.png)

출처 : https://programmers.co.kr/learn/courses/30/lessons/49189

문제 접근
> 그래프를 구현하는 방법에는 인접행렬(Adjacency Materix)와 인접리스트(Adjacency List)방식이 있다. 두개의 구현 방식은 각각의 상반된 장단점을 가지고 있는데 대부분 인접리스트 형식을 많이 사용한다.

> 이 문제는 vertex 배열을 인접리스트로 만들어서 BFS를 통해 해결했다.

> 노드는 한번씩만 도달하면 더 이상 그 노드를 찾지 않도록 check 배열을 사용했다. (다른 길을 사용해서 중복으로 계산되는 것을 방지하기 위해)

> alist는 queue에서 pop이 이뤄지기 때문에 각 노드마다의 깊이를 저장하기 위해 설정해줬다.

> * list의 count와 max, in 시간복잡도는 O(n)


### 2. 순위 (ranking.py) **
---
문제 설명

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
> * 선수의 수는 1명 이상 100명 이하입니다.
> * 경기 결과는 1개 이상 4,500개 이하입니다.
> * results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
> * 모든 경기 결과에는 모순이 없습니다.

입출력 예

|n|results|return|
|:-:|:---:|:----:|
|5|[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]|2|

입출력 예 설명

2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.

출처 : https://programmers.co.kr/learn/courses/30/lessons/49191

문제 접근
> i에게 지는 사람은 i를 이긴 사람에게도 진다. 또한 i를 이긴 사람은 i에게 진 사람에게도 이긴다. 이 두가지 조건을 사용해서 문제를 해결한다. (이 부분이 생각하기 어려웠다.)

> 중복을 허용하지 않기 위해서 집합을 사용한다.

> 각 선수의 이긴 선수와 진 선수의 합이 전체 n에서 자기 자신을 뺀 n-1과 같다면 정확하게 순위를 체크할 수 있으므로 count를 증가 시켜준다.
