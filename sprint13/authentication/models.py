from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
import datetime
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.core.validators import validate_email

import time

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class CustomUser(AbstractBaseUser):
    """
        This class represents a basic user. \n
        Attributes:
        -----------
        param first_name: Describes first name of the user
        type first_name: str max length=20
        param last_name: Describes last name of the user
        type last_name: str max length=20
        param middle_name: Describes middle name of the user
        type middle_name: str max length=20
        param email: Describes the email of the user
        type email: str, unique, max length=100
        param password: Describes the password of the user
        type password: str
        param created_at: Describes the date when the user was created. Can't be changed.
        type created_at: int (timestamp)
        param updated_at: Describes the date when the user was modified
        type updated_at: int (timestamp)
        param role: user role, default role (0, 'visitor')
        type updated_at: int (choices)
        param is_active: user role, default value False
        type updated_at: bool

    """



    id =models.BigAutoField(editable=False,primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True,max_length=100)
    password = models.CharField(max_length=1001)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role= models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=False)



    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """

        return ', '.join([f"'{key}': '{value}'" if not isinstance(value,int) else f"'{key}': {value}" for key, value in self.to_dict().items() ])
    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(user_id):
        """
        :param user_id: SERIAL: the id of a user to be found in the DB
        :return: user object or None if a user with such ID does not exist
        """
        return CustomUser.objects.filter(id = user_id).first()

    @staticmethod
    def get_by_email(email):
        """
        Returns user by email
        :param email: email by which we need to find the user
        :type email: str
        :return: user object or None if a user with such ID does not exist
        """
        return CustomUser.objects.filter(email=email).first()
    @staticmethod
    def delete_by_id(user_id):
        """
        :param user_id: an id of a user to be deleted
        :type user_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return True
        except ObjectDoesNotExist :
            return False
    @staticmethod
    def create(email, password, first_name=None, middle_name=None, last_name=None):
        """
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param email: email of a user
        :type email: str
        :param password: password of a user
        :type password: str
        :return: a new user object which is also written into the DB
        """

        if len(first_name)<21 and len(middle_name)<21 and len(last_name)<21 and not CustomUser.objects.filter(email=email).first() :
            user = CustomUser(first_name=first_name, email=email, password=password, middle_name=middle_name,
                              last_name=last_name)
            user.save()
            try:
                validate_email(email)
            except ValidationError:
                return None
            return user

    def to_dict(self):
        """
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at, user is_active
        :Example:
        | {
        |   'id': 8,
        |   'first_name': 'fn',
        |   'middle_name': 'mn',
        |   'last_name': 'ln',
        |   'email': 'ln@mail.com',
        |   'created_at': 1509393504,
        |   'updated_at': 1509402866,
        |   'role': 0
        |   'is_active:' True
        | }
        """

        return   {
        'id': self.id,
        f'first_name': f'{self.first_name}',
        f'middle_name': f'{self.middle_name}',
        f'last_name': f'{self.last_name}',
        f'email': f'{self.email}',
        f'created_at': int(datetime.datetime.timestamp(self.created_at)),
        f'updated_at': int(datetime.datetime.timestamp(self.updated_at)),
        f'role': self.role,
        f'is_active': self.is_active }
    def update(self,
               first_name=None,
               last_name=None,
               middle_name=None,
               password=None,
               role=None,
               is_active=None):
        """
        Updates user profile in the database with the specified parameters.\n
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param password: password of a user
        :type password: str
        :param role: role id
        :type role: int
        :param is_active: activation state
        :type is_active: bool
        :return: None
        """
        check_string = [first_name, middle_name, last_name]
        update_field = {'first_name':first_name, 'middle_name':middle_name,
                        'last_name':last_name,'password':password,'role':role,'is_active':is_active}
        if all([len(item_string) < 21 for item_string in check_string if item_string != None]):
            user = CustomUser.objects.get(id=self.id)
            for item in update_field:
                if not item is None:
                    user.__setattr__= item
            user.save()


    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all users
        """

        return CustomUser.objects.all()

    def get_role_name(self):
        """
        returns str role name
        """

        return ROLE_CHOICES[self.role][1]