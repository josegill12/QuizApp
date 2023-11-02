from django.urls import path
from .views import QuizListCreate, QuizDetailUpdateDelete, CreateQuestion

urlpatterns = [
    path('quizzes/', QuizListCreate.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizDetailUpdateDelete.as_view(), name='quiz-detail-update-delete'),
    path('quizzes/<int:pk>/questions/', CreateQuestion.as_view(), name='create-question'),
]