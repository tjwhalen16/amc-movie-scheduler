from lxml import html
import requests
import re
from movie import Movie

# return dictionary [name: list of Movie]
def parseMoviesFromURL(link):
    response = requests.get(link, allow_redirects=False)
    root = html.fromstring(response.content)
    moviesHtml = root.xpath("//div[@class='ShowtimesByTheatre-film']")
    movies = {}
    for movie in moviesHtml:
        # names = movie.xpath(".//a[@class='MovieTitleHeader-title']//h2")
        # for name in names:
        #     print(name.text.strip())
        nameElem = movie.xpath(".//a[@class='MovieTitleHeader-title']//h2")[0]
        name = nameElem.text.strip()

        # runtimes = movie.xpath("(.//div[@class='txt--tiny MovieTitleHeader-list txt--medium txt--gray--light u-uppercase']//span//span)[2]")
        # for runtime in runtimes:
        #     # html looks like: <span data-reactid="821"><!-- react-text: 822 -->1 hr 36 min<!-- /react-text -->
        #     # Can't get at the time the conventional xpath way, use regex
        #     htmlWithTime = html.tostring(runtime).decode("utf-8")
        #     time = re.search('\d hr \d+ min', htmlWithTime).group(0)
        #     print(time)
        runtimeElem = movie.xpath("(.//div[@class='txt--tiny MovieTitleHeader-list txt--medium txt--gray--light u-uppercase']//span//span)[2]")[0]
        # html looks like: <span data-reactid="821"><!-- react-text: 822 -->1 hr 36 min<!-- /react-text -->
        # Can't get at the time the conventional xpath way, use regex
        htmlWithTime = html.tostring(runtimeElem).decode("utf-8")
        runTime = re.search('\d hr \d+ min', htmlWithTime).group(0)

        # showTimes = movie.xpath(".//div[contains(@class, 'Showtimes-Section-Wrapper-First') or contains(@class, 'Showtimes-Section-Wrapper')]")
        # for showTime in showTimes:
        #     #print(html.tostring(showTime))
        #     screenFormats = showTime.xpath(".//div[@class='Showtimes-Section--PremiumFormat-Heading-Title']//h4")
        #     for screenFormat in screenFormats:
        #         print(screenFormat.text.strip())
            
        #     startTimes = showTime.xpath(".//div[@class='Showtime']")
        #     for startTime in startTimes:
        #         #print(html.tostring(startTime))
        #         print(startTime.get('aria-label'))
        screenings = []
        showTimes = movie.xpath(".//div[contains(@class, 'Showtimes-Section-Wrapper-First') or contains(@class, 'Showtimes-Section-Wrapper')]")
        for showTime in showTimes:
            screenFormatElem = showTime.xpath(".//div[@class='Showtimes-Section--PremiumFormat-Heading-Title']//h4")[0]
            screenFormat = screenFormatElem.text.strip()
            startTimesHtml = showTime.xpath(".//div[@class='Showtime']")
            for startTime in startTimesHtml:
                screenings.append(Movie(name, runTime, screenFormat, startTime.get('aria-label')))
        movies[name] = screenings
    return movies
    
