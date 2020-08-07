import requests
import lxml.html as html



def get_universal():
    XPATH_TITLE = '//h2[@class="ce6-Tipo1_Titulo"]/a/text()'
    XPATH_LINK_TO_ARTICLE = '//h2[@class="ce6-Tipo1_Titulo"]/a/@href'
    XPATH_SUMMARY = '//p[@class="ce6-Tipo1_Nota"]/text()'
    XPATH_LINK_IMAGE = '//img[@class="ce6-Tipo1_Imagen"]/@src'
    try:
        url_search = 'https://www.eluniversal.com.mx/' 
        response = requests.get(url_search)
        if response.status_code == 200:
            temp_news = []
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            temp_news.append(parsed.xpath(XPATH_TITLE))
            temp_news.append(parsed.xpath(XPATH_LINK_TO_ARTICLE))
            temp_news.append(parsed.xpath(XPATH_SUMMARY))
            temp_news.append(parsed.xpath(XPATH_LINK_IMAGE))
            news =({
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                }
                )
            i = 0
            while i <= 4:
                news[i]['title'] = temp_news[0][i]
                news[i]['link_article'] = temp_news[1][i]
                news[i]['summary'] = temp_news[2][i]
                if temp_news[3][i] == 'https://www.eluniversal.com.mx/sites/all/modules/lazyloader/image_placeholder.gif':
                    news[i]['link_image'] = 'https://acegif.com/wp-content/uploads/loading-46.gif'
                else:
                    news[i]['link_image'] = temp_news[3][i]
                
                i = i + 1

            return news
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print('Upps! We have a problem, try again',ve)

def get_bbc():
    XPATH_TITLE = '//h3[@class="lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"]/a/span/text()'
    XPATH_LINK_TO_ARTICLE = '//h3[@class="lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"]/a/@href'
    XPATH_SUMMARY = '//p[@class="lx-stream-related-story--summary qa-story-summary"]/text()'
    XPATH_LINK_IMAGE = '//img[@class="qa-srcset-image lx-stream-related-story--index-image qa-story-image"]/@src'
    try:
        url_search = 'https://www.bbc.com/mundo/topics/c2lej05epw5t' 
        response = requests.get(url_search)
        if response.status_code == 200:
            temp_news = []
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            temp_news.append(parsed.xpath(XPATH_TITLE))
            temp_news.append(parsed.xpath(XPATH_LINK_TO_ARTICLE))
            page = 'https://www.bbc.com'
            j = 0
            while j <=6:
                temp_news[1][j] = page + temp_news[1][j]
                j = j + 1
                
            temp_news.append(parsed.xpath(XPATH_SUMMARY))
            temp_news.append(parsed.xpath(XPATH_LINK_IMAGE))
            news =({
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                }
                )
            i = 0
            while i <= 4:
                news[i]['title'] = temp_news[0][i]
                news[i]['link_article'] = temp_news[1][i]
                news[i]['summary'] = temp_news[2][i]
                news[i]['link_image'] = temp_news[3][i]
                i = i + 1

            return news
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print('Upps! We have a problem, try again',ve)



def get_new_york():
    XPATH_TITLE = '//h2[@class="css-pdtj06 e1xfvim30"]/text()'
    XPATH_LINK_TO_ARTICLE = '//div[@class="css-1l4spti"]/a/@href'
    XPATH_SUMMARY = '//p[@class="css-1echdzn e1xfvim31"]/text()'
    XPATH_LINK_IMAGE = '//img[@class="css-11cwn6f"]/@src'
    try:
        url_search = 'https://www.nytimes.com/es/' 
        response = requests.get(url_search)
        if response.status_code == 200:
            temp_news = []
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            temp_news.append(parsed.xpath(XPATH_TITLE))
            temp_news.append(parsed.xpath(XPATH_LINK_TO_ARTICLE))
            page = 'https://www.nytimes.com'
            j = 0
            while j <=6:
                temp_news[1][j] = page + temp_news[1][j]
                j = j + 1
                
            temp_news.append(parsed.xpath(XPATH_SUMMARY))
            temp_news.append(parsed.xpath(XPATH_LINK_IMAGE))
            news =({
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                },
                {
                'title': 'none',
                'link_article': 'none',
                'summary': 'none', 
                'link_image': 'none'
                }
                )
            i = 0
            while i <= 4:
                news[i]['title'] = temp_news[0][i]
                news[i]['link_article'] = temp_news[1][i]
                news[i]['summary'] = temp_news[2][i]
                news[i]['link_image'] = temp_news[3][i]
                
                i = i + 1

            return news
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print('Upps! We have a problem, try again',ve)



def run():
    print(get_new_york())
    print('----------------------------------------------------------------------------------------')
    print(get_bbc())
    print('----------------------------------------------------------------------------------------')
    print(get_universal())



if __name__ == '__main__':
    run()