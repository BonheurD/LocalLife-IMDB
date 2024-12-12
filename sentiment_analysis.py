import openai
import pandas as pd
import os

os.makedirs('results', exist_ok=True)

openai.api_key = "api-key"

# Function to perform sentiment analysis
def analyze_sentiment(review_text):
    try:
        # Call ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant performing sentiment analysis on movie reviews. " 
                 "Answer only with a single word, 'positive' if the review is positive, 'negative' if the review is negative, and 'neutral' if the review is neutral or you cannot decied."},
                {"role": "user", "content": f"Analyze the sentiment of this movie review: {review_text}"}
            ],
            temperature=0.5
        )
        # Extract the sentiment from the response
        sentiment = response['choices'][0]['message']['content'].strip()
        return sentiment
    
    except Exception as e:
        print(f"Error processing review: {e}")
        return "Error"

# Load the dataset
def load_reviews(file_path):
    return pd.read_csv(file_path)

# Add sentiment analysis results to the dataset
def perform_sentiment_analysis(input_file, output_file):
    df = load_reviews(input_file)
        
    # Analyze sentiment for each review
    df['sentiment'] = df['review'].apply(analyze_sentiment)
    
    # Save results to a new CSV file
    df.to_csv(output_file, index=False)

# Main
if __name__ == "__main__":
    input_csv = "prepared_data/data.csv"  # Input file with reviews
    output_csv = "results/data.csv"  # Output file with sentiments
    
    try:
        perform_sentiment_analysis(input_csv, output_csv)
    except Exception as e:
        print(f"An error occurred: {e}")
