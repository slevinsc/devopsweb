#!/usr/bin/python
# encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    username = request.POST.get("username", None)
    if username:
        return render_to_response("login.html", {"username": username})
    else:
        return render_to_response("login.html")


def index(request):
    return render_to_response("index.html", {}, RequestContext(request))


def host(request):
    return render_to_response("host.html", {}, RequestContext(request))
