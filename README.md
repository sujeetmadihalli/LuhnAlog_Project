# Card Validator Django Project

This is a Django web application for validating credit card numbers using the Luhn algorithm.

## Installation

1. Clone the repository to your local machine:
	git clone https://github.com/sujeetmadihalli/LuhnAlog_Project.git

2. Navigate to the project directory:
	cd luhnAlog_project

3. Install dependencies:
	pip install -r requirements.txt


## Usage

1. Start the Django development server:
	python manage.py runserver

2. Access the application in your web browser at `http://127.0.0.1:8000/`.

3. Enter a credit card number in the provided form and click "Validate" to check if it's valid.


## Running with Docker

You can also run the project using Docker with just a few simple commands:

1. Build the Docker image:
docker build -t card_validator_image .

2. Run the Docker container:
docker run -p 8001:8000 card_validator_image

Now, you can access the application in your web browser at `http://127.0.0.1:8001/`.


## Author

Created by Sujeet
