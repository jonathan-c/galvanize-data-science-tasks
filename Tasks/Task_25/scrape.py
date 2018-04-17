import requests
import bs4

def scraper(url, results=None):
	if not results:
		results = []

	page = requests.get(url)
	soup = bs4.BeautifulSoup(page.text, "html.parser")
	elements = soup.select('p b.big')

	for element in elements:
		try:
			movie = element.text
			results.append(movie)
		except IndexError:
			return 'No matching element found.'

	link = soup.select('a.next')

	try:
		href = link[0].get('href')
		scraper(href, results)
	except IndexError:
		return 'No matching element found'
	
	return results


rankings = scraper('https://www.pastemagazine.com/articles/2017/12/the-50-best-movies-of-2017.html')
print(rankings)