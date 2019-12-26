# bantaipublic


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

<!-- ABOUT THE PROJECT -->
## About The Project

A simple friend suggestion api built in django.

DB: PostgreSQL
Framework: Django
Libraries used: faker, rest_framework

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/your_username_/Project-Name.git
```
2. Setup PostgreSQL
- Django supports PostgreSQL 9.0 and higher.
- In case you do not have Postgres on your system already, I would recommend you downloading and installing it from the package app on their site.
3. Install psycopg2
```sh
pip install psycopg2
python -c "import psycopg2"
```
4. Install Django
```sh
pip install Django
```
5. Run migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
6. Start the Server
```sh
python manage.py runserver
```

### Usage

1. User list
```
GET /api/users HTTP/1.1
Host: localhost:8000
Content-Type: application/json
```
```JSON
{
    "count": 200,
    "next": "http://localhost:8000/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1511,
            "user_id": "b44d363fd13d",
            "username": "aolsen",
            "dob": "1978-05-23",
            "name": "Jordan Rivers",
            "gender": "M",
            "location": "Bradshawfurt",
            "pic_url": "https://mcintosh.com/"
        },
        {
            "id": 1509,
            "user_id": "5e96fff684b3",
            "username": "stephaniemoore",
            "dob": "2016-03-06",
            "name": "John Evans",
            "gender": "M",
            "location": "Lake Emmamouth",
            "pic_url": "https://griffin.biz/"
        },
        ..
      ]
}
```

2. Friendship list
```
GET /api/friendships HTTP/1.1
Host: localhost:8000
Content-Type: application/json
```
```JSON
{
    "count": 1047,
    "next": "http://localhost:8000/api/friendships/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1285,
            "profile_1": 1169,
            "profile_2": 1458,
            "created_at": "2019-12-26T14:15:07.822202Z"
        },
        {
            "id": 1286,
            "profile_1": 1290,
            "profile_2": 1246,
            "created_at": "2019-12-26T14:15:07.863245Z"
        },
    ..
  ]
}
```

3. Friendlist for a particular user.
```
GET /api/user/5e96fff684b3/friendlist HTTP/1.1
Host: localhost:8000
Cache-Control: no-cache
```
```JSON
```

4. Friend Suggestions for a particular user.
```
GET /api/user/5e96fff684b3/suggestions HTTP/1.1
Host: localhost:8000
Cache-Control: no-cache
```
```JSON
```

### Tests
Run the following in the root directory to run testcases.
```sh
python manage.py test
```
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
