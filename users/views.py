from django.contrib.auth import authenticate
from django.http import JsonResponse
import json

def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            return JsonResponse({"message": "Login success"})
        else:
            return JsonResponse({"error": "Invalid credentials"})

    return JsonResponse({"error": "Only POST allowed"})