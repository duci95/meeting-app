from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")

def about(request):
    return HttpResponse("About page displayed")