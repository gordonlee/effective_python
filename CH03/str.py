import os


# input: (str or bytes)
# output: str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # str instance


# input: (str or bytes)
# output: bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # bytes instance


def print_debug(inst):
    print(inst, type(inst))


# main function
def main():
    str_inst = "이건 스트링 객체입니다."
    print_debug(str_inst)

    str_inst_convert_bytes = to_bytes(str_inst)
    print_debug(str_inst_convert_bytes)

    bytes_convert_str = to_str(str_inst_convert_bytes)
    print_debug(bytes_convert_str)

    '''
    아래 코드는 런타임 에러가 출력됩니다. // TypeError: must be str, not bytes
    python3 에서 아래 파일을 열려면, 파일이 binary 임을 명시해야 합니다.
    '''
    # with open('/random.bin', 'wb') as f:
    with open('/random.bin', 'w') as f:
        f.write(os.urandom(10))

if __name__ == "__main__":
    main()
