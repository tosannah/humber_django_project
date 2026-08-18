from django.shortcuts import render


def home(request):
    context = {
        "greeting": "Welcome to Waypoint!"
    }
    return render(request, "home.html", context)


def report(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        return render(request, "thank_you.html", {"name": name})

    return render(request, "report.html")


def search(request):
    query = request.GET.get("q", "")
    return render(request, "search.html", {"query": query})