from typing import List, Optional

from libs.operator import Operator


class OperatorRepository:
    def __init__(self):
        self.operators: List[Operator] = []

    def add_operator(self, operator: Operator):
        self.operators.append(operator)

    def find_cheapest_operator(self, phone_number: str) -> Optional[Operator]:
        cheapest_rate = float("inf")
        cheapest_operator = None

        for operator in self.operators:
            rate = operator.get_rate(phone_number)
            if rate is not None and rate < cheapest_rate:
                cheapest_rate = rate
                cheapest_operator = operator

        return cheapest_operator
