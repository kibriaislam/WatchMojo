from django.urls import path



from movies.api.views import movie_list,movie_details

urlpatterns = [
    path("", movie_list, name='listing-movie'),
    path('<int:pk>', movie_details, name='movie-details'),
]
