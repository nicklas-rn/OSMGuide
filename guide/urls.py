from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tactics/counter-tactics/', views.counter_tactics, name='counter-tactics'),
    path('tactics/overall-tactics/', views.overall_tactics, name='overall-tactics'),
    path('tactics/<title>/', views.counter_tactic_detail, name='tactics-detail'),
    path('beginners_guide/', views.beginners_guide, name='beginners_guide'),
    path('players/', views.players, name='players'),
    path('tips/', views.tips, name='tips'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('thank_you/', views.thank_you, name='thank_you'),

]