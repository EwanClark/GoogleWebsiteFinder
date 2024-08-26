from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.getenv("API_KEY")
print("GOOGLE SEARCH KEYWORDS")
print()

def again():
    while True:
        print()
        print("Again? (y/n)")
        again = input()
        if again.lower() == "y":
            main()
            break
        elif again.lower() == "n":
            exit()
        else:
            print("Invalid input. Please enter \"y\" or \"n\"")
def main():
    print()
    # What they want to see:
    def what_data_to_see():
        while True:
            while True:
                print()
                print("Do you want to see the site title? (y/n): ")
                global seesitetitle
                seesitetitle = input()
                if seesitetitle.lower() == "y":
                    seesitetitle = True
                    break                
                if seesitetitle.lower() == "n":
                    seesitetitle = False
                    break
                else:
                    print("Invalid input. Please enter \"y\" or \"n\"")
            while True:
                print()
                print("Do you want to see the site link? (y/n): ")
                global seesitelink
                seesitelink = input()
                if seesitelink.lower() == "y":
                    seesitelink = True
                    break                
                if seesitelink.lower() == "n":
                    seesitelink = False
                    break
                else:
                    print("Invalid input. Please enter \"y\" or \"n\"")           
            while True:
                print()
                print("Do you want to see the site description? (y/n): ")
                global seesitedescription
                seesitedescription = input()
                if seesitedescription.lower() == "y":
                    seesitedescription = True
                    break                
                if seesitedescription.lower() == "n":
                    seesitedescription = False
                    break
                else:
                    print("Invalid input. Please enter \"y\" or \"n\"")           
            while True:
                print()
                print("Do you want to see the website name? (y/n): ")
                global seesitescource
                seesitescource = input()
                if seesitescource.lower() == "y":
                    seesitescource = True
                    break                
                if seesitescource.lower() == "n":
                    seesitescource = False
                    break
                else:
                    print("Invalid input. Please enter \"y\" or \"n\"")
            if seesitetitle == False and seesitelink == False and seesitedescription == False and seesitescource == False:
                print()
                print("Please accept at least one peace of data.")
                print()
            else:
                break
    what_data_to_see()
    print()
    # get the keywords        
    first_keyword = input("Enter the first keyword (required): ")
    second_keyword = input("Enter the second keyword (press enter to skip): ")
    thrid_keyword = input("Enter the third keyword (press enter to skip): ")
    print()
    print("Loading results...")
    print()

    params = {
        "engine": "google",
        "q": f"{first_keyword} {second_keyword} {thrid_keyword}",
        "api_key": apikey
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    results = results["organic_results"]
    for site in results:
        sitenumber = site["position"]
        sitetitle = site["title"]
        sitelink = site["link"]
        sitedescription = site["snippet"]
        sitescource = site["source"]
        #show results:
        print(f"Site {sitenumber}:")
        if seesitetitle == True:
            print(f"Title: {sitetitle}")
        if seesitelink == True:
            print(f"Link: {sitelink}")
        if seesitedescription == True:
            print(f"Description: {sitedescription}")
        if seesitescource == True:
            print(f"Website name: {sitescource}")
        print()
    again()
main()

def new():
    print("this is a new func")
    print("add functionality to function")
    print("Do more stuff")