from django.urls import path



from movies.api.views import StreamingPlatformAV, StreamingPlatformDtails, content_list,content_details,StreamingPlatformAV

urlpatterns = [
    path("", content_list, name='listing-movie'),
    path('<int:pk>', content_details, name='movie-details'),

    path('streaming-platform/', StreamingPlatformAV.as_view(),name = "streaming-platform"),
    path("streaming-platform/<int:pk>/", StreamingPlatformDtails.as_view(), name="platform-detail"),
]
