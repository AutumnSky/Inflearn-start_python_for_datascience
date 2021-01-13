# -*- coding: utf-8 -*-
def convert_celsius_fahrenheit(celsius):
    fahrenheit = float(((9/5)*celsius) + 32)
    return fahrenheit


def input_celsius_value():
    return float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: "))


def print_fahrenheit_value(celsius, fahrenheit):
    print("섭씨온도 : {0}, 화씨온도 : {1}".format(celsius, fahrenheit))


def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    celsius = input_celsius_value()
    fahrenheit = convert_celsius_fahrenheit(celsius)
    print_fahrenheit_value(celsius, fahrenheit)
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
