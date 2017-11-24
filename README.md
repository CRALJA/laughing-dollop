# laughing-dollop

A project written in Python to predict the next city Uber should work in. We limited our search initially to the UK and then to cities in England, excluding London, based on the data that we could find. We excluded London because it is not comparable to any other city - by size or population. We felt that the reasons why Uber is so successful in London would not be transferrable to other UK cities. Also, the private hire licenced for Uber was revoked in London as of September 2017. They are currently appealing this decision and so this was another reason why we decided to excluded London from our analysis at this point. 


Research:
Stage 1 was researching different external data sources which could be used to predict the ideal future city for Uber. We focused on a number of different areas.
Public transport: Collecting data on the number of public transport stations for each city.
House prices: Historical data on average house prices in cities Uber already occupies, aiming to specifically focus in on the 12 months before and after Uber started in each city. 
Employment data:  Number of people self-employed and unemployed in each city. Uber operates by using drivers who are self-employed so we specifically focused on this category. 
Population data: City level population data.
Taxi data: Considering the number of taxis and private hire vehicles in each city.
Crime data: Theft from a person, vehicle crime, violence and sexual offences, and bicycle theft data were collected for each city. 
Deprivation data: Average deprivation for each city, calculated by grouping LSOA codes. The deprivation data is from a source collected between 2011 and 2013. 
Uber data: Demographics of Uber users, broken down by age, gender, and income. Also collected the date that Uber launched in each city.
Uber operates through a mobile device.  Based on this we decided to research mobile phone coverage for the UK, with the aim of breaking this down to a city level. This was only available as an infographic rather than a dataset and so hindered our ability to incorporate it. If this became available, it would be something we could explore further. 



Staging the data:
MongoDB: Employment, house prices, population and taxi data were loaded into a Mongo database. Each data set had its own collection
SQL: The data sets for deprivation and public transport were loaded in to SQL as they were easier to manipulate and analyse rather than using Mongo. 



Analysis: 
Public transport: Less public transport links may indicate that the city would benefit for an additional taxi service such as Uber. The data collected would give a good indicator of whether Uber would make a positive impact on the city and therefore whether it would be a good prediction for the next best city. 
House prices: The analysis specifically focused on this data in the 12 months before and after Uber started in each city. Viewing the change in prices may indicate the impact that Uber has on the economy of a city. We compared this to the 
Employment data: Employment and unemployment data were researched because they give a good indication of the demographic of people in each city (is this why we did it???). Comparing employment data (all 3 types) from Uber cities with non-Uber cities can identify similarities in the levels of cities that Uber is already successfully running in. 
Population data: Looking at the population for cities with Uber and comparing these population levels to those cities without Uber. From this, we can suggest cities with similar population levels as a prediction for Uber’s next city. 
Taxi data: Considering the number of taxis in each city before and after Uber launched. Looking at the ‘before Uber levels’ may indicate that the next city for Uber to launch in should be one with similar number of taxis. 
Crime data: We considered whether crime levels in 4 types of crime (theft from a person, vehicle crime, violence and sexual offences, and bicycle theft) changed in the 12 months before and after Uber launched in the city. This would give a good indication of whether Uber had a positive impact on reducing crime levels and would be beneficial to a new city. 
Deprivation data: This is used to suggest possible Uber cities based on their similar deprivation levels when compared to cities that do have Uber. 
Uber data: Demographic of Uber users and the date that Uber launched in each city. Uber user demographic show that 40% of users (in the USA) are aged 24-30. Determining the proportion of these people in each city would identify the cities which are the best for Uber to join next. 
