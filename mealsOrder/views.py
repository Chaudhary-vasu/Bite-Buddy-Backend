from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class MealsItemAPI(APIView):
    def get(self, request):
        meals = MealsItems.objects.all()
        serializer = MealsItemSerializer(meals, many=True)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Meals list",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = MealsItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "message": "Meals Created",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Some Error Occured.",
                "data": serializer.data,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class OrdersAPI(APIView):
    def get(self, request, user):
        orders = Orders.objects.filter(user__user=user)

        if orders.exists():  # Check if there are any orders
            serializer = OrdersSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "No orders found.",
                    "data": [],
                },
                status=status.HTTP_200_OK,
            )

    def post(self, request):
        data = request.data
        user = data["user"]
        # print("data = ", data)
        ordermeals = data["ordered_meals"]

        # print("ordermeals =", ordermeals)

        if len(ordermeals) == 0:
            return Response(
                {
                    "status": status.HTTP_204_NO_CONTENT,
                    "message": "Order can't be empty.",
                    "data": "",
                },
                status=status.HTTP_200_OK,
            )

        customer = Customer.objects.create(
            user=user["name"],
            street=user["street"],
            postalCode=user["postalCode"],
            city=user["city"],
        )
        customer.save()

        for i in ordermeals:
            meal_item = MealsItems.objects.get(name=i["name"])
            if not meal_item:
                return Response({
                    "success": status.HTTP_400_BAD_REQUEST,
                    "message": "Something went wrong.",
                 },
                status=status.HTTP_400_BAD_REQUEST,
            )
            # print("MealItem=",meal_item)
            item = Orders.objects.create(
                ordered_meals=meal_item, user=customer, quantity=i["amount"]
            )
            item.save()
        
        return Response(
            {
                "success": status.HTTP_201_CREATED,
                "message": "Order Placed!!",
                "customer": customer.user,
            },
            status=status.HTTP_200_OK,
        )