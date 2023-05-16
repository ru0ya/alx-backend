#!/usr/bin/env python3
"""
function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range of indexes to
return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.


"""


import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Function that takes two arguments

    Parameters: page(int), page_size(int)

    Returns: Tuple of size two containing a start and end
    index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns correct list of rows
        """
        with open('Popular_Baby_Names.csv', 'r') as file:
            data = csv.reader(file)
            if not (isinstance(page, int) and page > 0):
                raise AssertionError
            if not (isinstance(page_size, int) and page > 0):
                raise AssertionError
            try:
                start_index, end_index = index_range(page, page_size)
                paginated_data = [row for i, row in enumerate(data)
                                  if start_index <= i < end_index]

                return paginated_data
            except IndexError:
                return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, List]:
        """
        function that takes page and page_size as arguments

        Returns: Dictionary containing key-value pairs
        """


