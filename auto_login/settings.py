CELERY_BEAT_SCHEDULE = {
    'check-and-login-every-day': {
        'task': 'accounts.tasks.check_and_login',
        'schedule': 86400.0,  # Check every day
    },
}
