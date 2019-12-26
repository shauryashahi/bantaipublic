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

1. Friend Suggestions for a particular user
```
GET /api/user/0c9054ed-729a-4acd-a70c-82086089b86d/suggestions HTTP/1.1
Host: localhost:8000
Cache-Control: no-cache
```
```JSON
{
    "count": 50,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4241,
            "user_id": "844a51cc-b32d-4b22-b42c-14b1cbc8a6ce",
            "username": "jenniferlopez9d539231-e67f-4963-914a-0e6ab43244e4",
            "dob": "2015-02-20",
            "name": "Lisa Carroll",
            "gender": "M",
            "location": "Hansenfort",
            "pic_url": "https://www.carlson.net/"
        },
        {
            "id": 4223,
            "user_id": "d2493e8a-1a2d-4c7f-8ed9-fa823b3ca2b3",
            "username": "davistricia0da3cbcf-bf8c-42ad-b90c-349a73f93d65",
            "dob": "2018-10-18",
            "name": "Kathleen Jackson",
            "gender": "M",
            "location": "Karenton",
            "pic_url": "http://www.nolan-ali.com/"
        },
        ..
      ]
}
```

2. Friend list for a particular user.
```
GET /api/user/0c9054ed-729a-4acd-a70c-82086089b86d/friendlist HTTP/1.1
Host: localhost:8000
Cache-Control: no-cache
```
```JSON
{
    "count": 111,
    "next": "http://localhost:8000/api/user/0c9054ed-729a-4acd-a70c-82086089b86d/friendlist?limit=100&offset=100",
    "previous": null,
    "results": [
        {
            "id": 4243,
            "user_id": "da23644b-46e9-4683-8bca-9fea4fc277f5",
            "username": "kevinbishop6c6c560d-810c-44dd-a2a3-40afff0a37ef",
            "dob": "1971-12-03",
            "name": "Jose Flowers",
            "gender": "M",
            "location": "Jenniferfurt",
            "pic_url": "https://bright.org/"
        },
        {
            "id": 4242,
            "user_id": "1487f169-d144-4341-9d44-677464969337",
            "username": "jleeebbae1f0-bd98-4bc0-83d6-17541aea9ac4",
            "dob": "2015-05-11",
            "name": "Jacqueline Reese",
            "gender": "M",
            "location": "Jennyland",
            "pic_url": "http://www.reed-mejia.org/"
        },
        ..
      ]
}
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
