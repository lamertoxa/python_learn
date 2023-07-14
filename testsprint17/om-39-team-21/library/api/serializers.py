from rest_framework import  serializers
from authentication.models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'middle_name','last_name','email','password','created_at',  'role', )
        read_only_fields = ['id','role']
        extra_kwargs = {
            'password': {'write_only':True},
            'email': {'write_only': True}
        }
    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password = make_password(validated_data['password'])
        )
        return user
class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','book_id','user_id','created_at','end_at','plated_end_at')
        read_only_fields = ['id','user_id']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','user','user_id','book_id', 'book', 'created_at', 'end_at', 'plated_end_at')
        read_only_fields = ['id','user_id','created_at']
        extra_kwargs = {

            'book': {'write_only': True},
            'user': {'write_only': True}
        }

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic', 'books')

    def create(self, validated_data):
        author = Author.objects.create(
            name=validated_data['name'],
            surname=validated_data['surname'],
            patronymic=validated_data['patronymic'],
        )
        if validated_data['books']:
            for book_id in validated_data['books']:
                author.books.add(book_id)
        return author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'count', 'year_of_publication', 'date_of_issue', 'authors')

    def create(self, validated_data):
        book = Book.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            count=validated_data['count'],
            year_of_publication=validated_data['year_of_publication'],
            date_of_issue=validated_data['date_of_issue']
        )
        if validated_data['authors']:
            for author_id in validated_data['authors']:
                book.authors.add(author_id)
        return book
