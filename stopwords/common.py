from abc import abstractmethod
from typing import List


@abstractmethod
def get_stopwords(filename: str) -> List[str]:
    """
    Get the list of stop words from file.
    :param filename: Filename in the same directory.
    :return: Stop words.
    :rtype: List of str.
    """
    raise NotImplementedError
