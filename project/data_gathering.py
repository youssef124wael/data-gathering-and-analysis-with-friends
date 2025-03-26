import pandas as pd
from gathering_from_coursera import GC
from gathering_from_coursera import GCL


links = []
for i in range(83):
    links.append(f"https://www.coursera.org/courses?page={str(i + 1)}&sortBy=BEST_MATCH")
gathering_courses = GC()
gathering_links_bot = GCL()

df = {'title': [], 'rating': [], 'completion_time': [],'modules_number': []}
for link in links:
    page_courses = gathering_links_bot.gathering(link)
    course_data = gathering_courses.gather(page_courses)
    df['title'].extend(course_data['title'])
    df['rating'].extend(course_data['rating'])
    df['completion_time'].extend(course_data['completion_time'])
    df['modules_number'].extend(course_data['modules_number'])

df = pd.DataFrame(df)
df.to_csv('courses.csv')
