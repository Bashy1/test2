from django.shortcuts import render
from mainweb.forms import NewProspect


def home(request):
    form = NewProspect()

    if request.method == "POST":
        form = NewProspect(request.POST)

        if form.is_valid():
            form.save()

        else:
            print("error form invalid")

    return render(request, 'mainweb/home.html', {'form': form})

def thankyou(request):
    return render(request, 'mainweb/thankyou.html')