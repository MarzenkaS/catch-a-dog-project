# Catch a Dog - Advanced Zoophysiotherapy & Fitness

My inspiration for creating this Django project was my sister's profession. She is a physiotherapist for dogs and cats. I wanted to create a website where pet owners can find the information they need to know about therapy she is providing. Another important thing is the ability to read other people's opinions and comments, as well as add your own after logging in.

![responsive mockup](https://res.cloudinary.com/dguqjbr12/image/upload/v1711357050/catch%20a%20dog%20readme/responsive_uzx4fe.png)

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

![nav.loggedout](https://res.cloudinary.com/dguqjbr12/image/upload/v1711361030/catch%20a%20dog%20readme/nav.loggedout_pag7xo.png)
![nav.loggedin](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359029/catch%20a%20dog%20readme/nav.loggedin_xfjkvp.png)
![burger.menu](https://res.cloudinary.com/dguqjbr12/image/upload/v1711361536/catch%20a%20dog%20readme/burger.menu_qyoqcz.png)
![burger.menu1](https://res.cloudinary.com/dguqjbr12/image/upload/v1711361528/catch%20a%20dog%20readme/burger.menu1_mfkpvw.png)

Register
- Allows user to create an account
- Username, password and password confirmation are required, email (optional)

![Sign up](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359035/catch%20a%20dog%20readme/register_pllhtg.png)

Login
- For registered already user
- Username and password required
- Contains "Remember me" option
- After signed in, user see confirmation
- When username or password are incorrect, user will be informed

![Sign in](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359047/catch%20a%20dog%20readme/signin_ctyrmv.png)
![sign in as](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359041/catch%20a%20dog%20readme/signedin_u14mpd.png)
![wrong details](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359053/catch%20a%20dog%20readme/wrong.password_vhmtwq.png)

Logout
- After user clicks on logout link in nav bar, will see confirm form
- Then user will be redirected to home page with confirmation message about being signed out

![sign out](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359009/catch%20a%20dog%20readme/confirm.signout_yliews.png)
![sign out confirmation](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359044/catch%20a%20dog%20readme/signedout_i3m1tv.png)

Add new review
- An authenticated user from nav bar can navigate to add review page
- Afte adding review and clicking Submit button will see confirmation
- User can delete or edit and update own review
- Confirmation message about delete and update will be shown to a user

![add review](https://res.cloudinary.com/dguqjbr12/image/upload/v1711366236/catch%20a%20dog%20readme/add.review1_fjpcno.png)
![review submitted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711373137/catch%20a%20dog%20readme/review.submitted_ijewzh.png)
![delete review](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359018/catch%20a%20dog%20readme/delete.review_edtjxs.png)
![review deleted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711373125/catch%20a%20dog%20readme/review.deleted_qgjp8n.png)
![edit review]()
![review updated]()

Home page
- Includes welcome paragraph with instruction and short introduction to website
- Below each user can see reviews in order from the newest
- Paginated list of reviews

![home](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359026/catch%20a%20dog%20readme/home.page_yio1q7.png)

Review detail
- User even not registered can open single review on separate page to see it in detail
- Each page displays review with author, date and time of updatig and number of comments
- User also can see all attached to review comments and by who and when were written

![review detail](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359038/catch%20a%20dog%20readme/review.detail_djdjwo.png)
![review with comments](https://res.cloudinary.com/dguqjbr12/image/upload/v1711374325/catch%20a%20dog%20readme/review.with.comments_smlkqe.png)

Comments
- Only authenticated user can add comment
- Comment has to be approved by admin
- User can delete or edit and update own comment
- Confirmation message about delete and update will be shown to a user

![comments form](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359058/catch%20a%20dog%20readme/comments_zcxgei.png)
![comment submitted](https://res.cloudinary.com/dguqjbr12/image/upload/v1711375601/catch%20a%20dog%20readme/comment.submitted_dsgafe.png)
![edit comment](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359021/catch%20a%20dog%20readme/edit.comment_zzcyk7.png)
![comment updated](https://res.cloudinary.com/dguqjbr12/image/upload/v1711375606/catch%20a%20dog%20readme/comment.updated_vmobot.png)
![delete comment](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359015/catch%20a%20dog%20readme/delete.comment_czxtuy.png)
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

![about](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359056/catch%20a%20dog%20readme/about_xglzux.png)
![contact](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359012/catch%20a%20dog%20readme/contact_ainpbz.png)
![gallery](https://res.cloudinary.com/dguqjbr12/image/upload/v1711359063/catch%20a%20dog%20readme/gallery_pr7kww.png)

### Future Features

## Database Design
### Database Model

The database model diagram was designed using [draw.io](https://app.diagrams.net/) 

![ERD](https://res.cloudinary.com/dguqjbr12/image/upload/v1711357059/catch%20a%20dog%20readme/ERD_hc8bp8.png)

### Custom Model

To build my models, I followed the walkthrough project created by the Code Institute and adapted for my project's requirements.
I added required Custom Model not covered in the walkthrough - Reviews Model so each authenticated user can add own review.

### CRUD
The CRUD principle I did for my original Reviews Model and Comment Model

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
### Lighthouse
1. Desktop
2. Mobile
### Other browsers
### Different screen sizes
### Bugs

## Technologies Used

## Deployment

## Credits
### Content
### Media