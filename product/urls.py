from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('my-product/<slug:product_slug>/', views.MyProductDetail.as_view()),
    path('my-auction/', views.MyAuction),
    path('create-auction/', views.CreateAuction),
    path('bid/', views.CreateBid),
    path('question/', views.CreateQuestion),
    path('answer/', views.CreateAnswer),
    path('getquestion/<slug:product_slug>/', views.getQuestions),
    path('sendmail/<slug:product_slug>/', views.sendmail ),
    path('search/', views.searchlist ),
    path('getanswer/<slug:product_slug>/', views.getAnswers)
    #path('<int:pk>', views.ProductDetail.as_view()),
]