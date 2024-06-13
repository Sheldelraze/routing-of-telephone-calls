import unittest

from libs.operator import Operator
from libs.operator_repository import OperatorRepository
from libs.routing_service import RoutingService

class TestRoutingService(unittest.TestCase):

    def setUp(self):
        self.operator_a = Operator("Operator A")
        self.operator_a.insert_prefix("1", 0.9)
        self.operator_a.insert_prefix("268", 5.1)
        self.operator_a.insert_prefix("46", 0.17)
        self.operator_a.insert_prefix("4620", 0.0)
        self.operator_a.insert_prefix("468", 0.15)
        self.operator_a.insert_prefix("4631", 0.15)
        self.operator_a.insert_prefix("4673", 0.9)
        self.operator_a.insert_prefix("46732", 1.1)

        self.operator_b = Operator("Operator B")
        self.operator_b.insert_prefix("1", 0.92)
        self.operator_b.insert_prefix("44", 0.5)
        self.operator_b.insert_prefix("46", 0.2)
        self.operator_b.insert_prefix("467", 1.0)
        self.operator_b.insert_prefix("48", 1.2)

        self.operator_repository = OperatorRepository()
        self.operator_repository.add_operator(self.operator_a)
        self.operator_repository.add_operator(self.operator_b)

        self.call_routing_service = RoutingService(self.operator_repository)

    def test_cheapest_operator_happy_path(self):
        phone_number = "4673212345"
        cheapest_operator = self.call_routing_service.find_cheapest_operator(phone_number)
        self.assertEqual(cheapest_operator, "Operator B")

    def test_cheapest_operator_edge_case_no_operator(self):
        phone_number = "9999999999"
        cheapest_operator = self.call_routing_service.find_cheapest_operator(phone_number)
        self.assertIsNone(cheapest_operator)

    def test_cheapest_operator_no_prefix(self):
        phone_number = ""
        cheapest_operator = self.call_routing_service.find_cheapest_operator(phone_number)
        self.assertIsNone(cheapest_operator)
