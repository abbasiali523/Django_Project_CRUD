from django.urls import path
from .views import index  , post_delete , post_detail , post_edit
app_name = 'blog'
urlpatterns = [
    path('',index,name='index' ),
    path('post/<int:pk>/delete/', post_delete, name='post-delete'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:id>/edit/', post_edit, name='post-edit'),

]
