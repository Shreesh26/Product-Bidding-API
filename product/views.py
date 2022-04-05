from itertools import product
from urllib import request, response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *


class AllProduct (APIView):
    @staticmethod
    def get(request):
        a=list(Product.objects.filter(is_sold=False).values())
        return Response(a)

class AddProduct(APIView):
    @staticmethod
    def post(request):
        
        data=request.data
        user=request.user
        name=data["name"]
        description=data["description"]
        start_price=data["start_price"]
        img=data["img"]
        prod_type=data["type"]
        item=Product(user=user, name=name, description=description, start_price=start_price, img=img, product_type=prod_type, is_sold=False)
        item.save()
        return Response("Item Added")

class ViewProduct(APIView):
    @staticmethod
    def get(request):
        data=request.data
        product=data["product_id"]
        prod_obj=Product.objects.filter(id=product)[0]
        if prod_obj.is_sold==True:
            return Response("Product Already Sold")
        else:
            prod_list=list(Product.objects.filter(id=product).values())
            return Response(prod_list)

class ViewBid(APIView):
    @staticmethod
    def get(request):
        data=request.data
        product=data["product_id"]
        prod_obj=Product.objects.filter(id=product)[0]
        bid=list(Bid.objects.filter(product=prod_obj).order_by("-bid").values())
        return Response(bid)

class PlaceBid(APIView):
    @staticmethod
    def post(request):
        data=request.data
        user=request.user
        product=data["product_id"]
        prod_obj=Product.objects.filter(id=product)[0]
        bid=data["bid"]
        if bid<prod_obj.start_price:
            return Response("Price must be more than the minimum price specified by the seller")
        else:
            prior_bid=Bid.objects.filter(bidder=user, product=prod_obj)
            if len(prior_bid)==0:
                bid_obj=Bid(bidder=user, product=prod_obj, bid=bid)
                bid_obj.save()
                return Response("Bid submitted Sucessfully")
            else:
                Bid.objects.filter(bidder=user, product=prod_obj).update(bidder=user, product=prod_obj, bid=bid)
                return Response("Bid Updated Sucessfully")

class FinalizeBid(APIView):
    @staticmethod
    def post(request):
        data=request.data
        user=request.user
        product=data["product_id"]
        prod_obj=Product.objects.filter(id=product)[0]
        bid=data["bid_id"]
        bid_obj=Bid.objects.filter(id=bid)[0]
        
        if user != prod_obj.user:
            print (prod_obj.user)
            return Response ("Error")
        elif prod_obj.is_sold==True:
            return Response("Error! Successful Bid already selected by you!")

        else:
            Product.objects.filter(id=product).update(is_sold=True)
            success=SuccessfulBid(success_bid=bid_obj)
            success.save()
            successful_bidder=bid_obj.bidder.email
            return Response(successful_bidder)
        
class ProductSearch(APIView):
    @staticmethod
    def get(request):
        prod_type=request.data["type"]
        name=request.data["name"]
        if prod_type==None:
            by_name=list(Product.objects.filter(name__icontains=name, is_sold=False).values())
            return Response (by_name)
        elif name==None:
            by_type=list(Product.objects.filter(product_type=prod_type, is_sold=False).values())
            return Response(by_type)
        by_name=Product.objects.filter(name__icontains=name, is_sold=False)
        by_type=Product.objects.filter(product_type=prod_type, is_sold=False)
        print(by_name.union(by_type))
        search_result=list((by_name.union(by_type)).values())
        return Response(search_result)