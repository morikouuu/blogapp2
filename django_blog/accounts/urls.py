from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/',views.ProfileView.as_view(), name ='profile'),
    path('author/<int:pk>/',views.AuthorView.as_view(),name = 'author'),
    path('update/<int:pk>',views.UpdateView.as_view(), name ='update'),
    path('logged_out_confirm/',views.LoggedoutconfirmView.as_view(),name='logged_out_confirm'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)