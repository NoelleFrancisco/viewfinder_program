import random
import pandas as pd
from art import logo

# Load the CSV file into a DataFrame
movies_df = pd.read_csv('movie_list.csv')

# Load ASCII logo of the program
print(logo)


def create_list_of_recommendations():
    # Get user's preference for type of medium (movie or TV show) to watch
    is_tv_series = prompt_input("Would you prefer to watch TV Series? (Yes/No): ", ["YES", "NO"],
                                "Please enter Yes or No")

    # Get user's preferred main genre for preferred medium
    print("\nNext let's find out what main genre you're interested in. "
          "The genre options are: Action, Adventure, Comedy, Drama, Romance, Science Fiction")
    valid_genres = ["ACTION", "ADVENTURE", "COMEDY", "DRAMA", "ROMANCE", "SCIENCE FICTION"]
    main_genre = prompt_input("What main genre would you prefer? ", valid_genres,
                              "Please enter a valid genre.")

    # Get preferred runtime length
    print("\nGreat! Do you want to watch something short, medium or long? "
          "Something short is less than 1.5 hours. Medium is 1.5 to less than 2.75 hours. "
          "Long is more than 2.75 hours.")
    valid_runtime_options = ["SHORT", "MEDIUM", "LONG"]
    runtime_option = prompt_input("What runtime length would you prefer? ", valid_runtime_options,
                                  "Please enter Short, Medium or Long.")

    # Get user's preferred language for preferred medium
    language = prompt_input("\nWould you prefer something in a foreign language? (Yes/No) ",
                            ["YES", "NO"], "Please enter Yes or No")

    # Filter the dataframe based on user's response to the questions provided above
    filtered_movies_df = movies_df[
        (movies_df['Is TV Series'].str.capitalize() == is_tv_series) &
        (movies_df['Genres'].str.contains(main_genre)) &
        (movies_df['Duration Type'].str.contains(runtime_option)) &
        (movies_df['Foreign Language'].str.contains(language))
        ]

    # Takes filtered movies dataframe and creates a list containing the titles
    list_of_movies = filtered_movies_df['Title'].to_list()
    return list_of_movies


def prompt_input(question, options, error_message):
    # Prompts a question to the user. If response does not match options, will loop question to user until it matches
    while True:
        response = input(question)
        if response.upper() in options:
            return response
        else:
            print(error_message)


# Function to prompt user and begin process to find a recommendation
def recommend_movie_or_tv():
    print("Hello! Let me help you find something to watch. I will ask you a series of questions to find what"
          "would be a good fit for what you're in the mood for.")

    while True:
        recommendations = create_list_of_recommendations()

        # Reviews list in recommendations variable. If list contains items, will identify a recommendation.
        # If list does not contain elements, will re-run create_list_of_recommendations function.
        if recommendations:

            # Uses random function to determine a random index to pick a recommendation
            picker = random.randint(0, len(recommendations)-1)
            recommended_movie_or_show = recommendations[picker]
            print(f"\nBased on what you're looking for, we recommend watching: {recommended_movie_or_show}.")

            # If the list of recommendations includes more than one item, will pop the index containing original
            # recommendation and run another random function to determine a second recommendation
            if len(recommendations) > 1:
                recommendations.pop(picker)
                alt_picker = random.randint(0, len(recommendations)-1)
                alt_recommended_movie_or_show = recommendations[alt_picker]
                print(f"If you're not feeling {recommended_movie_or_show}, another option we recommend"
                      f" is: {alt_recommended_movie_or_show}.")
                print("\nThanks for using The Viewfinder! Have fun watching!")
            break
        else:
            print("Sorry, we weren't able to find anything based on your criteria. Let's try again.")


# Run the recommendation function
recommend_movie_or_tv()
