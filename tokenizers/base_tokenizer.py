from abc import ABC, abstractmethod
from typing import List


class Tokenizer(ABC):
    """
    Tokenizer base class
    """
    @abstractmethod
    def tokenize(self, input) -> List:
        """
        :param input: Input to be tokenize.
        :return: Tokens of input.
        :rtype: List.
        """
        raise NotImplementedError
