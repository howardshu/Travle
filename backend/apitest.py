import requests

API_BASE_URL = "http://127.0.0.1:8000"


def send_guess_to_api(song_title):
    """
    Send the guess information to the REST API.
    """
    guess = {"songTitle": song_title}

    try:
        response = requests.post(f"{API_BASE_URL}/make_guess", json=guess)
        response.raise_for_status()
        print("Guess sent to the server")
        print(response.json())
        return response.json().get("correct")
    except requests.exceptions.RequestException as e:
        print("Failed to send guess to the server: ", e)
    return False


# posting to the API analogous to inputting song guess, the API then returns the results of the guess
if __name__ == '__main__':
    input("Press enter to begin: ")
    response = requests.post(f"{API_BASE_URL}/start_game")
    response.raise_for_status()
    print(response.json())

    while True:
        choice = input("1 for search, 2 for guess: ")
        if choice == "1":
            title = input("Search: ")
            response = requests.post(f"{API_BASE_URL}/search", json={"title": title})
            print(response.json())
        elif choice == "2":
            song_guess = input("Enter a song title: ")
            if send_guess_to_api(song_guess):
                break

    print("You did it!")
    # response = requests.post(f"{API_BASE_URL}/end_game")
    # response.raise_for_status()
    # print(response.json())