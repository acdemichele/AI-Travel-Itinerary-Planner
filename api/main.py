from fastapi import FastAPI
from travel.travelAssistant import travel_itinerary

app = FastAPI()

@app.get("/get_itinerary")

def travel_itinerary(interests: str, city: str, country: str, budget: str):
      output = travel_itinerary(interests, city, country, budget)
      return {"itinerary": output}  

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    