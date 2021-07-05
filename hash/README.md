# Hash
### 1. 완주하지 못한 선수 (marathon.py)
---
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
>1. 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
>2. completion의 길이는 participant의 길이보다 1 작습니다.
>3. 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
>4. 참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예
|participant|completion|return|
|:------:|:---:|:---:|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|
|["mislav", "stanko", "mislav", "ana"]|["stanko", "ana", "mislav"]|"mislav"|

입출력 예 설명

>예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

>예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

>예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

출처 : https://hsin.hr/coci/archive/2014_2015/contest2_tasks.pdf

문제 접근
>동명이인이 있을 수 있으므로 완주하지 않은 동일인물을 찾아낼 수 있도록 동명이인의 수를 기록하는 자료구조가 필요하다. 이때 해시를 이용하면 더 효율적으로 해결할 수 있다.

>각 언어에는 대응 관계를 나타내는 자료형을 갖고 있는데, 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다. 파이썬에서 이를 사용한 자료형으로는 Dictionary 가 있다. 

>이 dictionary 자료형을 사용해서 Key 에 참가자의 이름을, Value 에 그 이름을 가지고 있는 사람의 수를 넣어 dictionary를 만든다. 그 후 완주한 사람 이름을 가지고 있는 dictionary의 Value 뺀다. 마지막으로 참가자중 Value 값이 0이상인 한 사람을 리턴한다.