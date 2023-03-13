from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requset):
    return HttpResponse("안녕하세요. 당신의 poll 인덱스입니다.")
