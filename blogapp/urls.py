from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('create/',views.create,name = 'create'),
    path('<int:pk>/update',views.update,name = 'update'),
    path('myblogs',views.myblogs,name='myblogs'),
    path('<int:pk>/delete',views.delete,name='delete')
]

