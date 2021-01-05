from django.urls import path,include
from .views import HomePageView ,PostDetailsView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/',PostDetailsView.as_view(), name='details'),
    path('new/',PostCreateView.as_view(), name = 'add' ),
    path('<int:pk>/edit/',PostUpdateView.as_view(), name = 'edit' ),
    path('<int:pk>/delete/',PostDeleteView.as_view(), name = 'delete' ),
    
]
    