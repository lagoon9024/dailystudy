# dailystudy
daily study about programming :)  
- [0317 :: about collection](/200317/0317.md)
  - 번외 심심풀이 코딩 rpi softone maker(악보입력 => 곡출력) [softone_maker](/200317/makesomenoise.c)
    - raspberry pi의 wiring pi의 softone 라이브러리를 활용함
    - 출력 주파수와 음계를 1:1 매핑, string 형태의 입력을 실제 연주 가능한 악보로 저장하는 것을 목표로 제작했다
    - 해싱을 통해 연주 가능한 음을 hash table에 저장하고, 입력값과 hash의 value를 매핑, 배열에 저장해둔 뒤 입력 종료 후 출력
