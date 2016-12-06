cd /vagrant
sudo apt-get update
sudo apt install -y libpq-dev python-dev
sudo apt-get install -y python-pip
. ./app.env

sudo apt-get install -y postgresql postgresql-contrib
echo "psql -c \"CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';\"" | sudo -i -u postgres
echo "psql -c \"CREATE DATABASE ${DB_NAME};\"" | sudo -i -u postgres
echo "psql -c \"GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};\"" | sudo -i -u postgres
