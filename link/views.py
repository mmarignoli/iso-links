from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from link.models import Link
import urllib

def link(request,url):
    try:
        l = Link.objects.get(link_name=url)
        response = HttpResponse(content="", status=307)
        response["Location"] = l.link_to
        return response
    except Link.DoesNotExist:
        return HttpResponseRedirect('/')
