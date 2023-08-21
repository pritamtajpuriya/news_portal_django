from datetime import datetime
import email
from email import message

from django.shortcuts import get_object_or_404, render, HttpResponse

from news.models import Category, News, Subscription, Tag
from django.db.models import Q
from rest_framework import status
from news.serializers import CategorySerializer, NewsSerializer
from news.utils import TodayBS
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

# Create your views here.


class NewsList(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs["id"])


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainNewsList(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(is_main=True)


class RecentUpdateList(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(is_main=False, is_highlighted=False).order_by(
            "-published_at"
        )[0:6]


@api_view(["GET", "POST"])
def subscription(request):
    message = ""
    print(request.data["email"])
    if request.method == "POST":
        subscriptionFind = Subscription.objects.filter(email=request.data["email"])
        if subscriptionFind:
            message = "Email already Exist"
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            Subscription.objects.create(email=request.data["email"])
            message = "Successfully created"

            return Response({"message": message}, status=status.HTTP_201_CREATED)
