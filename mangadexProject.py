
from requests_html import HTML, HTMLSession
import os

session = HTMLSession()

def getManga_Html():
    ''' Get the manga html '''
    mangadex_url = 'https://mangadex.org/title/'
    mangaid = input("Manga Id:  \n")
    url = mangadex_url + mangaid
    url = url.replace(' ', '')
    print(url)
    try:
        mrequests = session.get(url).html
        return mrequests
    except:
        return(print("Wrong Id"))


def find_Chapters():
    ''''
    Get the Chapters of the Manga
    Corregir Solo descarga la primera página del los capitulos
    Para mangas muy largos
    '''
    soup = getManga_Html()
    chaptersList = []
    for chapter in soup.find('a[href^="/chapter"]'):
        subchapter = str(chapter.attrs['href'])
        if subchapter.endswith('comments'):
            pass
        else:
            chaptersList.append('https://mangadex.org' + subchapter)
    chaptersList.reverse()
    return chaptersList

def chapterHtml(chapter_url):
    '''Get Chapter Soup
        RENDER NOT WORKING
    '''
    try:
        r =session.get(chapter_url).html
        r.render()
        print(r)
        return r
    except:
        print("Couldnt print r")
        return None
def compare_url(chapter_url):
    ''' (str) -> bool
    Compares if the current url is equal to the given url to check if
    the chapter is still the same or if it changed automatically
    changes the chapter automatically
    '''
    currentUrl = ''
    soup = chapterHtml(chapter_url)

    urls = soup.find('head meta')
    for url in urls:
        try:
            if url.attrs['property'] == 'og:url':
                currentUrl = url.attrs['content']
        except:
            pass
    if chapter_url.startswith(currentUrl):
        print("Both Urls are the same")
        return True
    else:
        chapter_url = currentUrl
        return False
    # try:
    #     url = soup.head.find('meta',{'property': 'og:url'})['content']
    #     return url
    # except:
    #     print("Probably the last chapter")
    #     return None

def get_image(chapter_soup):
    soup = chapter_soup.find('img[srs^="https://s2.mangadex.org/data"]')
    print(soup)

  '''
  Not Working
  '''
    # for first_div in  chapter_soup.find_all('img'):
    #     print(first_div.prettify())





#     first_div = chapter_soup.find('div',
#                 class_='reader-main col row no-gutters flex-column flex-nowrap noselect')
#     second_div = first_div.find('div',
#     class_='reader-images col-auto row no-gutters flex-nowrap m-auto text-center cursor-pointer directional')
#     print(second_div.prettify())
#
#
#
#
# def getTotalPages(chapter_url):
#      #Get the number of pages in a Chapter to create the
#     #appropiate number of Urls
#
#     chapter_soup = chapterSoup(chapter_url)
#     fDiv = chapter_soup.find('div', {'data-manga-id' : "46010"})
#     #sDiv = fDiv.find('div',
#     #          class_='col text-center reader-controls-page-text cursor-pointer')
#     print(fDiv.prettify())
#
#     #return number_Pages
#


r = find_Chapters()
new = compare_url(r[0])
print(r[0])

msoup = chapterHtml(new)
get_image(msoup)
#print("r is " + str(r))


'''
Encontrar forma de hacer que beutifulsoup saque todas las imagines que no fueron
cargadas al no cargase Javascript

Activar html requests
Ver como funcionan las branches
'''
