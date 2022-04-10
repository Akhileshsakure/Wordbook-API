from django.urls import include, path, re_path
from .views import WordsList, WordsCreate, WordsRetrieve, WordsUpdate, WordsDelete

urlpatterns = [
    path('add/',WordsCreate.as_view(), name = 'add-word'),
    path('',WordsList.as_view()),
    path('details/<str:word>/', WordsRetrieve.as_view()),
    path('update/<int:pk>/', WordsUpdate.as_view()),
    path('delete/<int:pk>/', WordsDelete.as_view())
]