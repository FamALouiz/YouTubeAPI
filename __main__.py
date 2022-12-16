from API_scrapping import requests_thumbnails, errorMessage, get_thumbnail_Id

# Thumbnails 
thumbnail_urls = []

# Youtuber usernames we wanna use
youtuber_usernames = ["PewDiePie",
"MrBeast6000", 
"KSIOlajideBT",
"TheDiamondMinecart",
"CaptainSparklez",
"Smosh"
]

def addThumbnails(response):

    # Adds thumbnails of the given response to the list
    for item in response["items"]:
        if int(item["snippet"]["publishedAt"][:4]) <= 2019: # Change date to whatever we want
            return False 
        current_url = item["snippet"]["thumbnails"]["high"]["url"]  # Change quality here 
        thumbnail_urls.append(current_url)

def main():
    
    for name in youtuber_usernames:

        uploads_id = get_thumbnail_Id(name)

        # Requesting all urls per youtuber
        response, nextPageToken = requests_thumbnails(name, None, uploads_id)

        # Checking if response raises an error
        if response == 1 or 2: errorMessage(response)

        # Adding the given thumbnails 
        addThumbnails(response)

        # Checking if there is a next page
        if not nextPageToken:
            print(thumbnail_urls)
        else:  

            # Looping till we reach stop date
            while True:
                if nextPageToken == None: 
                    break
                response, nextPageToken = requests_thumbnails(name, nextPageToken, uploads_id)
                stop = addThumbnails(response)
                print(name, nextPageToken, stop)
                if stop == False: 
                    print("Stopped")
                    break
            
    # Printing results
    print(f"The number of thumbnails: {len(thumbnail_urls)}\n"
    f"The number of youtubers: {len(youtuber_usernames)}\n"
    f"The average number of thumbails per youtuber: {len(thumbnail_urls)/len(youtuber_usernames)}")

    print("Writing text.....")

    # Writing the results
    f = open("links.txt", "w")
    for item in thumbnail_urls: 
        f.write(f"Link: {item}\n")
    f.write(f"The number of thumbnails: {len(thumbnail_urls)}\n"
    f"The number of youtubers: {len(youtuber_usernames)}\n"
    f"The average number of thumbails per youtuber: {len(thumbnail_urls)/len(youtuber_usernames)}")     


if __name__ == "__main__": 
    main() 