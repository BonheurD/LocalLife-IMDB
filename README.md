# LocalLife IMDB Task

During the given hour, I primarily searched for an appropriate dataset and structured the process for data formatting and performing sentiment analysis.

I did not manage to find a complete dataset. I found useful information on [IMDB's non-commercial datasets](https://developer.imdb.com/non-commercial-datasets/), which contain most information about IMDB items but not reviews. Another dataset I found contained reviews but did not specify which movies the reviews belonged to. If I had more time available, I would have looked for a way to extract reviews from IMDB or find a new and improved dataset.

I downloaded the datasets and stored them in a directory called `raw_data/`, as can be seen in the code. However, I was not able to upload those files.

I divided the code into three parts, but I only had time to implement the first two. However, since I do not have a dataset for the reviews nor an API key for OpenAI, none of the code compiles.

1. **format_data.py**: This will format the data, merging columns for movie IDs, movie titles, and reviews. Below is an example of how it would look if there existed a file consisting of the columns `tconst` and `reviews`. If another dataset solution is found, this would need to be altered.
2. **sentiment_analysis.py**: This will perform sentiment analysis for each review, creating a new file with the sentiment analysis added. The new file will have the following format: `movie_id | movie_title | review | sentiment`.
3. **(Unimplemented)**: This part will allow the user to request the reviews of a movie. My initial idea is to use the OpenAI API to determine the movie in question and then perform a search (most likely binary + linear) in the listed movies based on the movie title. Finally, the desired reviews will be returned.

If I had more time, I would look for a better dataset or implement one myself. Additionally, I would implement step 3 to return reviews based on user requests.
