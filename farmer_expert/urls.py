from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('farmersubmission/', views.farmer_query_submission, name = 'farmer_query_submission'),
    #path('thankyou/', views.Inquery_Submitted, name='Inquery_Submitted'),
    path('thankyou/expertfeedback/', views.expert_feedback_recieved, name='expert_feedback_recieved'),

    path('farmerquerieslist/', views.farmer_query_list, name='farmer_query_list'),
    path('farmerqueriesdetails/<int:id>', views.farmer_query_details, name='farmer_query_details'),



    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('farmerpage/', views.farmer, name='farmer'),
    path('expertpage/', views.expert, name='expert'),



     path('expert_reply/', views.expert_reply, name='expert_reply'),
     path('thankyouexpert/', views.Expert_Reply_Submitted, name='Expert_Reply_Submitted'),
     path('thankyoufarmer/', views.Farmer_request_Submitted, name='Farmer_request_Submitted'),

    ########## classify urls path

    path('disease/', views.disease, name='disease'),
    path('classify/', views.classify, name='classify'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)