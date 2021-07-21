# Sort
### 1. K번째 수 (Kth_num.py)
---
문제 설명

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
> * array의 길이는 1 이상 100 이하입니다.
> * array의 각 원소는 1 이상 100 이하입니다.
> * commands의 길이는 1 이상 50 이하입니다.
> * commands의 각 원소는 길이가 3입니다.


입출력 예
|array|commands|return|
|:---:|:------:|:----:|
|[1, 5, 2, 6, 3, 7, 4]|[[2, 5, 3], [4, 4, 1], [1, 7, 3]]|[5, 6, 3]|

입출력 예 설명

[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.

[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.

[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

출처 : https://neerc.ifmo.ru/subregions/northern.html

문제 접근
>많은 정렬 알고리즘이 있으나 파이썬 list 내장 함수의 시간복잡도는 Nlog(N)으로 좋은 속도를 가지기 때문에 사용한다.

>정렬 알고리즘에는 버블 정렬, 선택 정렬, 퀵 정렬, 힙 정렬, 병합 정렬, 삽입 정렬, 카운팅 정렬등이 있으며 처음 접해보는 카운팅 정렬에 대한 코드를 같이 업로드한다.


### 2. 가장 큰 수 (largest_num.py)
---
문제 설명

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한사항
> * numbers의 길이는 1 이상 100,000 이하입니다.
> * numbers의 원소는 0 이상 1,000 이하입니다.
> * 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
|numbers|return|
|:-----:|:----:|
|[6, 10, 2]|"6210"|
|[3, 30, 34, 5, 9]|"9534330"|

출처 : https://programmers.co.kr/learn/courses/30/lessons/42746

문제 접근
>우선 0만 들어있는 배열이 입력으로 들어올 수 있기 때문에 배열의 모든 원소가 0일 때 0을 출력해주는 처리를 한다. 예를 들어 [0,0,0,0]이 들어오면 0000이 아니라 0이 출력될 수 있게 한다.

>배열의 타입인 정수를 사용하면 식이 복잡해지기 때문에 문자열로 바꿔 ASCII 코드를 통해 비교하도록 한다. ASCII 코드는 비교 할 때 첫번째 index를 비교하고 같으면 다음 index를 비교 하기 때문에 이 문제에 적합하다.

>여기서 정렬할 때 x*3을 기준으로 하는 이유는 입력의 최대 자리수가 3자리 수이기 때문이다. 그리고 자리수가 다른 것 중 자리수가 달라 비교할 수 없는 경우 인덱스에 같은 수가 나오면 다음 인덱스가 자리수가 적은 수의 마지막 수 보다 커야 더 큰 수라고 할 수 있다. 예를 들어 6, 62가 입력으로 들어오면 2가 6보다 작기 때문에 662가 된다.