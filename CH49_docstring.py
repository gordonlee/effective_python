"""Library for testing words for various linguistic patterns.

Testing how words relate to each ...

Available functions:
- palindrome: Determine if a word is a palindrome.
- check_anagram: Determine if two words are anagrams.
...
"""
"""

49. 모든 함수, 클래스 모듈에 docstring 을 작성하자.

"""


# 함수 docstring 예제
def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

print('**********************************************************')
print(repr(palindrome))
print('**********************************************************')
print(repr(palindrome.__doc__))
print('**********************************************************')
help(palindrome)

"""
    - 대화식 개발이 편해진다.
    repr( __doc__ ) 으로 확인하거나, help(obj) 함수로 확인이 용이하다.
    - 소스코드의 docstring 을 그대로 외부에서 출력할 수 있기 때문에 문서 생성
    도구의 활용의 폭이 커진다.
    - 코더 입장에서 문서가 더 잘 정리되도록 장려할 수 있다.

     PEP 257 에서 docstring 의 모범 사례를 볼 수 있다.
"""

# 모듈의 문서화
# 각 모듈에는 최상위 docstring 이 있어야 한다. 큰따옴표 세 개를 사용한다.
# 첫 번째 줄은 모듈의 목적을 기술, 그 이후 문단은
# 모듈의 모든 사용자가 알아야 하는 모듈의 동작을 자세히 설명.

# words.py
#!/usr/bin/env python3
"""Library for testing words for various linguistic patterns.

Testing how words relate to each ...

Available functions:
- palindrome: Determine if a word is a palindrome.
- check_anagram: Determine if two words are anagrams.
...
"""


# class 의 docstring 도 모듈과 크게 다르지 않다.
class Player(object):
    """Represents a player of the game.

    Subclasses may override the 'tick' method to provide ...

    Public attributes:
    - power: Unused power-ups (float between 0 and 1)
    - coins: ...(integer)
    """
    def __init__(self):
        self.power = 0.0
        self.coins = 1


# 함수 문서화
# 각 공개 함수와 메서드에는 docstring 을 포함한다. 요약을 첫 번째 줄에 적고,
# 그 다음은 특별한 동작이나 인수, 반환 값, 예외에 대해 언급한다.
def find_anagrams(word, dictionary):
    """Find all anagrams for a word.

    This function only runs as fast as the test for ...

    Args:
        word: String of the target word.
        dictionary: Container with all strings that ...

    Returns:
        List of anagrams that were found. ...
    """
    return word

print('**********************************************************')
print(repr(find_anagrams))
print('**********************************************************')
print(repr(find_anagrams.__doc__))
print('**********************************************************')
help(find_anagrams)

print('**********************************************************')
help(Player)  # help(class)
print('**********************************************************')
print(Player.__doc__)  # print(class's doc)
print('**********************************************************')
print(__doc__)  # print(module's doc)
