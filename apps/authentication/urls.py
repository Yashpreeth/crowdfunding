from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.home import views 
from apps.home.views import rate

from .views import user_login, signup,activate ,user_logout ,EditProfile, profile ,emailPasswordReset ,ResetPasswordLink ,ResetPassword , deleteAccount


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login', user_login, name="login"),
    path('register', signup, name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,18})/',
         activate, name='activate'),
    path("logout", user_logout, name="logout"),
    path("profile" , profile , name="profile"),
    path('edit/profile', EditProfile, name="editProfile"),
    path('emailReset', emailPasswordReset, name="emailReset"),
    path('ResetPasswordLink/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,18})/',
         ResetPasswordLink, name='ResetPasswordLink'),
    path('passwordReset/<int:id>', ResetPassword, name="passwordReset"),
    path('DeleteAccount', deleteAccount, name="deleteAccount"),
    path('create-project/', views.create_new_project, name='create_project'),
    path('search-result/', views.search, name='search'),
    path('projects/tag/<int:tag_id>/', views.get_tag_projects, name='get_tag_projects'),
    path('project-details/<int:project_id>/', views.show_project_details, name='project_details'),
    path('project-details/<int:project_id>/comment/', views.create_comment, name='create_comment'),
    path('project-details/<int:comment_id>/reply/', views.create_comment_reply, name='create_comment_reply'),
    path('project-details/<int:project_id>/donate/', views.donate, name='donate'),
    path('<int:project_id>/rate/', views.rate, name='project_rate'),
    path('project-details/<int:project_id>/report/', views.add_report, name='create_report'),
    path('project-details/<int:comment_id>/report_comment/', views.add_comment_report, name='create_comment_report'),
    path('projects/category/<int:category_id>/', views.get_category_projects, name='get_category'), 
    path('category_form/', views.add_category, name='create_category'),
    path('projects/featured/', views.get_featured_projects, name='featured_projects'),
    path('projects/', views.all_projects, name='all_projects'),
    path('project-details/<int:project_id>/cancel/', views.cancel_project, name='cancel_project'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
