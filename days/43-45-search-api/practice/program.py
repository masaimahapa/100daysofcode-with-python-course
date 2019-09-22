import api
import webbrowser

def main():

    search= input('Enter a search term:')
    results= api.find_movie_by_title(search)

    print(f"There are {len(results)} results found.")
    for r in results:
        print(f"  Found in Category : {r.category} has and id of {r.id}. Its url is {r.url}")

    view_id= int(input('would you like to view any of them? Enter id: '))
    website= 'talkpython.fm'
    for r in results:
        if r.id == view_id:
            item_url= website+r.url

    webbrowser.open(item_url, new=2)

if __name__ == '__main__':
    main()

