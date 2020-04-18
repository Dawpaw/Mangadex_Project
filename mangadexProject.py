from bs4 import BeautifulSoup as bs
import requests
import os

def getManga_Soup():
    ''' Get the manga html '''
    mangadex_url = 'https://mangadex.org/title/'
    mangaid = input("Manga Id:  \n")
    url = mangadex_url + mangaid
    url = url.replace(' ', '')
    print(url)
    try:
        mrequests = requests.get(url).text
        manga_soup = bs(mrequests, 'lxml')
        #print(manga_soup.prettify())
        return manga_soup
    except:
        return(print("Wrong Id"))


def find_Chapters():
    ''''
    Get the Chapters of the Manga
    Corregir Solo descarga la primera página del los capitulos
    Para mangas muy largos
    '''
    soup = getManga_Soup()
    chaptersList = []
    for chapter in soup.find_all('div', class_='row no-gutters'):
        subchapters = chapter.find('div',
        class_='chapter-row d-flex row no-gutters p-2 align-items-center border-bottom odd-row')
        try:
            sub_Subchapters = subchapters.find('div',
            class_='col col-lg-5 row no-gutters align-items-center flex-nowrap text-truncate pr-1 order-lg-2')
            chap_link = sub_Subchapters.find('a',href = True)
            if chap_link.has_attr('href'):
                chap_Newlink = "https://mangadex.org/" + chap_link['href']
                print(chap_Newlink)
                chaptersList.append(chap_Newlink)
            print("\n---------------------------------------------------\n")
        except:
            pass
    chaptersList.reverse()
    return chaptersList

def chapterSoup(chapter_url):
    '''Get Chapter Soup'''
    try:
        reqNumber = requests.get(chapter_url).text
        return bs(reqNumber, 'lxml')
    except:
        return None
def compare_url(chapter_url):
    '''
    Compares if the current url is equal to the given url to check if
    the chapter is still the same or if it changed automatically
    changes the chapter automatically
    '''

    soup = chapterSoup(chapter_url)
    try:
        url = soup.head.find('meta',{'property': 'og:url'})['content']
        return url
    except:
        print("Probably the last chapter")
        return None

def get_image(chapter_soup):
    for first_div in  chapter_soup.find_all('img'):
        print(first_div.prettify())
    '''first_div = chapter_soup.find('div',
                class_='reader-main col row no-gutters flex-column flex-nowrap noselect')
    second_div = first_div.find('div',
    class_='reader-images col-auto row no-gutters flex-nowrap m-auto text-center cursor-pointer directional')
    print(second_div.prettify())


'''

'''def getTotalPages(chapter_url):
     #Get the number of pages in a Chapter to create the
    #appropiate number of Urls

    chapter_soup = chapterSoup(chapter_url)
    fDiv = chapter_soup.find('div', {'data-manga-id' : "46010"})
    #sDiv = fDiv.find('div',
    #          class_='col text-center reader-controls-page-text cursor-pointer')
    print(fDiv.prettify())

    #return number_Pages

'''


r = find_Chapters()
new = compare_url(r[0])
new = new + "/1"
msoup = chapterSoup(new)
get_image(msoup)
#print("r is " + str(r))


'''
Encontrar forma de hacer que beutifulsoup saque todas las imagines que no fueron
cargadas al no cargase Javascript

Activar html requests
'''
