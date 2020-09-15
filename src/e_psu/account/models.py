from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, user_type=0):
        if not email:
            raise ValueError("User harus mempunyai email")
        if not username:
            raise ValueError("User harus mempunyai username")
        if not password:
            raise ValueError("User harus mempunyai password")
        print(password)

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password=password,
            username=username,
            user_type=1
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    ADMIN = 1
    PERWAKILAN = 2
    SKPD = 3
    WARGA = 4
    USER_TYPE_CHOICES = (
      (ADMIN, 'admin'),
      (PERWAKILAN, 'perwakilan'),
      (SKPD, 'skpd'),
      (WARGA, 'warga'),
    )

    email = models.EmailField(verbose_name="email", max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table= "kelola_account"
