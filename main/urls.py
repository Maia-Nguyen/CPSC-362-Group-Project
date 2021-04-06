from django.urls import path
from . import views
# Goal: Navigate to profile page
# User is prompted to input their info
# Check admin to confirm
# Goal2: Store User's list into the database
# Let user access their list by navigating to their profile
# Goal3: Display Popular movies, Highest grossing, High rated, allow user to refresh
# Home page also provides the user a personalized recommendation based on their list
urlpatterns = [
    path("my_form", views.my_form, name='form'),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("display", views.display, name="display"),
    path("display/home", views.home, name="return")
]