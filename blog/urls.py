from django.urls import path
from . import views

urlpatterns = [
    # path('', views.LoginView, name='login'),
    # path('', views.home, name='login_page'),
    path('', views.main_page, name='main_page'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
    # path('mainpage/', views.main_page, name='main_page'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # path('accounts/login/', views.LoginView, name='login'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # path('post/board/', views.post_bulletin, name='post_board'),
    path('post/board/', views.listing, name='post_board'),
]