from celery import shared_task
from .models import Account
import datetime
from .automated_login import gmail_login  # Import your login function

@shared_task
def check_and_login():
    accounts = Account.objects.all()
    for account in accounts:
        if datetime.datetime.now() - account.last_login > datetime.timedelta(days=account.login_frequency):
            if account.platform == 'Gmail':
                gmail_login(account.username, account.password)
                account.last_login = datetime.datetime.now()
                account.save()
