from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")



def travel_itinerary(interests: str, city: str, country: str, budget: str):

    '''
    INPUTS:
    interests: A str interest or hobby (eg. eating at restaurants, hiking, or sightseeing)
    city: A str city name (eg. Toronto, New York, or Rome)
    country: A str country name where the city is located (eg. Canada, The United States, or Italy)
    budget: a str budget (ex. $50,000) 
    '''

# Define a System prompt which will be the budget template -> PromptTemplate

    system_template = "I am a tour guide local to the city of {city} in the country of {country} that helps people find activites related to {interests} on a budget of {budget}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# Define a Human Prompt -> PromptTemplate

    human_template = "Please provide for me an itinerary"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Compile ChatPromptTemplate by creating a str array

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    
# Insert Variable Values here --> ChatPromptTemplate

    request = chat_prompt.format_prompt(interests = interests, city = city, country = country, budget = budget)


    chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
    
    result = chat.invoke(request)
    
    return result.content    
