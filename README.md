# surfs_up

## About this project
Oahu weather data was queried to provide insight for investors of a surf and ice cream shop business on whether it would be sustainable year-round. 

## Resources
### Data sources
* hawaii.sqlite

### Software
* Jupyter Notebook 6.3.0
* SQLalchemy 1.4.7
* Visual Studio Code 1.62.3

## Results
### Highlights
* On average, June (average temperature: 74°F) is slightly warmer than December (average temperature: 71°F).
* Extreme temperatures (min, max) for June and December appear to follow the trend of averages, slightly warmer in June than December. 
<picture>
* June has more temperature data points than December (1700 points vs. 1517 points, respectively).

## Summary
In summary, temperature data for 2 months of the year do not lend enough information for action. If the point of the analysis is to assess sustainability of the business around the year, the analysis should consider metrics important to surfers and tourists who would be the primary target audiences for this business. To supplement this, I would perform the following additional queries:
* Retrieve important surf metrics such as surf height, tide height, wind speed and direction, swell locations
* Retrieve metrics non-surf tourists would consider such as UV index, humidity, 
* Perform analyses on all months instead of just two months to provide more accurate yearly trends.
