cd /vagrant
sudo pip install -r requirements.txt
. ./app.env
python manage.py runserver 0.0.0.0:8000  > /dev/null 2>&1 &
