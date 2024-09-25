**Job Application Email Sender**
=====================================

**1. What is this application for?**
------------------------------------

This application allows you to send automatic emails using Gmail's SMTP service to companies for job applications. The application uses Python to connect and send emails to companies using your CV and a list of known companies in Denmark.

**2. What you need**
--------------------

* Python installed
* bulkemail - project
* A "Gmail" account with 2-factor authentication enabled and app password
* CV.pdf
* Application.pdf
* companylist.xlsx

Note: You can download the companylist.xlsx from [Lærepladsen](https://www.laerepladsen.dk/) for the education you need.

**3. Setting up Gmail - and app passwords**
--------------------------------------------

You already have a Gmail account. The next step is to enable 2-factor authentication in Gmail.

### 3.1 Enabling 2-factor authentication

```bash
Settings -> Security -> 2-Step Verification
```

Enter your phone number and enter the one-time password to enable 2-factor authentication. Refresh the page.

### 3.2 Creating an "App password" for SMTP

```bash
Settings
```

In the search bar on the top of the page, type:
```bash
app passwords
```

Click on app password and create an application. Copy the app password and save it. You need it later.

**4. Installing requirements**
-----------------------------

Before starting the application, you need to install the libraries used for this project. This is done by installing the dependencies in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**5. Editing file**
-------------------

The `config.ini` is the file where you type in program-specific information in order for the application to function properly. The `config.ini` looks like this:

```ini
[variables]

# Husk der skal ikke være specielle tegn eller danske bogstaver i path til filerne.
# Ellers virker programmet ikke

# example: C:\Users\martin\Desktop\bulkemail\jobvirksomheder.xlsx
excelpath =

# example: ["C:\Users\martin\Desktop\CV.pdf", "C:\Users\martin\Desktop\Application.pdf"]
filer =

# excluded emails that you dont want to send emails to
#example: ["timem@gmail.com", "company5@gmail.com"]
excludedemails =

# Start from a specific email in the list
#example: company5@gmail.com
Startfromemail =

#Your name
#example: Martin
navn =

#Your gmail address
#example: myemail@gmail.com
email =

#Your gmail appassword that you have generated
# fjgk jdkf dkdl fkfj
password =
```

Follow the instructions in the `config.ini` to fill all the variables with the data it needs.

**6. Running the application**
-----------------------------

The `main.py` file is the main entry file for the application. Just run the app `main.py` using Python, and the application will send automatic emails to companies.

**Logs**
--------

The application will print all the emails it has sent to like this:

```bash
Email sent to: mail@planbornefonden.dk
Email sent to: jbj@consult.dk
Email sent to: info@tt.dk
Email sent to: dk@titancontainer.com
```