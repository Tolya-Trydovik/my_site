from django.shortcuts import render

def render(request):
    return render(request, 'todo/render.html', {})
