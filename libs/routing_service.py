from typing import Optional

from libs.operator_repository import OperatorRepository


class RoutingService:
    def __init__(self, operator_repository: OperatorRepository):
        self.operator_repository = operator_repository

    def find_cheapest_operator(self, phone_number: str) -> Optional[str]:
        cheapest_operator = self.operator_repository.find_cheapest_operator(phone_number)
        return cheapest_operator.name if cheapest_operator else None
