# EasyCoding (Django Blogging Website Project)

#Description about repository:
* This repository consists of all my django blogging project.It was made using Python3.8 + Django 3.0 and database is SQLite.Bootstrap was used for styling.
* There is a login and registration functionality included and post views is also included.
* Admin can post the blog post.Every authenticated user can comment and can reply to the comment on the admin post.
* Blog home post page is paginated list of all post.
* Non-authenticated users can see all blog post,but cannot comment on it.

Clone This Project:

*Make sure you have git installed.
https://github.com/n07tesh/EasyCoding.git

*Install Dependencies:
pip install -r requirements.txt

*Set Database (Make sure you are in the same directory as manage.py):
1.python manage.py makemigrations,
2.python manage.py migrate

*Create superuser: 
python manage.py createsuperuser

*After all these steps, you can start testing and developing this project.
