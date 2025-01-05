from concurrent import futures
import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink",
                          "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake",
                            "cheese cake", "brownie", "pancakes", "waffles"]


class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    # Logic goes here
    def _create_response(self, orderID, items, status):
        """Helper to create a RestaurantResponse"""
        item_messages = [restaurant_pb2.items(itemName=item) for item in items]
        return restaurant_pb2.RestaurantResponse(
            orderID=orderID,
            status=restaurant_pb2.RestaurantResponse.ACCEPTED if status else restaurant_pb2.RestaurantResponse.REJECTED,
            itemMessage=item_messages,
        )

    def FoodOrder(self, request, context):
        # Check if all items are valid food items
        if all(item in RESTAURANT_ITEMS_FOOD for item in request.items):
            return self._create_response(request.orderID, request.items, True)
        return self._create_response(request.orderID, request.items, False)

    def DrinkOrder(self, request, context):
        # Check if all items are valid drink items
        if all(item in RESTAURANT_ITEMS_DRINK for item in request.items):
            return self._create_response(request.orderID, request.items, True)
        return self._create_response(request.orderID, request.items, False)

    def DessertOrder(self, request, context):
        # Check if all items are valid dessert items
        if all(item in RESTAURANT_ITEMS_DESSERT for item in request.items):
            return self._create_response(request.orderID, request.items, True)
        return self._create_response(request.orderID, request.items, False)

    def MealOrder(self, request, context):
        # Check if there are exactly three items: one each from food, drink, dessert in the correct order
        if len(request.items) == 3 and \
                request.items[0] in RESTAURANT_ITEMS_FOOD and \
                request.items[1] in RESTAURANT_ITEMS_DRINK and \
                request.items[2] in RESTAURANT_ITEMS_DESSERT:
            return self._create_response(request.orderID, request.items, True)
        return self._create_response(request.orderID, request.items, False)


def serve():
    # Logic goes here
    # Remember to start the server on localhost and a port defined by the first command line argument
    port = sys.argv[1] if len(sys.argv) > 1 else "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
