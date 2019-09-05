from django.shortcuts import render

from .forms import FormWithCaptcha


def index(request):
    if request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            response = {'first_name': first_name, 'last_name': last_name}
        else:
            response = {'form': form}
        return render(request, 'index.html', response)
    else:
        form = FormWithCaptcha()
        return render(request, 'index.html', {'form': form})
