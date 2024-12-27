from django.urls import path
from forum import views

urlpatterns = [
    path('forum/', views.ForumListView.as_view(), name = 'forum-list'),
    path('forum/create/', views.ForumCreateView.as_view(), name = 'forum-create'),
    path('forum/delete/<int:pk>', views.ForumDeleteView.as_view(), name = 'forum-delete'),
    path('forum/edit/<int:pk>', views.ForumEditView.as_view(), name = 'forum-edit'),
    path('forum/detail/<int:pk>', views.ForumDetailView.as_view(), name = 'forum-detail'),
]