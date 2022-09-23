"""TrishaAmman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mygoddess import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('goddess_temple/',views.goddess_temple,name='goddess_temple'),
    path('seva_edit/',views.editseva,name='seva_edit'),
    path('seva_delete/',views.deleteseva,name='seva_delete'),
    path('devotees/',views.devotees,name='devotees'),
    path('nayanathara_devotee/',views.nayanathara_devotee,name='nayanathara'),
    path('kajal_devotee/',views.kajal_devotee,name='kajal'),
    path('anushka_devotee/',views.anushka_devotee,name='anushka'),
    path('slaves/',views.slaves,name='slaves'),
    path('signup/',views.signup,name='signup'),
    path('add_profile/',views.user_add_profile,name='add_profile'),
    path('profile_detail/<int:id>/',views.profile_detail,name='profile_detail'),
    path('slaves_pics/<int:id>/',views.goddess_trisha_slaves,name='slave_pics'),
    path('accounts/login/',views.user_login,name='login'),
    path('accounts/logout/',views.user_logout,name='logout'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

