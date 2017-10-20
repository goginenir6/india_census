# india_census
Gramener product test case
download this code from git by using this command in terminal

git clone https://github.com/goginenir6/india_census.git

I added enviroment folder also(env).
open terminal and go to the project source code. Then activate environment.
> source env/bin/acctivate

If it is not worked in your mahine please fallow below steps.
crete  virtual environment
> virtualenv env

Activate environment
>source env/bin/activate

Install all requirements librarys 
>pip install -r requirements.txt

creating and migrating db(dont forgot to create a schema in your machine if you are trying to connect your local db)
> python manage.py makemigrations

Migrate to data base.
>python manage.py migrate

Runserver 
>python manage.py runsserver

Test this link in your browser.
http://127.0.0.1:8000

I used google oauthlogin to go inside of my django project. After you can find questions and answers . I used only Jupyter
html fies to show the results. I have also attached the ipynb files also. in path "jupyter files/.ipynb".
