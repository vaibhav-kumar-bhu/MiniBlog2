"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blog import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
admin.site.site_header='MiniBlog'
admin.site.index_title='Welcome to the MiniBlog Portal'
admin.site.site_title = "MiniBlog Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<int:id>/',views.updatepost,name='updatepost'),
    path('deletepost/<int:id>/',views.deletepost,name='deletepost'),
    path('addcomment/',views.addcomments,name='comment'),
    path('deletecomment/<int:sno>/',views.deletecomment,name='delete'),
    path('editcomment/<int:sno>/',views.editcomment,name='editcomment'),
    path('reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),

    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset_password_conf/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_comp/',auth_views.PasswordResetCompleteView.as_view(template_name='core/signinagain.html'),name='password_reset_complete'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



