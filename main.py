"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    primeiro = 0  # o primeiro número da soma
    segundo = 0  # o segundo número da soma    
    numbers.sort()
    if len(numbers) < 2:
        return None
    if len(numbers) > 2:
        primeiro = numbers[-2]
        segundo = numbers[-1]
        return primeiro, segundo
