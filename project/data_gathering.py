import pandas as pd
from gathering_from_coursera import GatheringCoursera
from gathering_from_coursera import GatheringCourseraLinks



gathering_links_bot = GatheringCourseraLinks()
output = gathering_links_bot.gathering('https://www.coursera.org/courses')
print(output)
