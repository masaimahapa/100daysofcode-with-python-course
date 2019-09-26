import bs4
import requests
import os

os.system('clear')

def pull_site(URL):
    raw_website= requests.get(URL)
    raw_website.raise_for_status()
    return raw_website

def scraper(site):
    
    news_list = []
    dates_list = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_news_list = soup.select('.newsInfo')
    html_dates_list= soup.select('.formatTimeAgo')
    

    for date in html_dates_list:
        dates_list.append(date.getText())

    for new in html_news_list:
        news_list.append(new.getText())



    print('--------------------------------------------------------------')
    everything= list(zip(news_list, dates_list))
    for each in everything:
        print(each[0] + each[1])



def news_scraper(site):
    headlines_list= []
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_headlines= soup.select('.content')

    for headline in html_headlines:
        headlines_list.append(headline.getText())
        
    print('--------------------------------------------------------------')
    for idx, headline in enumerate(headlines_list[:10]):
        print(f'{idx+1}. {headline}')
        print()




def main():
    while True:
        print('--------------------------------------------------------------')
        interest= input('chess (c), SA news (n) or exit (x)?')
        if interest.lower() == 'n':
            URL= 'https://www.iol.co.za/'
            site= pull_site(URL)
            news_scraper(site)

        elif interest.lower() == 'c':
            URL= 'https://chess24.com/en/read/news'
            site= pull_site(URL)
            scraper(site)

        elif interest.lower()=='x':
            break

        else:
            print('command not understood.')
            main()

    

if __name__ == '__main__':
    main()
