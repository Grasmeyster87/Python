def concat(first, second):
    return first + second


def concat1(first: str, second: str) -> str:
    return first + second


def double(n: int) -> int:
    result: int = n * 2
    return result


def word_multiply(text: str, num: int) -> str:
    return f'{text*num}'


text = 'python'
print(word_multiply(text, 2))  # => pythonpython
print(word_multiply(text, 0))  # => 
