Here I am getting familiar with the concept of Remote Procedure Calls (RPC, often used in building distributed systems) and gRPC (a popular open source RPC framework). I have created a gRPC server that functions as a restaurant. Requests with an order ID and a list of items will be sent to the server and it will respond with the order ID, itemsMessage and a ACCEPTED or REJECTED status.

Repository main structure:
```
restaurant.proto        <-- contains the message definitions and the following service definition:
    FoodOrder           <-- only receive orders that contain food items.
    DrinkOrder          <-- only receive orders that contain drink items.
    DessertOrder        <-- only receive orders that contain dessert items.
    MealOrder           <-- only receive orders that contains only 3 items in the order: food, drink, dessert.
    
restaurant_pb2.py       <-- generated automatically from restaurant.proto.
restaurant_pb2_grpc.py  <-- generated automatically from restaurant.proto.
restaurant_server.py    <-- gRPC server
```