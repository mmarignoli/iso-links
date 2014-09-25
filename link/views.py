from django.shortcuts import render
from django.http import HttpResponse
from link.models import Link
import urllib

def link(request,url):
    l = Link.objects.get(link_name=url)
    response = HttpResponse(content="", status=307)
    response["Location"] = l.link_to
    return response
