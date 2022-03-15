### Overview
This is a demo Django app that uses login.gov for authentication.
We're using the `mozilla-django-oidc` package (see https://mozilla-django-oidc.readthedocs.io/en/stable/index.html)



### Set up virtualenv, install requirements
```
pyenv virtualenv 3.8.12 login-demo
pyenv activate login-demo
pip install -r requirements.txt
```

### Set env vars
```
export OIDC_RP_CLIENT_ID="From login.gov"
export OIDC_RP_CLIENT_SECRET=`cat private.pem`  # see login.gov docs on how to generate
```

### Run the site
```
cd mysite
gunicorn --bind 0.0.0.0:8080 mysite.wsgi -w 9 -t 200
```

### Test login
http://0.0.0.0:8080/simpleapp

### Set redirect URI in login.gov
See docs: https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html#acquire-a-client-id-and-client-secret

https://login-demo.app.cloud.gov/oidc/callback/

### Deploy to cloud.gov
```
cf login --sso
```
target fec-fecfileonline-prototyping, dev space
```
cf push -f manifest-dev.yml
```

### Set env vars in cloud.gov dashboard
```
# In dashboard
OIDC_RP_CLIENT_ID="From login.gov"
OIDC_RP_CLIENT_SECRET=`cat private.pem`  # see login.gov docs on how to generate

# In terminal
cf restage login-demo
```

### Test on cloud.gov
https://login-demo.app.cloud.gov/simpleapp
