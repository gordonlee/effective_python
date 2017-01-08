"""

53. 의존성을 분리하고 재현하려면 가상 환경을 사용하자.

핵심 정리
    - 가상 환경은 pip 를 사용하여 같은 머신에서 같은 패키지의 여러 버전을 충돌
    없이 설치할 수 있게 해준다.
    - 가상 환경은 pyvenv 로 생성하며, source bin/activate 로 활성화하고
    deactivate 로 비활성화 한다.
    - pip freeze 로 환경에 대한 모든 요구 사항을 덤프할 수 있다.
    requirements.txt 파일을 pip install -r 명령의 인수로 전달하여 환경을
    재현할 수 있다.
    - 파이썬 3.4 이전 버전에서는 pyvenv 도구를 별도로 다운로드해서 설치해야 한다.
    명령줄 도구의 이름은 pyvenv 가 아닌 virtualevn 다.

for windows
    https://docs.python.org/3/library/venv.html

"""
import httpie
