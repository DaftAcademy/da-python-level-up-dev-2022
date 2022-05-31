# da-2022-example


## baza northwind
https://code.google.com/archive/p/northwindextended/downloads


## heroku-cli
https://devcenter.heroku.com/articles/heroku-cli


## Szczegóły jak zainstalować dockera
https://docs.docker.com/engine/install/


## Szczegóły jak zainstalować docker-compose (w przypadku większości systemów copose będzie już częścią dockera)
https://docs.docker.com/compose/install/


## jak uruchomić bazę lokalnie z docker-compose'a
`docker compose up -d postgres`  
ta komenda pobierze (jeśli jeszcze nie jest pobrany obraz) i uruchomi


## Skąd wziąć DATABASE_URI
DATABASE_URI autmatycznie zostanie dodane do zmiennych w aplkaji Heroku, ale jest tam niewłaściwa schema.  
postgres → postgresql


## dump db
`pg_dump --format=c --no-owner --no-acl -U postgres  > northwind.sql.dump`


## Restore db
heroku pg:backups:restore 'https://github.com/DaftAcademy-Python-LevelUP-Dev-2022/da-python-level-up-dev-2022/blob/main/4_T_jak_Tabela/dumps/northwind.sql.dump'  postgresql-silhouetted-07931 --app da-2021-example --confirm da-2021-example


## Generowanie modeli
`sqlacodegen 'postgresql://postgres:DaftAcademy@127.0.0.1:5555' > models.py`


## Lokalne uruchomienie apki
`SQLALCHEMY_DATABASE_URL="postgresql://postgres:DaftAcademy@127.0.0.1:5555/postgres" uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
postgresql://postgres:DaftAcademy@127.0.0.1:5555/postgres
`
