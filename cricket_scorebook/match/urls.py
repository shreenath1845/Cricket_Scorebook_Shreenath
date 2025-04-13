from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Serve the HTML page
    path('save-match/', views.save_match, name='save_match'),  # Save match API
    path('delete-match/<int:match_id>/', views.delete_match, name='delete_match'),
    path('load-match/<int:match_id>/', views.load_match, name='load_match'),
    path('get-saved-matches/', views.get_saved_matches, name='get_saved_matches'),

]
