import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news}')
res2 = requests.get('https://news.ycombinator.com/news?p=2')


# print(res,res.text)
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

# selective picking: select() use css selector
# print(soup.select('.storylink')[0])
links = soup.select('.storylink')
links2 = soup2.select('.storylink')

# votes = soup.select('.score')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

first_2pages_links = links + links2
first_2pages_subtexts = subtext + subtext2

# print(votes[0])
# print(links[0].getText())
# print(links[0].get('href',None))

# typical pattern to sort a dictionary, using a lambda  
def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key= lambda k: k['votes'],reverse=True)

def create_custom_hn(links,subtext):
    hn = []
    for index,item in enumerate(links):
        # why we use enumerate?
        # links[index] = item, but to retrieve subtext (that is not being enumerate) we need to use enumerate
        title = links[index].getText()
        href = links[index].get('href',None)
        vote = subtext[index].select('.score')
        # now this is going to run if the vote list exist
        if len(vote):
            points = int(vote[0].getText().replace(' points','')) # get rid of the point text and just keep the 'int' for the next check
            # print(points)
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points}) 
    # return hn
    return sort_stories_by_votes(hn)

# pprint.pprint(create_custom_hn(links,subtext))
pprint.pprint(create_custom_hn(first_2pages_links,first_2pages_subtexts))
