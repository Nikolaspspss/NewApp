from django.urls import path

from .views import PostList, PostDetail, PostSearch, PostUpdate, PostDelete, PostCreate, CategoryListView, subscribe

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='detail_post'),
   path('search/', PostSearch.as_view(), name='news_search'),
   path('create/', PostCreate.as_view(), name='create_post'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]