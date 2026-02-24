from django.urls import path
from .views import (
    BookListCreateAPIView, BookDetailAPIView,
    MemberListCreateAPIView, MemberDetailAPIView,
    LoanListCreateAPIView, LoanDetailAPIView
)

urlpatterns = [
    path("books", BookListCreateAPIView.as_view(), name="book-list-create"),
    path("books/<int:book_id>", BookDetailAPIView.as_view(), name="book-detail"),

    path("members", MemberListCreateAPIView.as_view(), name="member-list-create"),
    path("members/<int:member_id>", MemberDetailAPIView.as_view(), name="member-detail"),

    path("loans", LoanListCreateAPIView.as_view(), name="loan-list-create"),
    path("loans/<int:loan_id>", LoanDetailAPIView.as_view(), name="loan-detail"),
]
