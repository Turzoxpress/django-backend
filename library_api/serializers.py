from rest_framework import serializers
from .models import Book, Member, Loan


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "isbn",
            "title",
            "author",
            "published_year",
            "available_copies",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "id",
            "membership_no",
            "full_name",
            "email",
            "joined_at",
            "created_at",
        ]
        read_only_fields = ["id", "joined_at", "created_at"]


class LoanSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source="book"
    )
    member_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source="member"
    )

    class Meta:
        model = Loan
        fields = [
            "id",
            "book_id",
            "member_id",
            "loan_date",
            "due_date",
            "returned_date",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, attrs):
        loan_date = attrs.get("loan_date", getattr(self.instance, "loan_date", None))
        due_date = attrs.get("due_date", getattr(self.instance, "due_date", None))
        returned_date = attrs.get("returned_date", getattr(self.instance, "returned_date", None))

        if loan_date and due_date and due_date < loan_date:
            raise serializers.ValidationError({"due_date": "due_date cannot be earlier than loan_date"})
        if returned_date and loan_date and returned_date < loan_date:
            raise serializers.ValidationError({"returned_date": "returned_date cannot be earlier than loan_date"})
        return attrs
