# contactPy
A MarieDB Python microservice baced web app to save phone numbers

MariaDB
  - This assumes MariaDB is installed. If not folllow these instructions: https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04
  - Install the pythion MariaDB connector: https://mariadb.com/docs/skysql/connect/programming-languages/python/install/

## Change the database credentials in contactApp.py:
```
    USER = "kenyon"
    DB = "kenyon"
    PASS="GambierOwls"
```
## Add a directory to your web directory:

sudo mkdir /var/www/html/contactPy/
sudo chown ubuntu /var/www/html/contactPy/

## Make and run
  - make
  - ./start.sh
