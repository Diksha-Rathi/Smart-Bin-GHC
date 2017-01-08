#Smart Bin GHCI

The Smart Bin project of GHC Women Hackathon 2015.

View demo video: [Desktop View](https://youtu.be/UP_KwSg6GIk) | [Mobile View](https://youtu.be/PT_DKmhWBwI)

* Clone the source.

```sh
$ git clone git@github.com:diksha-rathi/Smart-Bin-GHC.git
```

* Install postgresql.

* Create a database with the name 'smart_bin'.

* Edit the following lines in smart_bin/settings.py with your username and password for the database.

```sh
'USER': 'your_username',
'PASSWORD': 'your_password',
```

* Create migrations for the models.

```sh
$ python makemigrations
```

## Run the project

```sh
$ cd Smart-Bin-GHC
$ python manage.py runserver
```

##License

[MIT](https://github.com/Diksha-Rathi/Smart-Bin-GHC/blob/master/LICENSE)

#### Thanks for creating the following:

* [bootstrap-datepicker](https://github.com/uxsolutions/bootstrap-datepicker)
