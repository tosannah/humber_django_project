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

def catalog(request):
    trails = [
        {
            "name": "Pine Ridge",
            "distance": 8.5,
            "elevation": 320,
            "difficulty": "moderate",
            "is_open": True,
        },
        {
            "name": "Maple Loop",
            "distance": 5.2,
            "elevation": 180,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Eagle Peak",
            "distance": 12.7,
            "elevation": 850,
            "difficulty": "expert",
            "is_open": True,
        },
        {
            "name": "Cedar Trail",
            "distance": 7.4,
            "elevation": 410,
            "difficulty": "hard",
            "is_open": False,
        },
        {
            "name": "Lakeview Path",
            "distance": 3.8,
            "elevation": 95,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Summit Ridge",
            "distance": 15.3,
            "elevation": 1020,
            "difficulty": "expert",
            "is_open": False,
        },
    ]

    return render(request, "catalog.html", {"trails": trails})