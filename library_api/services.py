from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import Book, Member, Loan


class BookService:
    @staticmethod
    def list_queryset():
        return Book.objects.all().order_by("-id")

    @staticmethod
    def get(book_id: int) -> Book:
        return get_object_or_404(Book, pk=book_id)

    @staticmethod
    @transaction.atomic
    def create(validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update(instance: Book, validated_data: dict) -> Book:
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    @staticmethod
    @transaction.atomic
    def delete(instance: Book):
        instance.delete()


class MemberService:
    @staticmethod
    def list_queryset():
        return Member.objects.all().order_by("-id")

    @staticmethod
    def get(member_id: int) -> Member:
        return get_object_or_404(Member, pk=member_id)

    @staticmethod
    @transaction.atomic
    def create(validated_data: dict) -> Member:
        return Member.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update(instance: Member, validated_data: dict) -> Member:
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    @staticmethod
    @transaction.atomic
    def delete(instance: Member):
        instance.delete()


class LoanService:
    @staticmethod
    def list_queryset():
        return Loan.objects.select_related("book", "member").all().order_by("-id")

    @staticmethod
    def get(loan_id: int) -> Loan:
        return get_object_or_404(Loan.objects.select_related("book", "member"), pk=loan_id)

    @staticmethod
    @transaction.atomic
    def create(validated_data: dict) -> Loan:
        return Loan.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update(instance: Loan, validated_data: dict) -> Loan:
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    @staticmethod
    @transaction.atomic
    def delete(instance: Loan):
        instance.delete()
