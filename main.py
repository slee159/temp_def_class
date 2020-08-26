# main py에서 calculation.py 정의한 함수 불러오기
# import calculation as cal

from arithmetic import plus
# arithmetic에 . 찍으면 클래스 명이, plus에 . 찍으면 함수 명이 나오게 됨 ㅎㅎ
from arithmetic import subtract

a = 3
b = 4

def main():
    print("안녕하세요, main() 입니다.")
    print("a + b = ", plus.add(a, b))
    print("a - b = ", subtract.minus(a, b))

# 데이터 전처리 시작
from dataPreprocessing import processing
from dataPreprocessing import importData
data = importData.readData()
processing.process_data(data)


if __name__ == "__main__":
    main()



