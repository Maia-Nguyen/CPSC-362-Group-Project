from django.shortcuts import render
from .models import MyModel
from .forms import MyForm
from django.http import HttpResponse, HttpResponseRedirect
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
# from django.shortcuts import HttpResponse
import pandas as pd
from matplotlib import pyplot as plt
from Collab_Filter import data2, indices, cosine_sim, movies_list
# from tvmaze.api import Api
# api = Api()


def home(response):
    return render(response, "main/home.html", {})


def logout(request, redirect=None, auth=None):
    auth.logout(request)
    return redirect('home_url')


def display(request):
    def rec(title, cosine_sim=cosine_sim):
        # Find index of the movie that matches the title
        idx = indices[title]

        # Get pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get scores of 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get movie indices
        movie_indices = [i[0] for i in sim_scores]

        # TRY LOOPING TH OUTPUT
        # Return top 10 most similar movies
        return data2['title_x'].iloc[movie_indices]

    # Redirects in the display.html page and Outputs the user's recommendations
    res = request.POST['title']
    val = rec(res)
    val = val.reset_index()
    val = val[['title_x']].to_dict()
    return render(request, 'main/display.html', {'result': sorted(val.items())})


# def my_form(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MyForm()
#     return render(request, 'cvForm.html', {'form': form})

def user_profile(request):
    form = "profile"
    res =  request.POST[form]
    # def my_form(request):
    #     if request.method == "POST":
    #         form = MyForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #     else:
    #         form = MyForm()
    return render(request, 'user_profile.html', {'user_profile': form})
