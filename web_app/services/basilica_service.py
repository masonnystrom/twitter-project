
import basilica
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)

if __name__ == "__main__":

    print("---------")
    tweet_text = "I love #Blockchain"
    tweet_embedding = connection.embed_sentence(tweet_text, model="twitter")