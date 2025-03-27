# this file is for gathering from coursera only as other files for other websites will be added

# importing libraries
from bs4 import BeautifulSoup as bs
import requests as r
import numpy as np

# a class for gathering from each course page on coursera (needs edits i made some mistakes in the completion_time_tag variable)
# gathering coursera
class GC:
    def gather(self,links):
        coursera_courses_data = {'title': [], 'rating': [], 'level of course': [],'modules_number': []}
        headers = {"User-Agent": "Mozilla/5.0"}
        for url in links:
            
            response = r.get(url,headers=headers)

            if response.status_code == 200:
                soup = bs(response.text, 'html.parser')

                title_tag = soup.find(class_="cds-119 cds-Typography-base css-1xy8ceb cds-121")
                title = title_tag.text if title_tag else "Title Not Found"

                rating_tag = soup.find(class_='cds-119 cds-Typography-base css-h1jogs cds-121')
                rating = rating_tag.text if rating_tag else "Rating Not Found"

                level = soup.select('.css-86zyin .css-fk6qfz')[1].text # the correct one

                modules_number_tag = soup.find(class_='cds-119 cds-113 cds-115 css-17cxvu3 cds-142')            # adding the class
                modules_number = modules_number_tag.text if modules_number_tag else "Number of Modules not found"

                coursera_courses_data['title'].append(title)
                coursera_courses_data['rating'].append(rating)
                coursera_courses_data['level of course'].append(level)
                coursera_courses_data['modules_number'].append(modules_number)
                print(f"Successful: {title}")
            else:
                print(f"Failed to load page: {url}")

        return coursera_courses_data


# this class is for gathering the links of the courses then putting it with the coursera.org link so the link work for soup to work
# (i don't think any edits here is possible if you noticed anything change it in a branch)
# gathering coursera links
class GCL:
    def gathering(self, link):
        links = []
        response = r.get(link)
        if response.status_code == 200:
            soup = bs(response.text, 'html.parser')
            link = soup.select('.cds-ProductCard-content a')
            for url in link:
                links.append('https://www.coursera.org' + url.attrs['href'])
        return links
