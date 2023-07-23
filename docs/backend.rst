Backend
=====

Django
----------------
This app is built using `Django <https://www.djangoproject.com/>`_, a Python-based 
framework for developing web applications. Django does almost all of the heavy lifting when 
it comes to basic functionality and security, which allows me to spend more time on the core 
application logic. 

A few Django features of particular value to me are:

#. An active developer community, which means many components are available as packages. For 
   example, this app uses packages for handling data import/export, optimizing hierarchical data 
   structures for the location feature, and providing an audit log.
#. The inclusion of an object-relational mapping (ORM) tool, which represents database models 
   as Python objects. This makes it easier to manage, query, and migrate data, all without writing 
   raw SQL queries.
#. The usage of Python as its language, which results in highly readable and maintainable code. 
   When used for scientific applications, the code can also be understood by scientists familiar 
   with Python, and their pre-existing Python scripts can easily integrated into the app.

PostgreSQL
----------------
Benching and other LIMS vendors often use PostgreSQL for their backend database, and I have 
done the same for my demo. 

While this project does not need most of the advanced features PostgreSQL provides, such as 
indexing and query optimization, these features could be very important for a more developed 
LIMS. Choosing PostgreSQL over a simpler database like MySQL could mean avoiding a migration 
in the future if the need arises, which I believe is worth some additional overhead. 
