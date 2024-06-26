from .notifications import send_sms_notification

@shared_task
def check_and_login():
    accounts = Account.objects.all()
    for account in accounts:
        if datetime.datetime.now() - account.last_login > datetime.timedelta(days=account.login_frequency):
            if account.platform == 'Gmail':
                gmail_login(account.username, account.password)
                account.last_login = datetime.datetime.now()
                account.save()
                send_sms_notification(account.user.profile.phone_number, f"Logged into {account.platform} account {account.username}")
