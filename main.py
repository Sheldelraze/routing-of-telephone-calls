from libs.data_loader import load_operators_from_directory
from libs.routing_service import RoutingService

if __name__ == "__main__":
    operator_repository = load_operators_from_directory("data")
    routing_service = RoutingService(operator_repository)
    phone_number = "4673212345"
    cheapest_operator = routing_service.find_cheapest_operator(phone_number)
    print(f"The cheapest operator for {phone_number} is {cheapest_operator}")
