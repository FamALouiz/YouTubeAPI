import googleapiclient.discovery as g
import sys 
from key import secret_key

yk = secret_key

# Setting up the youtube requester 
youtube = g.build("youtube", "v3", developerKey= yk)

def requests_thumbnails(username, pageToken, uploads_id):

    # Third request for the videos
    request3 = youtube.playlistItems().list(
        part = "Snippet",
        playlistId = uploads_id,
        pageToken= pageToken
    )
    response3 = request3.execute()

    # Checking if there is a nextPageToken
    try:
        nextPageToken = response3["nextPageToken"]
    except: 
        nextPageToken = None

    return response3, nextPageToken

def errorMessage(error): 
    # Inspects error 
    if error == 1: 
        print("There are no account with that username or videos uploaded to this username. Please try another username")
        sys.exit()


def get_thumbnail_Id(username):
    # First request to grab id
    try:
        request1 = youtube.channels().list(
            part= "statistics",
            forUsername= username,
        )

        response1 = request1.execute()
        youtuber_id = response1["items"][0]["id"]
    except: 
        return 1

    # Second request to grab uploads
    request2 = youtube.channels().list(
        part= "contentDetails",
        id = youtuber_id
    )
    response2 = request2.execute()
    uploads_id = response2["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    return uploads_id