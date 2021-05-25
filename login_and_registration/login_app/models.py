from django.db import models
import bcrypt
import re	# the regex module

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = "First name must be longer than 3 letters."
        if len(form['last_name']) < 2:
            errors['last_name'] = "Last name must be longer than 3 letters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        email_check = self.filter(email=form['email']) # checks to make sure its unique
        if email_check:
            errors['email'] = "Email already in use"
        # password validation
        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors



    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw
        )

    def authenticate(self, email, password):
        return False

        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()