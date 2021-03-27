from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name = 'index'),

    #-------------------Launguages---------------------
    path('py/', views.python_file, name = 'python_file'),
    path('c/', views.c_file, name = 'c_file'),
    path('cpp/', views.cpp_file, name = 'cpp_file'),
    path('java/', views.java_file, name = 'java_file'),
    path('ds/', views.ds_file, name = 'ds_file'),
    path('php/', views.php_file, name = 'php_file'),


    #----------------Interview Portal----------------
    path('py_questions/', views.python_questions, name = 'python_questions'),
    path('c_questions/', views.c_questions, name = 'c_questions'),
    path('cpp_questions/', views.cpp_questions, name = 'cpp_questions'),
    path('java_questions/', views.java_questions, name = 'java_questions'),
    path('ds_questions/', views.ds_questions, name = 'ds_questions'),   
    path('php_questions/', views.php_questions, name = 'php_questions'),   
    path('html_questions/', views.html_questions, name = 'html_questions'),
    path('css_questions/', views.css_questions, name = 'css_questions'),
    path('js_questions/', views.js_questions, name = 'js_questions'),
    path('django_questions/', views.django_questions, name = 'django_questions'),   
    path('dbms_questions/', views.dbms_questions, name = 'dbms_questions'),



    #----------------User signup and login------------
    path('signup/', views.Signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('user/update/', views.edit_names, name = 'update_user'),


    # Forget Password
    # Change Password
    # if you singhed in then you can use change password but if you are not sign in then use password-reset option
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='movie/commons/change-password.html',
            success_url = '/va_tutorial/change-password-complete/'
        ),
        name='change_password'
    ),
    path('change-password-complete/',views.PasswordChangeComplete, name='change_password_complete'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='movie/commons/password-reset/password_reset.html',
             subject_template_name='movie/commons/password-reset/password_reset_subject.txt',
             email_template_name='movie/commons/password-reset/password_reset_email.html',
             success_url='/va_tutorial/password-reset/done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='movie/commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='movie/commons/password-reset/password_reset_confirm.html',
             success_url='/va_tutorial/password-reset-complete/'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='movie/commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),




    #----------------Footer Options------------
    path('report/', views.report, name='report'),
    path('privacy/', views.privacy, name='privacy'),
    path('term/', views.term, name='term'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name = 'contact'),
    path('copyright/', views.copyright, name = 'copyright'),
]