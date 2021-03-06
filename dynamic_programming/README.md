# Dynamic Programming
### 1. N으로 표현 (n_express.py)
---
문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.

이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
> * N은 1 이상 9 이하입니다.
> * number는 1 이상 32,000 이하입니다.
> * 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
> * 최솟값이 8보다 크면 -1을 return 합니다.

입출력 예

|N|number|return|
|:-:|:--:|:----:|
|5|12|4|
|2|11|3|

입출력 예 설명

예제 #1

문제에 나온 예와 같습니다.

예제 #2

* 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

출처 : https://www.oi.edu.pl/old/php/show.php?ac=e181413&module=show&file=zadania/oi6/monocyfr

문제 접근
> DP 문제는 이전에 실행의 결과 값이 다음 실행에 영향을 주는 것으로 인식해서 이전 값들의 조합을 살펴본다.

> * dp[1] = [N]
> * dp[2] = dp[1] ⚙︎ dp[1]
> * dp[3] = dp[1] ⚙︎ dp[2], dp[2] ⚙︎ dp[1]
> * dp[4] = dp[1] ⚙︎ dp[3], dp[2] ⚙︎ dp[2], dp[3] ⚙︎ dp[1]
> * dp[5] = dp[1] ⚙︎ dp[4], dp[2] ⚙︎ dp[3], dp[3] ⚙︎ dp[2], dp[4] ⚙︎ dp[1]
> * dp[6] = dp[1] ⚙︎ dp[5], dp[2] ⚙︎ dp[4], dp[3] ⚙︎ dp[3], dp[4] ⚙︎ dp[2], dp[5] ⚙︎ do[1]
> * dp[7] = dp[1] ⚙︎ dp[6], dp[2] ⚙︎ dp[5], dp[3] ⚙︎ dp[4], dp[4] ⚙︎ dp[3], dp[5] ⚙︎ do[2], dp[6] ⚙︎ do[1]
> * dp[8] = dp[1] ⚙︎ dp[7], dp[2] ⚙︎ dp[6], dp[3] ⚙︎ dp[5], dp[4] ⚙︎ dp[5], dp[5] ⚙︎ do[3], dp[6] ⚙︎ do[2], dp[7] ⚙︎ do[1]

> 다음과 같이 사칙연산한 값이 들어간다. 이에 대해서 중복을 제거해주기 위해서 set을 사용한다. 

> 이외에도 dp[2]에는 NN, dp[3]에는 NNN, dp[4]에는 NNNN과 같이 반복되는 수가 들어가줘야 한다.

> 시간 복잡도는 O(8 * 8 * 4 * 8) = O(1)로 좋은 효율성을 보인다.


### 2. 정수 삼각형 (int_triangle.py)
---
문제 설명

![image](https://user-images.githubusercontent.com/57613321/128980256-8e17aee3-81e0-4de6-a0f1-865d973cc853.png)

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
> * 삼각형의 높이는 1 이상 500 이하입니다.
> * 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

입출력 예

|triangle|result|
|:------:|:----:|
|[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]|30|

출처 : http://stats.ioinformatics.org/countries/SWE

문제 접근

> 메모이제이션은 반복적으로 계산되는 것들의 계산 횟수를 줄이기 위해 이전에 계산했던 값을 저장해두었다가 나중에 재사용하는 방법이다. 메모이제이션이 동적 프로그래밍 중 하나이다.

> 삼각형의 꼭대기부터 내려오면서 최대 값을 저장한다. 결국 삼각형의 가장 밑에는 해당 값까지 오기 위한 최대 값이 저장되고
max 메소드를 이용하여 그 중 가장 큰 값을 골라준다. 

> 여기서는 두가지 경우로 나눠야한다. 코너에 있어서 위레벨의 첫 또는 끝 숫자를 받아서 더해주는 경우, 중심에 있어서 위레벨의 좌우 숫자중 큰 것을 받아서 더해주는 경우가 있다.

> 처음에는 적은 쪽을 기준으로 for문을 작성했는데 복잡해져서 잘 해결되지 않았다. 따라서 큰 쪽을 기준으로 for문을 작성했는데 훨씬 수월했다. 다시 말해서 바꾸는 쪽을 기준으로 작성했더니 코드가 깔끔해졌다.

> 즉, 처음에는 7에 3, 8을 더해서 3, 8 위치에 저장하려 했고 이후에 3, 8에 7을 더해서 3, 8 위치에 저장했다.

> 깊이가 30이상된다면 깊이우선이나 너비우선보다는 동적계획법(최적의 효율을 찾아내야하는 코딩방식) 사용하는 것이 좋다. 또한 경로를 묻지 않고 최대값만 묻는 문제이기 때문에 동적계획법이 낫다.


### 3. 등굣길 (way_school.py)
---
문제 설명

계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

![image](https://user-images.githubusercontent.com/57613321/129195885-cd16c223-2935-4f1e-b93c-ea030eb5f524.png)

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

제한사항
> * 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
>   * m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
> * 물에 잠긴 지역은 0개 이상 10개 이하입니다.
> * 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

입출력 예

|m|n|puddles|return|
|:-:|:-:|:-:|:----:|
|4|3|[[2, 2]]|4|

입출력 예 설명

![image](https://user-images.githubusercontent.com/57613321/129195906-91542031-8a9a-4f01-b2e0-1abc16afd8bb.png)

출처 : https://programmers.co.kr/learn/courses/30/lessons/42898

문제 접근

> 동적계획법에 따라서 새로운 리스트를 만들어 경로를 기억한다. 이를 통해 왼쪽과 위집에서 부터 하나씩 모든 경우의 수를 계산하며 학교를 가면 되는 문제이다.

> 이동방향은 오른쪽과 아래 딱 두방향이기 때문에, dp[i,j]의 값은 다음과 같다.

> dp[i][j] = dp[i-1][j] + dp[i][j-1]

> 위 점화식에 맞춰 문제를 풀게 되면, 쉽게 풀 수 있다. 이 때 집에서 어떤 칸까지의 최적 경로는 어떤 칸의 윗칸과 왼쪽 칸의 합인데 맨 위쪽과 맨 왼쪽 같은 경우는 위 쪽과 왼쪽이 없기 때문에 계산을 편하게 하기 위해서 위쪽에 한줄, 왼쪽에 한 줄을 추가해준다.

> 새로 만든 줄들과 웅덩이가 연산에 영향을 미치지 못하게 하기 위해서 0으로 설정해준다.

> 또한 이번 문제에서 주의할 점은, 웅덩이의 위치 puddles의 좌표가 반대로 되어있다.


### 4. 도둑질 (stealing.py)
---
문제 설명

![image](https://user-images.githubusercontent.com/57613321/129329071-06d0b581-0658-4a3e-967b-2c19c44529a8.png)

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

제한사항
> * 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
> * money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

입출력 예

|money|return|
|:---:|:----:|
|[1, 2, 3, 1]|4|

출처 : https://programmers.co.kr/learn/courses/30/lessons/42897

문제 접근

> 도둑이 훔칠 수 있는 돈의 최댓값을 저장하는 dp 테이블을 생성한다. dp[i]는 i 번째 집까지 털었을 때 최댓값이다.

> 처음에 마을이 원형이 아닌 일자 형태로 있다고 생각한다.

> 첫 집 부터, 마지막 집까지 하나씩 추가하면서 최대로 가져올 수 있는 값을 구한다.
> * 집이 하나 있을 경우, 그 집을 터는게 최대값
> * 집이 두 개 있을 경우, 인접한 집을 털지 못하므로 두 집 중 money가 큰 집을 턴다.
> * 집이 3 개만 있을 때, 현재 i 집 money + i-2 번째 집 money 혹은 i-1집 money 중 더 큰 값을 가져오면 된다.

> 즉 아래와 같이 점화식이 나온다.

> dp[i] = max(dp[i-1], money[i]+ dp[i-2])

> 집들이 동그랗게 배치되어 있기 때문에 첫집과 마지막집은 인접한다. 또한 첫 집과 마지막 집이 둘다 포함되는 경우가 생길 수 있다. 따라서 첫집과 마지막집을 같이 털 수 없으므로, 첫집을 털 때와 마지막집을 털 때의 경우를 나누어야 한다.

> 코드에서 dp는 0번째 요소를 고르고 시작한 경우이며, dp2는 0번째 요소를 고르지 않고 시작한 경우
