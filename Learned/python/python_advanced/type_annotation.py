# mypy module: type_annotation
import typing

number : int = 1

def greeting(name: str) -> str:
    return f'Hello {name}'

arr : typing.List[int] = [1, 2, 3]
alpha : typing.List[str, str, str] = ['a', 'b', 'c']