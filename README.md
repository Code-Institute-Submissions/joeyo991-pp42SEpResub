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
- As a frequent visitor, I want to be abale to view the comments on mine and other users' posts.

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

