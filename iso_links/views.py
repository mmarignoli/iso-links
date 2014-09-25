from django.template import RequestContext, loader, Context, Template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from link.models import Link
from django import forms

class LinkForm(forms.Form):
    link_name = forms.CharField(label='Shorten Link', max_length=255)
    link_to = forms.CharField(label='URL', max_length=255)

def home(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            Link.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')

    else:
        form = LinkForm()

    return render(request, 'home.html', {'form': form})
