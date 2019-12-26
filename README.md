# bantaipublic

[![CircleCI](https://circleci.com/gh/shauryashahi/bantaipublic.svg?style=svg)](https://circleci.com/gh/shauryashahi/bantaipublic)
[![Contributors](https://img.shields.io/github/contributors/shauryashahi/bantaipublic.svg)](https://GitHub.com/shauryashahi/bantaipublic/graphs/contributors/)
[![Stargazers](https://img.shields.io/github/stars/shauryashahi/bantaipublic.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/shauryashahi/bantaipublic/stargazers/)
[![Issues](https://img.shields.io/github/issues/shauryashahi/bantaipublic.svg)](https://GitHub.com/shauryashahi/bantaipublic/issues/)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Tests](#tests)
* [Roadmap](#roadmap)
* [Contributing](#contributing)

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
2. Start a virtualenv and install requirements
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Setup PostgreSQL
- Django supports PostgreSQL 9.0 and higher.
- In case you do not have Postgres on your system already, I would recommend you downloading and installing it from the package app on their site.
4. Install psycopg2
```sh
pip install psycopg2
python3 -c "import psycopg2"
```
5. Run migrations and seed the database
```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py seed
```
6. Start the Server
```sh
python3 manage.py runserver
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
python3 manage.py test
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/shauryashahi/bantaipublic/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
