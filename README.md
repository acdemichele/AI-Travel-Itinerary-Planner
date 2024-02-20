# AI-Travel-Itinerary-Planner

AI assistant for travel itineraries leveraging the OpenAI API via LangChain

This project provides a RESTful API for generating travel itineraries based on user preferences using the OpenAI language model. It utilizes FastAPI for creating the web API and integrates with the langchain_openai library for interacting with OpenAI's GPT-3.5 model.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/travel-itinerary-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd travel-itinerary-api
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:

   ```python
   OPENAI_API_KEY=your-openai-api-key
   ```

## How to Run

1. Once the installation is complete and you have set up your environment variables, you can start the FastAPI application by running the following command:

   ```bash
   uvicorn api.main:app --reload
   ```

2. The API will start running locally at `http://127.0.0.1:8000`. You can access the Swagger documentation and test the endpoints by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Usage

To generate a travel itinerary, send a GET request to the `/get_itinerary/` endpoint with the following query parameters:

- `interests`: A string representing the user's interests or hobbies.
- `city`: A string representing the name of the city.
- `country`: A string representing the name of the country.
- `budget`: A string representing the budget for the trip.

Example:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get_itinerary/?interests=Exploring%20Museums&city=Paris&country=France&budget=%241000' \
  -H 'accept: application/json'
```
