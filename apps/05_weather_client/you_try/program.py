import bs4
import collections
import requests

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    print_header()

    zip_code = input('What zip code do you want the weather for (90210)? ')

    html = get_html_from_web(zip_code)

    report = get_weather_from_html(html)

    print('The temp in {} is {}°{} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

    # display the forecast


def print_header():
    print('------------------')
    print('   WEATHER APP')
    print('------------------')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, "lxml")
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
