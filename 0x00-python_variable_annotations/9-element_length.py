#!/usr/bin/env python3
""" type-notatiions - functions"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element length """
    return [(i, len(i)) for i in lst]
