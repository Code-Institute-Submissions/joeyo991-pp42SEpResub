# **RightRecovery**

![Responsive](/readme-images/sign-up.png)

## **About**

The live site can be accessed by this [link](https://rightrecovery.herokuapp.com/).

RightRecovery is a social/blog site that allows people in recovery from addiction and mental health problems to post their stories, struggles and successes. The site has the objective of providing an easy to use blog site. The user can create an account, write posts and also receive comments on their posts or give comments to other users' posts.

## **User Experience Design**

### **Strategy**

Developed for the purpose of allowing people struggling with problems to realise they are not alone.

### **Target Audience**

People in recovery from addiction or mental health problems.

#### **First Time Visitor Goals**
- As a first time visitor, I want to easily be able to navigate to the sign up page.
- As a first time visitor, I want to easily be able to create an account.
- As a first time visitor, I want to easily be able to navigate through the site.
- As a first time visitor, I want to be able to understand why this app might appeal to me.

#### **Frequent Visitor Goals**
- As a frequent visitor, I want to be able to log into my account, so that I can have a personal account.
- As a frequent visitor, I want to be able to easily navigate through the app so that I can find the content I am looking for.
- As a frequent visitor, I want to be able to log in and out of my account.
- As a frequent visitor, I want to be able to update my personal data so that I can keep my account up to date.
- As a frequent visitor, I want to be able to update my picture on the app.
- As a frequent visitor, I want to be able to upload a post.
- As a frequent visitor, I want to be able to comment on other users' posts.
- As a frequent visitor, I want to be able to view the comments on mine and other users' posts.

## **Technologies Used**
### **Languages:**
- [Python](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
- [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

### **Frameworks and Libraries:**
- [Django](https://www.djangoproject.com/): python framework used to create all the backend logic of the website.
- [Bootstrap](https://getbootstrap.com/): HTML and CSS templates used throughout the site.

### **Databases**
- [SQLite](https://www.sqlite.org/): was used as a database during the development stage of the website.
- [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

### **Other tools**
- [Git](https://git-scm.com/): the version control system used to manage the code.
- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
- [Psycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
- [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
- [GitHub](https://github.com/): used to host the website's source code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [PEP8](https://pep8.org/): was used to validate Python code for the website.

## **Features**

**Sign Up Page**

The sign up page features a form where the user enters their username, email and confirms a password.

![Sign Up Page](/readme-images/sign-up.png)

**Login Page**

When the user is logged out, the website will display display a login page with a login form, login button and a 'create account' button.

![Login Page](/readme-images/login-page.png)

When the user logs in, they are redirected to the feed page.

**Navbar**

The navbar is located at the top of the screen. When the user is logged out, the navbar contains:
- The name of the site - redirects to the login page.
- A Sign Up button - redirects to the sign up page.
- A Login button - redirects to the login page.

![Navbar signed out](/readme-images/navbar-out.png)

When the user is signed in, the navbar contains:
- A profile button - redirects to the user's profile.
- A Home button - redirects to the feed page.
- A Logout button - redirects to the logged out page.

![Navbar signed in](/readme-images/navbar-in.png)

On  a mobile, the navbar buttons are condensed into a dropdown.

![Navbar mobile](/readme-images/navbar-mobile.png)

**Profile Page**

This page has a container where the user can see their information and their picture. They can also edit this information via modal that is triggered by clicking the edit profile button. The user's profile is only viewable by themself to allow the site to remain anonymous.

![Profile](/readme-images/profile.png)

**Edit Profile Modal**

This modal allows the user to change their username, email address and their profile picture.

![Edit Profile](/readme-images/edit-profile.png)

**The Feed**

This is where all the posts are displayed whenever they are created by a user.

![Feed](/readme-images/feed.png)

**Post Form**

The post form appears to the left of the posts on the feed and allows the user to create a post. The post needs a title and then some content.

![Post Form](/readme-images/post-form.png)

**Posts**

The Posts are viewed by clicking on a post from the feed. This let's the user see the full post, how many comments it has and also leave a comment.

![Post Detial](/readme-images/post-detail.png)

**Comments**

The user can expand the comments and view them by clicking on the blue comments link on the post.

![Comments](/readme-images/comments.png)

**Post Options**

![Post Options](/readme-images/post-options.png)

If the user clicks into one of their own posts, they will see two buttons:
- Edit - Lets them edit their post.
- Delete - Lets them delete their post.

**Edit Post**

Clicking the edit button allows the user to edit the title or the content of their post.

![Edit Post](/readme-images/edit-post.png)

**Delete Post**

Clicking the delete button allows the user to delete their post if they wish to.

![Delete Post](/readme-images/delete-post.png)

**Logged out Page**

When the user clicks the Logout button in the navbar, they are redirected to the logged out page. This page consists of a message letting them know they have been signed out and also provides a button to bring them back to the log in page.

![Logged Out Page](/readme-images/logged-out.png)

## Future Improvements and Features

**Friends Lists**

In the future I think it could be a good idea to create friends lists so that people can interact with people they have met on the site or that they know already. The only problem with this is that as it is a recovery based site, many people may want to remain anonymous.

**Messaging**

In the future I would like to allow users to message eachother rather than just communicationg through comments on a post.

**Password Reset**

In the future I would like to add the option for the user to reset their password for security reasons or if they have forgotten theirs.

**Comment Deletion**

In the future it may be a good idea for users to have the option to delete a comment that someone has left on their post that they don't like or is unhelpful.

## **Design**

The central theme of the site is simplicity of use. It is aimed to guide the user to the best experience.

### **Colour Scheme**

The main color scheme of the application is blue and white due to the trend in modern web design / social media sites.

![Color Scheme](/readme-images/base-colors.png)

### **Typography**

Then main font used in the application is Segoe UI. The image below explains why I used this font.

![Segoe UI Font](/readme-images/Segoe-UI-Font.png)

### **Imagery**

I used the following image as a background for the Login and Sign Up pages as I feel like the colors contrast well with the blue and white and also beacause it is a great visual representation of what recovery can be like with a little help, which I hope this site can be.

![Background Image](/readme-images/rr-img.jpg)

## **Testing**

### **Testing User Stories**

| First Time Visitor Goals | Requirement met |
| ------------------------- | --------------- |
| As a first time visitor, I want to easily be able to navigate to the sign up page. | Yes |
| As a first time visitor, I want to easily be able to create an account. | Yes |
| As a first time visitor, I want to easily be able to navigate through the site. | Yes |
| As a first time visitor, I want to be able to understand why this app might appeal to me. | Yes |

| Frequent Visitor Goals | Requirement met |
| ----------------------- | --------------- |
| As a frequent visitor, I want to be able to log into my account, so that I can have a personal account. | Yes |
| As a frequent visitor, I want to be able to easily navigate through the app so that I can find the content I am looking for. | Yes |
| As a frequent visitor, I want to be able to log in and out of my account. | Yes |
| As a frequent visitor, I want to be able to update my personal data so that I can keep my account up to date. | Yes |
| As a frequent visitor, I want to be able to update my picture on the app. | Yes |
| As a frequent visitor, I want to be able to upload a post. | Yes |
| As a frequent visitor, I want to be able to comment on other users' posts. | Yes |
| As a frequent visitor, I want to be able to view the comments on mine and other users' posts. | Yes |

### **HTML Validation**

- HTML validation was done by using the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.

- All pages on the site returned back the same result:

![HTML Validation Results](/readme-images/html-validation.png)

### **CSS Validation**

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator.

![CSS Validation Results](/readme-images/css-validation.png)

### **Python Validation**

- No errors were found when the code was passed through Valentin Bryukhanov's [online validation tool](http://pep8online.com/). According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code from all the files and pasting it into the validator.

### **blog app**

**admin.py**

![blog admin.py check](/readme-images/blog-admin-check.png)

**forms.py**

![blog forms.py check](/readme-images/blog-forms-check.png)

**models.py**

![blog models.py check](/readme-images/blog-models-check.png)

**urls.py**

![blog urls.py check](/readme-images/blog-urls-check.png)

**views.py**

![blog views.py check](/readme-images/blog-views-check.png)

### **rightrecovery app**

**urls.py**

![rightrecovery urls.py check](/readme-images/rr-urls-check.png)

**settings.py**

settings.py had 5 lines too long that I could not format any shorter. This had no effect on the application.

![rightrecovery settings.py check](/readme-images/rr-settings-check.png)

### **users app**

**admin.py**

![users admin.py check](/readme-images/users-admin-check.png)

**apps.py**

![users apps.py check](/readme-images/users-apps-check.png)

**forms.py**

![users forms.py check](/readme-images/users-forms-check.png)

**models.py**

![users models.py check](/readme-images/users-models-check.png)

**signals.py**

![users signals.py check](/readme-images/users-signals-check.png)

**urls.py**

urls.py had 1 line too long that I could not format any shorter. This had no effect on the application.

![users urls.py check](/readme-images/users-urls-check.png)

**views.py**

![users views.py check](/readme-images/users-views-check.png)

### **Lighthouse Reports**

**Feed**

![Feed Lighthouse Report](/readme-images/feed-lighthouse.png)

**Login Page**

![Login Page Lighthouse Report](/readme-images/login-lighthouse.png)

**Sign Up Page**

![Sign Up Page Lighthouse Report](/readme-images/signup-lighthouse.png)

**Profile Page**

![Profile Page Lighthouse Report](/readme-images/profile-lighthouse.png)

**Post Detail Page**

![Post Detail Page Lighthouse Report](/readme-images/post-lighthouse.png)

### **Compatibility**

Testing was conducted on the following browsers:
- Chrome
- Brave
- Firefox

The site worked and functioned as it should on all of the tested browsers.

### **Responsiveness**

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

![Responsiveness test](/readme-images/responsiveness.png)

The screens shown above (from left to right) are:
- Large laptop 1440 x 900
- iPhone 8/7/6 Plus
- Galaxy S9/S8 Plus
- iPad

## **Bugs**
The only majaor bug I came across was when I was deploying my project to heroku. When DEBUG was set to False, the page was showing up blank with a message that read: BAD REQUEST(400). This was because of a typo I had left in the base.html template when linking my CSS. Removing the / before the file name solved the problem.

![Bad Request bug](/readme-images/bug.png)

Before Fix:

![Bug pre fix](/readme-images/bug-pre-fix.png)

After Fix:

![Bug post fix](/readme-images/bug-post-fix.png)

## **Deployment**

### **Heroku**

The website is hosted on Heroku and can be accessed by visiting this [link](https://rightrecovery.herokuapp.com/).


The process for deploying the website to Heroku is as follows:

1. Create a Heroku account if you don't already have one.

2. Create a new app on Heroku.

    1. Go to the [Heroku dashboard](https://dashboard.heroku.com/apps).
    2. Click on the "New" button.
    3. Click on the "Create new app" button.
    4. Choose a name for your app.
    5. Choose a region.
    6. Click on the "Create app" button.

3. In your app go to the "Resources" tab.

    - Add a Heroku Postgres database.

4. In your app go to the "Settings" tab, press "Reveal Config Vars", and add the following config vars if they are not already set:

    1. ```CLOUDINARY_URL``` = your cloudinary URL
    2. ```DATABASE_URL``` = the url of your heroku postgres database.
    3. ```SECRET_KEY``` = a secret key for your app.
    4. ```PORT``` = 8000
    11. ```DISABLE_COLLECTSTATIC``` = 1 during development. Remove this when deploying to production.

5. In your app go to the "Deploy" tab.

    1. If it's already possible, connect your Heroku account to your GitHub account and then click on the "Deploy" button.
    2. If not, you need to copy the Heroku CLI command to connect your heroku app and your local repository.

        - ```heroku git:remote -a <your-heroku-app-name>```

6. Go to your local repository.

7. Login to your Heroku account in your terminal and connect your local repository to your heroku app.

    1. ```heroku login -i``` - Enter all your Heroku credentials it will ask for.
    2. Paste the command you copied from step 5 into your terminal.

8. Create Procfile.

    For this project I used gunicorn, so in my case I had the following Procfile:
    - ```web: gunicorn rightrecovery.wsgi``` - This runs the app on heroku.

9. Create ```requirements.txt```. This can be done by running the following command:

    - ```pip freeze --local > requirements.txt```

10. Add and commit all changes.

11. Push your changes to Heroku.

    - ```git push heroku master```
    or
    - ```git push heroku main```

12. Check the logs of your app in heroku dashboard and make sure everything is working.

## **Credits**
- [Django](https://www.djangoproject.com/) for the framework.
- [Bootstrap](https://getbootstrap.com/): for the templates.
- [Django-allauth](https://django-allauth.readthedocs.io/) for the authentication library.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [Cloudinary](https://cloudinary.com/): for the free access to the image hosting service.
- [Coolors](https://coolors.co/): for providing a free platform to generate your own palette.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Google Fonts](https://fonts.google.com/): for providing a free platform to use Google Fonts.
- [KenBroTech](https://www.youtube.com/c/KenBroTech): for the django blog app tutorial I watched and based my project on and the python tutorial videos.
