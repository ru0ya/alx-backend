#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Method with two integers: index default value None and
        page_size default value 10

        Parameters: index(int), page_size(int)

        Returns: Dictionary with the following key pairs
            index: the current start index of the return page
            next_index: the next index to query with
            page_size: the current page size
            data: the actual page of the dataset
        """
        dataset = self.__dataset
        assert index is not None and index >= 0 and index < len(dataset)

        page = index // page_size
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        data = dataset[start_index:end_index]

        hyper_index = {
                'index': index,
                'next_index': index + 1,
                'page_size': page_size,
                'data': data
                }
        return hyper_index
