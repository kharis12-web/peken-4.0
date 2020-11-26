from django .urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index,name ='index'),
    path('regristration', views.profile_reg,name='reg'),
    path('login/', views.profile_login,name='login'),
    path('logout/', views.profile_logout,name='logout'),
    path('page1/', views.login_page,name='page1'),


    #urls reser password
    
    path('password_reset', auth_views.passwordResetView.as_view(),name='password_reset'),
    path('password_reset/done', auth_views.passwordResetDoneView.as_view(),name='password_reset/done'),
    path('reset/<uidb64>/<token>/', auth_views.passwordResetConfirmView.as_view(),name='password_reset_confrim'),
    path('reset/done', auth_views.passwordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
