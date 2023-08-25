#!/usr/bin/env python3
""" pagination module for start and end of page"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that takes in two integers and return
       a tuple containing number of pages"""

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
