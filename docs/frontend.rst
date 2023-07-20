Frontend
=====

Django Admin
------------
Django provides an admin interface out of the box - one of its strengths compared to other 
web frameworks. This admin interface automatically generates tables and forms for CRUD 
operations on the database tables the developer defines. 

.. image:: images/django-admin.png
   :width: 600

The admin site is typically used only by site administrators and staff. A typical use case 
might be content management for the site, as well as interaction with the default User and 
Group tables defined by Django. 

However, for a straightforward CRUD app like this LIMS, Django Admin provides most of the 
necessary functionality already. Rather than designing a UI from scratch (which I have done 
for other projects using Vue and Bootstrap), this demo starts with Django's admin page as 
the base, and adds a few extra features on top.

Unfold Admin
----------------
The default styling for Django's admin site is perfectly functional, but leaves a lot to be 
desired in terms of aesthetics when used as the main page of an app. 

To improve the styling, this site uses `Unfold Admin <https://unfoldadmin.com/>`_, a theme 
designed for Django's admin site. This theme is written using Tailwind CSS, and can be easily 
extended and customized. 
