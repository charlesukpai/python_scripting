#Writing a webcrawler that would crawl websites and extract links from the webpage
#Started by defining a function that is called as the crawler goes through the page to return urls
s = '''
page content
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries,
but also the leap <a href="https://www.facebook.com"</a> into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets
containing Lorem Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum
'''
def get_next_url(s):
    #the variable start_link locates the start of the a tag for the link:
    start_link = s.find('<a href=')
    #the variable start_quote locates the first quotation mark around the url
    #But will start looking after the location of start_link
    start_quote = s.find('"', start_link)
    #end_quote locates the final quotation marks and end of the url
    #start_quote + 1 means it starts looking after the position of the first one
    end_quote = s.find('"', start_quote + 1)
    #the url is then located and extracted
    url = s[start_quote + 1:end_quote]
    #returning the location of end_quote ensures we start looking for the next
    #url without repeating the one we already ound
    return url

print get_next_url(s)
