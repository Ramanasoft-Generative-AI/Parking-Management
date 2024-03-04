from  django.urls import path

from .views import DisplayItems
from . import views
from .views import ManageVehicle

urlpatterns = [
               path('display/', views.DisplayItems, name='Display'),
               path('manage/', views.ManageVehicle, name= 'Manage'),
               path('add/', views.addCategory, name= 'addCat'),
               path('add1/', views.Vehicleadd, name= 'Vehicle'),
               path('del/<int:pk>', views.delete, name='delete'),
               path('up/<int:pk>', views.update, name='update'),
               path('deactive/<int:pk>',views.deactive, name='deactive'),
               path('leaved/<int:pk>', views.leaved, name='leaved'),
               path('parked/<int:pk>', views.parked, name='parked'),
               path('active/<int:pk>',views.active, name='active'),
               path('search/', views.search, name='search'),
               path('managesearch/', views.manageSearch, name='managesearch'),
               path('categorysearch/', views.categorySearch, name='categorysearch'),
               path('dashboard/', views.dashboard, name='dashboard'),
               path('reports/', views.reports, name='reports'),
               path('accountsettings/', views.accountsettings, name='accountsettings'),
               path('register/', views.register, name='register'),
               path('', views.login, name='login'),
               path('logout/', views.logout, name='logout'),
]