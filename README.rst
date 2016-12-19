djangocms-smart-mirror
======================

A collection of django CMS addons to support a smart mirror project. Its a
(currently small) set of CMS Plugins that could be arranged on a single page 
intended to be the display for a Smart Mirror.

This project is based upon django CMS.

To get this up-and-running quickly:

1. Make a virtualenv for Python 2.7 (may work under 3.5 too)
2. `pip install -r requirements`
3. `./manage.py migrate`
4. `./manage.py createsuperuser`
5. `./manage.py runserver`
6. Login and create a new page
7. I recommend installing the Bootstrap "Row" plugin with 3 or 4 rows of equal
   column width (4 or 3 columns respectively)
8. In the first column created, add the "Smart Mirror Clock" plugin
9. In the last column created, add the "Smart Mirror Weather" plugin (NOTE: 
   You will need your own, free Weather Underground API key)
