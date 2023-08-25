#!/usr/bin/env python3
""" pagination module"""

from typing import Tuple, List
import csv
import math


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular babies names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset in cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Function to get the element in an order."""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        res = []

        if start >= len(self.dataset()):
            return res_list
        res = self.dataset()
        return res[start:end]
