# Recommended Places API

The Recommended Places API provides recommendations for places to visit based on user input. It utilizes a dataset of places and employs cosine similarity to generate personalized recommendations.

## Getting Started

To use the Recommended Places API, follow the steps below.

### Prerequisites

- Python 3.x
- Flask
- Pandas
- scikit-learn

### Installation

1. Clone the repository:
git clone [repository URL]

2. Install the required dependencies:
pip install -r requirements.txt


### Usage

1. Run the API:
python recommended_places_API.py


2. The API will be accessible at http://localhost:5000.

### API Endpoints

#### POST /recommend

This endpoint accepts a JSON payload containing user input and returns a JSON response with recommended places to visit.

Example Request:

POST /recommend
Content-Type: application/json

{
"AGE": 25,
"Interest": "Historical Sites, Delicious Food",
"Companions": "Family",
"Visiting Time": "2 days 1 night",
"Sex": "Male",
"Budget": "From 1 to 3 million"
}


Example Response:

HTTP/1.1 200 OK
Content-Type: application/json

{
"top_recommended_places": [
"Hue Imperial City",
"Vong Canh Hill",
"Thien Mu Pagoda",
"Bach Van Flower Garden",
"Dong Ba Market"
]
}


#### GET /recommend

This endpoint provides a welcome message to verify that the API is running.

Example Request:

GET /recommend


Example Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
"message": "Welcome to the Recommended Places API"
}


## Dataset

The dataset used for recommendations is sourced from [link](https://raw.githubusercontent.com/1337Rinz/DATA_for_machine_learning/main/dataHUE.csv).

## Notes

- The API utilizes cosine similarity to calculate recommendations based on user input.
- Feel free to customize the API endpoints, response messages, and dataset as per your requirements.

