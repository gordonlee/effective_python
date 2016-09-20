from urllib.parse import parse_qs


# main function
def main():
    my_values = parse_qs('red=5&blue=0&green='
                         , keep_blank_values=True)
    print(repr(my_values))

    # my_values(dict)에서 값을 꺼내오기.
    # 값이 비어있거나, 없는 경우에도 예외 없이 꺼내온다.
    print('-- get value from dictionary --')
    print('Red:     ', my_values.get('red'))
    print('Green:   ', my_values.get('green'))
    print('Opacity: ', my_values.get('opacity'))

    # dict 에 없는 값은 초기값으로 대체하기
    red = my_values.get('red', [''])[0] or 0
    green = my_values.get('green', [''])[0] or 0
    opacity = my_values.get('opacity', [''])[0] or 0
    print('-- default value --')
    print('Red:       %r' % red)
    print('green:     %r' % green)  # FIXME: 프린트안에서 쓰는 %r은 뭐고 % 이건 뭔가?
    print('Opacity:   %r' % opacity)

    # 위처럼 처리했을 때, green 과 opacity 는 int 형인 0이고(디폴트니까),
    # red 는 문자열이 리턴된다.
    # 만일 어떤 인자값이던 관계없이 int 로 받으려면 아래와 같은 처리가 필요하다.
    red = int(my_values.get('red', [''])[0] or 0)


if __name__ == "__main__":
    main()
