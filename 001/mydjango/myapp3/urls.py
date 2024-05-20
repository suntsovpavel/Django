from django.urls import path
from .views import about, hello, HelloView, year_post, MonthPost, post_detail, my_view, TemplIf, view_for, author_posts, post_full


urlpatterns = [
    path('hello/', hello, name='hello'),    # представление на основе функции
    path('hello2/', HelloView.as_view(), name='hello2'),  # представление на основе класса
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
