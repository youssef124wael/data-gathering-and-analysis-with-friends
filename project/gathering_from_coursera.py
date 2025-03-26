from bs4 import BeautifulSoup
import requests as r

class GatheringCoursera:
    def gathering(self, links):
        coursera_courses_data = {'title': [], 'rating': [], 'completion_time': []}

        for url in links:
            response = r.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                title_tag = soup.find(class_="cds-119 cds-Typography-base css-1xy8ceb cds-121")
                title = title_tag.text if title_tag else "Title Not Found"

                rating_tag = soup.find(class_='cds-119 cds-Typography-base css-h1jogs cds-121')
                rating = rating_tag.text if rating_tag else "Rating Not Found"

                completion_time_tag = soup.find(class_='css-fk6qfz')
                completion_time = completion_time_tag.text if completion_time_tag else "Time Not Found"

                coursera_courses_data['title'].append(title)
                coursera_courses_data['rating'].append(rating)
                coursera_courses_data['completion_time'].append(completion_time)

                print(f"Successful: {title}")
            else:
                print(f"Failed to load page: {url}")

        return coursera_courses_data
    

class GatheringCourseraLinks:
    def gathering(self,link):
        links = []
        response = r.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            link = soup.select('.cds-ProductCard-content a')
            for url in link:
                links.append('coursera.org' + url.attrs['href'])
        return links
