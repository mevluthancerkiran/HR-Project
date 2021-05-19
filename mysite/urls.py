from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from firstPage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index, name="Homepage"),
    url('the_func', views.the_func, name="the_func"),

]
