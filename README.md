## Run the project on the local machine
-run script
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py runserver
```
- Navgiate http://127.0.0.1:8000/
- Also, you can experiement the API on django rest framework standard UI.(http://127.0.0.1:8000/api/books/)
- You will see the Swagger UI

## Filter Feature by genere
- you have to provide the genere filter data on the query parameters <br/>
  for example: http://127.0.0.1:8000/api/books/?genere=Fantasy&genere=Horror&genere=LF <br/>
  then, by default, we list the book with ```"OR"``` operator  for genere field. that is; list all the books whose genere is `Fantasy` or `Horror` or `LF`.
- However, if you specify `and` query param as `"true"` , <br/>
  It lists the books wit `AND` operator. example url: `http://127.0.0.1:8000/api/books/?genere=Fantasy&genere=Horror&genere=LF`&and=true`
