## break down of steps for this assignment.

1. run pipenv install django in the terminal.
*set up virtual environ
*django-debug-toolbar_look up how to set it up
*django-extentions//shell_plus
*django-registration-redux

## Postgres and Heroku



## Registration and Login
    * install registration-redux

### Users should be able to create new habits and track those habits with trackers,
>what methods do you know that can accomplish this in django?

#### Each habit should have a name and a target or goal.
>What is this "target"? Each habit should have a daily number of some action you want to do.
1. How can I accomplish this? URLS, Views,Templates??


##### A user can only have **one record per day per habit** the constraints option at this address (https://docs.djangoproject.com/en/4.0/ref/models/constraints/) with `UniqueConstraint` to make the habit records unique by user, habit, and day.
>will be helpful in order to accomplish this.