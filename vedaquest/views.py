from django.shortcuts import render, HttpResponse, redirect


def main(request):
    return render(request, 'base.html')
