# Welcome to the (former) back-end to the health insurance policy holder management system!
While this currently does not do any work for [policy-holders-web](https://github.com/kate-perry/policy-holders-web), this backend was intended to host a local MongoDB instance to store policy holder and insured event information. In this repo, you will find MongoDB setup functionality and views to manipulate data.

# To Run...
1. Ensure MongoDB is installed on your machine.
2. Start a local MongoDB instance by running `python manage.py runserver 8080`
2. Create the DB tables by running `python manage.py migrate`
3. Use Postman to get and create Policy Holders and Insurance Events.
