# untrumpt
A Django app that helps people find constructive ways to fight a Trump presidency

### Getting Started
Clone the repo

Make sure you have VirtualBox and Vagrant on your computer. Don't `vagrant up` yet!

Copy `app.env.example` over to `app.env` and:
- Update the database username and password if you want to (database name, host, and port should be fine for now)
- Generage a Django `SECRET_KEY` [here](http://www.miniwebtool.com/django-secret-key-generator/) and paste it in.

Now you can `vagrant_up`.

Once all that runs, login to the vagrant box (default username is `vagrant@localhost` with port 2222; default pass is `vagrant`. Type:
```
cd /vagrant
python manage.py createsuperuser
```

Follow the prompt to create your Django admin username and password.

```
python manage.py migrate
```

Now go to `http://localhost:18000` and it's a site!
