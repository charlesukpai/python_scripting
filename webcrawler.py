#Writing a webcrawler that would crawl websites and extract links from the webpage
#Started by defining a function that is called as the crawler goes through the page to return urls

url = 'http://xkcd.com/353'

#This method gets the webpage url and parses it so we can crawl
#and extract the urls on it
def get_webpage(url):
    #try block tries the code and if it fails jumps to except block
    try:
        import urllib
        return urllib.urlopen(url).read()
    #exception handler for edge cases and errors
    except:
        return ""

#This method extracts each new url located on the webpage
def get_next_url(webpage):
    #the variable start_link locates the start of the a tag for the link:
    start_link = webpage.find('<a href=')
    #add an if statement to handle for no url found
    if start_link == -1:
        return None, 0
    #the variable start_quote locates the first quotation mark around the url
    #But will start looking after the location of start_link
    start_quote = webpage.find('"', start_link)
    #end_quote locates the final quotation marks and end of the url
    #start_quote + 1 means it starts looking after the position of the first one
    end_quote = webpage.find('"', start_quote + 1)
    #the url is then located and extracted
    url = webpage[start_quote + 1:end_quote]
    #returning the location of end_quote ensures we start looking for the next
    #url without repeating the one we already ound
    return url, end_quote

#This method returns all the urls found on the target webpage
def get_all_urls(webpage):
    while True:
        url, endpos = get_next_url(webpage)
        if url:
            print url
            webpage = webpage[endpos:]
        else:
            break

print get_all_urls(get_page('http://xkcd.com/353'))
