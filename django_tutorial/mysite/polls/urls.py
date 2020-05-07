'''

The next step is to point the root URLconf at the polls.urls module. 
In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list

'''



from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]