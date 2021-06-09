# The Python web scraper:

## Problem we want to solve: to collect information from hackernews that has at least 100 points, so I am can read the most relevant info on the topic.

In simple term web scraping is the art of automate the process of getting data from a website without using their API.
Why we would do that then?
There's no API, the API is not free, restricted to certain users or the API is not good enough.

Ethically since we are checking the example.com/robots.txt file that check who is the 'User-Agent' and what can scrape 'allow' or 'Disallow'. If nothing is there, it implicitally means that we should be good to go.

### Starting the project

We are using **_Beautiful Soup_** ( from PyPI ),as a Python library to scrape websites and **_requests_** to grab _html_ files.

On Terminal:

```terminal
> pip3 install beautifulsoup4
> pip3 install requests
```

Scrape.py file, importing needed libraries:

```python
import requests
from bs4 import BeautifulSoup
import pprint # a module to have a nice print on the Terminal
```

#### How to get the html content of a page from the website?

We can send a request via the module:

```python
res = request.get('https://news.ycombinator.com/news')
# print(res,res.text) # and we are getting back the response status [200] and the html text;
soup = BeautifulSoup(res.text,'html.parser') # transform the raw html string to usable data, a 'soup' object easy to use
links = soup.select('.storylink')
subtext = soup.select('.subtext')
```

What is Beautfil Soup?

> BS can help us to parse the text via a soup object, but we ned to add one more parameters, specific to get only html and not xml (that bs can parse too)
> BS has methods to get all specific data from the html:
> ex

```python
# find all contest in a list form
print(soup.body.contents)
# find all paragraphs
print(soup.find_all('p'))
# find all title
print(soup.title)
```

Beautiful soup **_selectors_**: select(), use [css selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

<!-- ```python
votes = soup.select('.score')
# want to be more specific? ex.
votes[0].get(id)
links[0].getText() # get the text of the html tag
links[0].get('href',None) # get an attribute specificied as first parameter
``` -->

But instad of grab the votes, we need to grab the **_.subtext_** class to make sure that all link has a subtext:

<!-- ```python
vote = subtext[index].select('.score')
# why we use enumerate?
        # links[index] = item, but to retrieve subtext we need to use enumerate
        title = links[index].getText() # or
        title = item.getText()
``` -->

The rest of the code:

```python
# Helper function; typical pattern to sort a dictionary, using a lambda.
def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key= lambda k: k['votes'],reverse=True)

def create_custom_hn(links,subtext):
    hn = []
    for index,item in enumerate(links):
        # why we use enumerate? we have 2 lists: links and subtext and we enom only on links, so the only way to grab subtext is use enumerate and use the index
        title = links[index].getText() # links[index] = item; since we don't need the index
        href = links[index].get('href',None)
        vote = subtext[index].select('.score')
        # now we need to check if the vote list exist otherwise we can skip the news
        if len(vote):
            points = int(vote[0].getText().replace(' points','')) # get rid of the 'points' text and just keep the 'integer' for the next check
            # print(points)
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points}) # creating the dictionary
    # return hn
    return sort_stories_by_votes(hn) # Helper function to sort

pprint.pprint(create_custom_hn(links,subtext))
```

---

Now that we know how to get specific data, how to display the custom hackernews?

- First I need to index the item that I need so I need to loop over an 'enumerate'
- then I need to create a function that create a Dict out of collected 'title' and 'link'
- A possible ISSUE is story that ha no votes, so to fix error in the loop we need to ascertain first that for every link there's a vote otherwise:

7. now how can improve the appearance in the terminal of the list od news created?
   we can use the library 'pprint'

8. finally we want to order the story based on number of votes
   so let's create a funciton called sort_stories_by_votes and instead of returning the 'hn' we then return:

```python

sort_stories_by_votes(hnlist):
    return sorted(hnlist,key= lambda k: k['<index>'])

# ...
return sort_stories_by_votes(hn)
# this is a common pattern to how to sort dictionaries 'Dict' , using a lambda function where the 2nd parameter is the key we want use to sort

```

## Next step from Library to Scrapy the framework... many more possibilities

And what to do with all this text data?

- save it as csv file, text file etc.

---

Enumerate, lambdas, common pattern

---
