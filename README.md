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

My server should fulfil the following: 

- Initialize a gRPC server to localhost with the port set by the first command line argument.
- Implement the functions defined in `restaurant.proto`
- When a request is received to one of the functions, the items in the request should be checked against the arrays defined in restaurant_server.py.
- If all the items from the request are in the restaurant menu, respond with an ACCEPTED status and the original order ID, and the items list itemMessage.
- If one or more items from the request is NOT in the restaurant menu, respond with a REJECTED status and the original order ID, and the items list itemMessage.
FoodOrder, DrinkOrder and DessertOrder will only receive items from their respective categories.
- MealOrder will only receive 1 item each from all categories, but in the order of Food,Drink,Dessert. For example: items=[ “chips”, “water”, “waffles” ]
- MealOrder returns rejected if the placement of each item is incorrect, or if the meal does not have 1 item each from every category.

For example: When the function DrinkOrder receives the following request:

```
orderID="12345abc"
items=[ "fizzy drink", "water", "water" ]
```

It should return:
```
orderID="12345abc"
status=ACCEPTED
itemMessage= [ "fizzy drink", "water", "water" ]
```
The status would be REJECTED if one or more of the items did not exist in the arrays defined in `restaurant_server.py`.