import os

from libs.operator import Operator
from libs.operator_repository import OperatorRepository


def load_operators_from_directory(directory_path: str) -> OperatorRepository:
    operator_repository = OperatorRepository()

    for filename in os.listdir(directory_path):
        operator_name = os.path.splitext(filename)[0]
        operator = Operator(operator_name)
        with open(os.path.join(directory_path, filename), "r") as file:
            for line in file:
                line = line.strip()
                prefix, price = line.split()
                operator.insert_prefix(prefix, float(price))
        operator_repository.add_operator(operator)

    return operator_repository
