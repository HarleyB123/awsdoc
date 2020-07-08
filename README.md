# awsdocs

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

<a name="general-info"></a>
## General info
Whenever I find myself struggling in the world of AWS services, I always go to the same [page](https://docs.aws.amazon.com/) and selecting the service in question. Since most of the time, I am either writing terraform or python in the terminal when I need this page, I thought why not create a pip package that will open the docs in my default browser from the command-line. Thus, a simple project called awsdocs was born.


<a name="technologies"></a>
## Technologies
* pypi to bundle the project into a pip package
* Python 3.7
* argparse

<a name="setup"></a>
## Setup

```
pip install awsdocs
```

Then pass through the service you wish to know more about - eg: 

```
awsdocs s3
```

<a name="features"></a>
## Features
* Opens aws documentation in your default browser
* Simple to use

ToDo: 

Since this code works on the URL path of the documentation, the format of the different services is not always intuitive. ```awsdocs ssm``` does not work, but ```awsdocs systems-manager``` does. Of course, I can use the choices option in argparse to make this explicit to the user, but I don't want to have to manually enter all the services. Need to think of an idea to get round that one. 

<a name="status"></a>
## Status
In Progress
