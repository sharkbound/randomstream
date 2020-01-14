import random
from collections.abc import Generator
from itertools import count

__all__ = (
    'randint',
    'randrange',
    'RngWrapper',
    'choice',
)

from typing import Sequence


class RngWrapper:
    def __init__(self, generator):
        self.generator: Generator = generator

    def next(self):
        return next(self)

    def next_iter(self, count=1):
        yield from (next(self) for _ in range(count))

    def next_tuple(self, count: int):
        return tuple(self.next_iter(count))

    def next_list(self, count: int):
        return list(self.next_iter(count))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)


def randint(a: int, b: int) -> RngWrapper:
    return RngWrapper((random.randint(a, b) for _ in count()))


def randrange(start: int, stop: int = None, step: int = 1) -> RngWrapper:
    return RngWrapper((random.randrange(start, stop, step) for _ in count()))


def choice(items: Sequence) -> RngWrapper:
    return RngWrapper((random.choice(items) for _ in count()))
