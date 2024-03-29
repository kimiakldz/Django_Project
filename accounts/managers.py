from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):  # 1.

    def create_user(self, email, first_name, last_name, password=None):
        """
                Creates and saves a User with the given email,first name, last name and password.
        """
        if not email:
            raise ValueError('Users must have an email address!!')

        if not first_name:
            raise ValueError('user must have first name!!')

        if not last_name:
            raise ValueError('user must have last name!!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
                Creates and saves a superuser with the given email,first name, last name and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        """
        Creates and saves a staff user with the given email,first name, last name and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user