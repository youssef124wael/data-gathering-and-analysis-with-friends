import pandas as pd
from gathering_from_coursera import GC
from gathering_from_coursera import GCL


links = []
for i in range(83):
    links.append(f"https://www.coursera.org/courses?page={str(i + 1)}&sortBy=BEST_MATCH")
gathering_courses = GC()
gathering_links_bot = GCL()

df = {'title': [], 'rating': [], 'level of course': [],'modules_number': []}
page = 1
for link in links:
    page_courses = gathering_links_bot.gathering(link)
    course_data = gathering_courses.gather(page_courses)
    df['title'].extend(course_data['title'])
    df['rating'].extend(course_data['rating'])
    df['level of course'].extend(course_data['level of course'])
    df['modules_number'].extend(course_data['modules_number'])
    print(f'page {str(page)} got extracted from')
    page += 1

df = pd.DataFrame(df)
df.to_csv('courses_edited.csv')
