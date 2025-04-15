from django.shortcuts import render
from . import main

def index(request):
    template_data = {}
    prompt = request.GET.get('prompt')
    template_data['response'] = main.generate(prompt)
    return render(
        request,
        'llm/index.html',
        {'template_data': template_data}
    )