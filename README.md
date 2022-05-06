### Overview
This is a demo Django app that uses login.gov for authentication.
We're using a forked copy of the `mozilla-django-oidc` package (see https://mozilla-django-oidc.readthedocs.io/en/stable/index.html) and https://github.com/fecgov/mozilla-django-oidc

### Set up app in login.gov dashboard
See https://developers.login.gov/testing/#how-to-get-started and https://developers.login.gov/testing/#creating-a-public-certificate

### Set up virtualenv, install requirements
```
pyenv virtualenv 3.8.12 login-demo
pyenv activate login-demo
pip install -r requirements.txt
```

### Set env var
```
export OIDC_RP_CLIENT_ID="From login.gov"
```

### Generate private/public key, save to app/login.gov
See login.gov docs for generating these keys. Moving to S3 with https://github.com/fecgov/fecfile-web-api/issues/110

Save private key in a `vars.yml` file:

**vars.yml**
```yml
---
cert: |
  -----BEGIN PRIVATE KEY-----
  ...
  -----END PRIVATE KEY-----
```
**manifest-dev.yml:**
```yml
---
applications:
- name: login-demo
  route: login-demo-dev.app.cloud.gov
  buildpacks:
    - python_buildpack
  memory: 512M
  services:
    - login-demo-rds
    - login-creds
  env:
    DISABLE_COLLECTSTATIC: 1
    OIDC_RP_CLIENT_SECRET: ((cert))
```

Deploy the app with `cf push -f manifest-dev.yml --vars-file .vars.yml`

Manifests are additive-only, so I removed the cert from the manifest and it will persist unless the app gets deleted.

Source: cloud foundry slack channel: https://cloudfoundry.slack.com/archives/C032824SM/p1587642436080100

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

### Create database service
```
cf create-service aws-rds small-psql-redundant login-demo-rds
```

### Test on cloud.gov
https://login-demo.app.cloud.gov/simpleapp

### Create super user
```
cf ssh login-demo
/tmp/lifecycle/shell
cd mysite
./manage.py createsuperuser
```
