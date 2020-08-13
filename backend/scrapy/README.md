
# Scraping.py


**Table of Contents**

[TOCM]

[TOC]


## What we do?
We are getting the information from several news sites to feed our web app

## Why we do what we do?
Make life easier for people


## General scraper structure　

```python

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
```
### Scraping page with XPATH

```python
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
```
### Returning information

```python
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
```
## Specific functions

### Universal
Problems to get the images sometimes so we added a cicle while to change the loadin gif from universal for better one in case than the image was no loaded
	
```python
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
```
### NY Times
Problems to get the completed link for the images due to them use a shorter version than autocomplete url's
	
```python
            temp_news.append(parsed.xpath(XPATH_LINK_TO_ARTICLE))
            page = 'https://www.nytimes.com'
            j = 0
            while j <=6:
                temp_news[1][j] = page + temp_news[1][j]
                j = j + 1
```
### BBC
Problems to get the completed link for the article due to them use a shorter version than autocomplete url's
	
```python
 temp_news.append(parsed.xpath(XPATH_LINK_TO_ARTICLE))
            page = 'https://www.bbc.com'
            j = 0
            while j <=6:
                temp_news[1][j] = page + temp_news[1][j]
                j = j + 1
                
            temp_news.append(parsed.xpath(XPATH_SUMMARY))
```
                
### FlowChart

```flow
st=>start: Activate function
op=>operation: Scraping content
cond=>condition: Successful Yes or No?
e=>end: Return information

st->op->cond
cond(yes)->e
cond(no)->op
```

### End
