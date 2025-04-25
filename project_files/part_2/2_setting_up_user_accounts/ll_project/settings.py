#add the accounts app to the installed apps

INSTALLED_APPS = [
    # My apps
    'learning_logs',
    'accounts',
]


#login and logout redirect setting. add this code to the end of the file
# My settings.
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'


