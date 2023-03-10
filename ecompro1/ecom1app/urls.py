from django.urls import path
from . import views
app_name='ecom1app'

urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:cslug>/',views.allprodcat,name='products_by_category'),
    path('<slug:cslug>/<slug:productslug>/',views.prodetail,name='procatdetail'),
]