from typing import List


def finalValueAfterOperations(self, operations: List[str]) -> int:

    value = 0
    for operation in operations:
        if operation == "++X" or operation == "X++":
            value = value + 1
        else:
            value = value - 1
    return value
