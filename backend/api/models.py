from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.contrib.auth.models import UserManager

class UserManager(BaseUserManager):
    def create_user(self, email,  full_name, phone_number, company_name, job_title, password=None):
        """
            CREATES AND SAVES A USER WITH THE GIVEN CREDENTIALS
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
  
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_staffuser(self,  email, password, full_name, phone_number, company_name, job_title):
        """
            CREATES AND SAVES A STAFF USER WITH THE GIVEN CREDENTIALS
        """

        user = self.create_user(
                email,
                password=password,
                full_name=full_name,
                phone_number=phone_number,
                company_name=company_name,
                job_title=job_title,
            )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password, full_name, phone_number, company_name, job_title):
        """
            CREATES AND SAVES A SUPER USER WITH THE GIVEN CREDENTIALS
        """
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            phone_number=phone_number,
            company_name=company_name,
            job_title=job_title,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number', 'company_name', 'job_title', 'password']

    def get_full_name(self):
        return self.full_name

    def get_job_title(self):
        return self.job_title

    def get_company_name(self):
        return self.company_name

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email
    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    
    
    @property
    def is_staff(self):
        return self.staff

    def is_admin(self):
        return self.admin

    object = UserManager()


    


        
