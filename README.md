# Catch a Dog - Advanced Zoophysiotherapy & Fitness

My inspiration for creating this Django project was my sister's profession. She is a physiotherapist for dogs and cats. I wanted to create a website where pet owners can find the information they need to know about therapy she is providing. Another important thing is the ability to read other people's opinions and comments, as well as add your own after logging in.

![responsive mockup](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/responsive_kezrms.png)

[Link to live site](https://catch-a-dog-99383fa22fc6.herokuapp.com)

## Table of Contents

- [User Experience(UX)](#user-experience(UX))
  - [Agile](#agile)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Database Design](#database-deign)
  - [Database Model](#database-model)
  - [Custom Model](#custom-model)
  - [CRUD](#crud)
- [Testing](#testing)
  - [Validator testing](#validator-testin)
  - [Lighthouse](#lighthouse)
  - [Other browsers](#other-browsers)
  - [Different screen sizes](#different-screen-sizes)
  - [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)     
- [Credits](#credits)     
  - [Content](#content)     
  - [Media](#media)     
   

## User Experience(UX)
### Agile

## Features
### Existing Features
Navigation Bar
- Navigation bar is available on all pages and includes clickable logo and nav links.
- Allows to easily move between pages.
- Different links visible for authenticated and unauthenticated users
- Collapsible burger menu with drop-down on small to medium screens
- Active link is black, hovered icon is black and underlined, not active link is white

![nav.loggedout](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965453/catch%20a%20dog%202/navbar1_rwretr.png)
![nav.loggedin](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/navbar_ehlcuq.png)
![burger.menu](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965650/catch%20a%20dog%202/burger_kiiei6.png)
![burger.menu1](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965650/catch%20a%20dog%202/burger1_uyz8zp.png)

Register
- Allows user to create an account
- Username, password and password confirmation are required, email (optional)

![Sign up](https://res.cloudinary.com/dguqjbr12/image/upload/v1722967351/catch%20a%20dog%202/register_ey3cfy.png)

Login
- For registered already user
- Username and password required
- Contains "Remember me" option
- After signed in, user see confirmation
- When username or password are incorrect, user will be informed

![Sign in](https://res.cloudinary.com/dguqjbr12/image/upload/v1722967346/catch%20a%20dog%202/login_qj1tnr.png)

Logout
- After user clicks on logout link in nav bar, will see confirm form
- Then user will be redirected to home page with confirmation message about being signed out

![sign out](https://res.cloudinary.com/dguqjbr12/image/upload/v1722967343/catch%20a%20dog%202/logout_phtw7l.png)

Contact
- User can send a mesage using contact form
- After sending message user will see confirmation on success page

![contact](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965265/catch%20a%20dog%202/contact_t2pwtf.png)
![success](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965269/catch%20a%20dog%202/success_vtribd.png)


Add new review
- An authenticated user from nav bar can navigate to add review page
- Admin can delete and edit user's reviews
- After adding review and clicking Submit button will see confirmation
- User can delete or edit and update own review
- Confirmation message about delete and update will be shown to a user
- After clicking edit button under review, user can see on right side form with review for editing

![add review](https://res.cloudinary.com/dguqjbr12/image/upload/v1711366236/catch%20a%20dog%20readme/add.review1_fjpcno.png)
![review submitted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711373137/catch%20a%20dog%20readme/review.submitted_ijewzh.png)
![delete review](https://res.cloudinary.com/dguqjbr12/image/upload/v1722971150/catch%20a%20dog%202/review.delete_hekb37.png)
![review deleted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711373125/catch%20a%20dog%20readme/review.deleted_qgjp8n.png)
![edit review](https://res.cloudinary.com/dguqjbr12/image/upload/v1722967848/catch%20a%20dog%202/review.edit_mkzcck.png)
![review updated](https://res.cloudinary.com/dguqjbr12/image/upload/v1722967846/catch%20a%20dog%202/review.updated_co82vs.png)

Home page
- Includes welcome paragraph with instruction and short introduction to website
- Below each user can see reviews in order from the newest
- Paginated list of reviews
- User can click each review to see details in separately page

![home](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/home_zjchzu.png)

Review detail
- User even not registered can open single review on separate page to see it in detail
- Each page displays review with author, date and time of updatig and number of comments
- User also can see all attached to review comments and by who and when were written

![review detail](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/review.comment_gtxmul.png)
![review with comments](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/review.comment.logout_p789tg.png)

Comments
- Only authenticated user can add comment
- User can delete or edit and update own comment
- Confirmation message about delete and update will be shown to a user

![comments form](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359058/catch%20a%20dog%20readme/comments_zcxgei.png)


![comment updated](https://res.cloudinary.com/dguqjbr12/image/upload/v1711375606/catch%20a%20dog%20readme/comment.updated_vmobot.png)

![comment deleted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711375597/catch%20a%20dog%20readme/comment.deleted_bhqcfn.png)

Footer
- The Footer section includes links to different social media sites like Facebook, Instagram or YouTube.
- Can be found on each page.
- Each link will open to a new tab.

![footer](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359023/catch%20a%20dog%20readme/footer_h5fyu6.png)

About page
- "About Me" section containing information about my sister's profession and qualifications
- User can see what she is gradueted and what courses she completed
- User sees which treatment and prices she is offering 
- Section with email address and social media through which user can contact
- A few photos from therapy with dog patients

![about](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965265/catch%20a%20dog%202/about_kevqdv.png)
![offer](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965265/catch%20a%20dog%202/about1_sa858x.png)
![gallery](https://res.cloudinary.com/dguqjbr12/image/upload/v1722965266/catch%20a%20dog%202/about2_rets2j.png)

### Future Features

## Database Design
### Database Model

The database model diagram was designed using [draw.io](https://app.diagrams.net/) 

![ERD](https://res.cloudinary.com/dguqjbr12/image/upload/v1711357059/catch%20a%20dog%20readme/ERD_hc8bp8.png)

### Custom Model

To build my models, I followed the walkthrough project created by the Code Institute and adapted for my project's requirements.
I added required Custom Model not covered in the walkthrough - Reviews Model so each authenticated user can add own review.

### CRUD
The CRUD principle I did for my original Reviews Model and Comment Model. Admin is able to delete and edit user's reviews and comments.

CRUD Reviews Model:

Create: An authenticated user can create own review

Read: A user can see and read own and other users' reviews

Update: An authenticated user can edit and update own reviews

Delete: An authenticated user can delete own reviews

CRUD Comment Model:

Create: An authenticated user can comment any review

Read: A user can see and read own and other users' comments

Update: An authenticated user can edit and update own comments

Delete: An authenticated user can delete own comments


Features visualized here [Existing Features](#existing-features)

## Testing
### Validator testing

HTML W3C validator

- Home page

![errors home](https://res.cloudinary.com/dguqjbr12/image/upload/v1711398628/catch%20a%20dog%20readme/html.home_viflfq.png)

Stray end 'div' tag and 'p' element applies to a review added by a user and I can't locate and fix it.

- Add review page

![errors add review](https://res.cloudinary.com/dguqjbr12/image/upload/v1711398616/catch%20a%20dog%20readme/html.add.review_npisnz.png)

No errors

- Reviews detail

![errors reviews detail](https://res.cloudinary.com/dguqjbr12/image/upload/v1711395766/catch%20a%20dog%20readme/html.reviews.detail_up6vsu.png)

For solving problem with duplicate ID I just changed value. I removed review_id from 'div' element.

![errors reviews detail1](https://res.cloudinary.com/dguqjbr12/image/upload/v1711395770/catch%20a%20dog%20readme/html.reviews.detail1_dmceww.png)

Error with review_id exist becausse each review has own number so I had to left this. 

- About me page

![errors about](https://res.cloudinary.com/dguqjbr12/image/upload/v1711392832/catch%20a%20dog%20readme/html.about_d5wmha.png)

To fix this errors I removed 'br' tags from line where it is marked. Size for logo in nav bar I setted up in css file. I removed context from 'ul' element and one end of 'p' tag.

![errors about1](https://res.cloudinary.com/dguqjbr12/image/upload/v1711392840/catch%20a%20dog%20readme/html.about1_vjwr5t.png)

The 'font' element, used to define the font face, size and color is no longer valid in HTML5. Instead, I should style in but content was written in admin panel.

- Contact us

No errors or warnings


CSS W3C validator

No errors
![css validator](https://res.cloudinary.com/dguqjbr12/image/upload/v1711379699/catch%20a%20dog%20readme/css_fc1kxa.png)

JavaScript JSHint

No errors only one undefined variable bootstrap - this is a custom bootstrap variable and did not need to be defined inside the script.

- comments.js

![comments js](https://res.cloudinary.com/dguqjbr12/image/upload/v1722970327/catch%20a%20dog%202/js.comments_lr28cs.png)

- reviews.js

![reviews js](https://res.cloudinary.com/dguqjbr12/image/upload/v1722970326/catch%20a%20dog%202/js.reviews_j5jsy7.png)


Python CI Python Linter

- About app

No errors in admin.py, urls.py, models.py, views.py

- My dog project app

No errors in settings.py and urls.py

- Contact app

No errors in forms.py, urls.py, views.py

- Reviews app

No errors in admin.py and views.py.

![errors reviews views.py](https://res.cloudinary.com/dguqjbr12/image/upload/v1711402326/catch%20a%20dog%20readme/python.reviews.views_py_qwpdh8.png)
All clear in views.py

![errors reviews urls.py](https://res.cloudinary.com/dguqjbr12/image/upload/v1711402323/catch%20a%20dog%20readme/python.reviews.urls.py_yfw8xc.png)
Line of code were too long so I moved it to the second line

![errors reviews models.py](https://res.cloudinary.com/dguqjbr12/image/upload/v1711402320/catch%20a%20dog%20readme/python.reviews.models.py_lxle66.png)
Removing trailing whitespaces

![errors reviews forms.py](https://res.cloudinary.com/dguqjbr12/image/upload/v1711402316/catch%20a%20dog%20readme/python.reviews.forms.py_othefr.png)
Missing whitespace around operator

### Lighthouse
I made a Lighthouse while being incognito. Had some issues to achieve high Accessibility and SEO.
- Had to add alt attribute to all images
- Most of my 'a' tags didn't have aria-lebel attribute
- Was missing 'meta' tag with description
- I made my nav-link names bolder to be more visible because of dark background color

1. Desktop

![lighthouse desktop](https://res.cloudinary.com/dguqjbr12/image/upload/v1722972004/catch%20a%20dog%202/desktop.lighthouse_r850st.png)

2. Mobile

![lighthouse mobile](https://res.cloudinary.com/dguqjbr12/image/upload/v1722972329/catch%20a%20dog%202/mobile.lighthouse_ehffeq.png)

### Other browsers
I tested my website on Google Chrome, Microsoft Edge, Mozilla Firefox and Safari. All functionality works.

### Different screen sizes
Thanks to Bootstrap my project is responsive on all device sizes

### Bugs
No bugs

## Technologies Used

### Work Environments and Hosting

- [draw.io](https://app.diagrams.net/) (ERD diagrams)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [Cloudinary](https://cloudinary.com/) (Serving static media files)

### Python Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [pillow](https://pypi.org/project/pillow/) (Python Imaging Library, used for image processing)

### Django Libraries

- [django-allauth](https://docs.allauth.org/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)

### External Libraries and Applications

- [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) (Serving static non-media files)
- [Summernote](https://pypi.org/project/django-summernote/) (WYSIWYG editor)

### Database

- [ElephantSQL](https://www.elephantsql.com/) (PostgreSQL database hosting)

### Frontend and styling

- [Bootstrap](https://getbootstrap.com/)

## Deployment

This project was deployed using [Heroku](https://heroku.com/), [Cloudinary](https://cloudinary.com/), [ElephantSQL](https://www.elephantsql.com/) and [Whitenoise](https://whitenoise.evans.io/en/latest/). Full list of libraries and technologies are listed in the section [Technologies Used](#technologies-used).

#### Installing libraries

Installed libraries :

- **Gunicorn** (server used to run Django on Heroku): pip3 install django gunicorn
- **pyscopg2** (connects to PostgreSQL): pip 3 install dj_database_url pyscopg2
- **Cloudinary** (host static files and images): pip3 install dj3-cloudinary-storage
- **Whitenoise** (prevent issues with Heroku not rendering custom stylesheet): pip3 install whitenoise

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

The database provided by Django can not be accessed by the deployed Heroku app and that's why creating database using ElephantSQl is needed.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle"). Tags are optional.
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create env.py file
- Add import os to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL 
os.environ.setdefault("DATABASE_URL", "copiedURL")
- Below, set **SECRET_KEY** variable os.environ.setdefault('SECRET_KEY', 'yoursecretkey')

#### Update Settings

- Add the following code at the top of settings.py to connect Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead SECRET_KEY = os.environ.get("SECRET_KEY")

- To connect to new database, replace provided **DATABASE** variable with 
    ````
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
    ````
- Save and migrate all changes made

#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")

#### Connect to Cloudinary

- In Cloudinary dashboard, copy **API Environment variables**
- In env.py file, add new variables
````
CLOUDINARY = {
    'cloud_name': os.getenv('cloud_name'),
    'api_key': os.getenv('api_key'),
    'api_secret': os.getenv('api_secret'),
}
````
- Add same 3 variables with values in Heroku config var
- In settings.py, in INSTALLED_APPS list, above django.contrib.staticfiles add cloudinary_storage and below add cloudinary
- To define Cloudinary as static file storage add the following to settings.py
    ````
    CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
}

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

#### Allow Heroku as host

- In settings.py add
    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost', '.herokuapp.com',]
    ````

## Credits
Sources I was using for that project:

1- [Code Institute](https://learn.codeinstitute.net/dashboard) 

2- [W3Schools](https://www.w3schools.com/)

3- [Stackoverflow.com](https://stackoverflow.com/)

4- [Diffchecker](https://www.diffchecker.com/)

5- [JSHint.com](https://jshint.com/) ( Javascript validator)

6- [CI Python Linter](https://pep8ci.herokuapp.com/) ( Python validator)

7- [jigsaw](https://jigsaw.w3.org/css-validator/) (CSS vlidator)

8- [Html validator](https://validator.w3.org/) (HTML validator)

### Content
1. Description for all treatments from About me page comes from:
- [Psielsko](https://psielsko.pl/)
- [Pieski umysl](https://pieski-umysl.pl/)
- [Med store](https://med-store.pl/)
- [Mvet](https://mvet.pl/)
2. The icons comes from [Font Awesome](https://fontawesome.com/)
3. Fonts are taken from [Google Fonts](https://fonts.google.com/)

### Media
1. Bacground image for home page and logo is taken from my sister's [Facebook](https://www.facebook.com/zlappsafizjo)
2. Images you can see on About me page also comes from my sister's [Facebook](https://www.facebook.com/zlappsafizjo)
3. Responsive view for my project I have thanks to [Am I Responsive](https://ui.dev/amiresponsive) page