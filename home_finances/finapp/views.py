from django.shortcuts import render
from django.http import HttpResponse
from finapp.models import Entry


def index(request):
    return HttpResponse("And so it begins...")


def detail(request, entry_id):
    entry = Entry.objects.filter(id=entry_id)
    return HttpResponse("Details for entry<br />"
                        f"{str(entry[0]) if entry else '<b>Not available</b>'}")


def results(results, entry_id):
    return HttpResponse(f"Results for entry {entry_id}")
