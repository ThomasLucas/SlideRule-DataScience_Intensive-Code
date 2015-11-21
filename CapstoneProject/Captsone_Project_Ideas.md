# Capstone Project Ideas #

*Data Science Intensive Workshop - Thomas Lucas*

----------

### **Flight Delay prediction tool** ###

The aim of the project will be to try to predict if a flight will arrive on time and to try to find patterns in flights which are (often) late.The result should be a web application where a user can easily put his parameters in and have a quick and clear output. Some visualizations will also be produced to illustrate the results.

This project will take in consideration several parameters like:

- the airline
- the duration of the flight
- the starting point airport
- the arrival airport
- the average price of the ticket (to compare low-cost airlines and other airlines)
- the weather (one of the objectives is also to try to classify the delayed flights, it is always more understandable for a passenger to see that his flight has been delayed because of bad weather conditions than because of another obscure reason for example)
- the season
- the rank of the flight in the day (for example for short distance flights, airplanes are often doing the same journey with the return trip several times a day - so if the first flight is late it will probably entail a delay on the following flights)
- ...

This project will use data from flight timetables. I found a dataset for the U.S but I still have to look at the same thing for Europe. I am more interested in doing this for European destinations and airlines as I know better the data and as I have experienced delays several times while travelling with low-cost European airlines.


----------


### **Build the Ultimate Premier League football team** ###

[Example: Building the ultimate NBA team](http://datascopeanalytics.com/blog/building-the-ultimate-nba-team/)

The idea of this project is to try to build the best football team using players of the Barclays Premier League for a given club with its limited budget. This will try to find the best players for each position in the team regarding statistics like goals, assists, pass accuracy, tackles, yellow/red cards,... and also the implication of the player in the team wins and losses. These data will be associated with the salary of the player and also with the price paid by the club to buy him. This should also enable the user to identify underpaid and overpaid players and the players who represent the best value for money.

It could be also interesting to add some features like the bankable aspect of a player (especially for a top player), which could reduce the cost of the player dramatically and very quickly. Thus, it seems to be possible to use a kind of return on investment (ROI) for the players and add this parameter to the study.

The output of this project will also be a web application which will enable a user to pick his team, define his priorities (homogeneous team / superstar and average players / minimize the cost of the team / maximize the ROI / …) and then generate the optimal team. Visualizations can be added to the project to illustrate the study.


----------


### **Identify the trend and characteristics of popular songs over the years** ###

The objective of this project is to try to identify if there are some patterns and common characteristics among the most popular songs of all time. In other words, I want to try to find if there is a “magic recipe” to create a song and have it on top of the charts. If there is no global trend over the years, it will be interesting to look at the data on a smaller time scale to try to identify some potential copycats. For example, if a song reaches the top of the charts and presents some new characteristics by comparison with what has been done in the past, it could be interesting to see if in the same year other songs will used the same “model”.

Using intuition, I can imagine that summer hits will have specific characteristics like a higher “danceability” and probably different rhythm / scales of notes… Therefore I think that it can be interesting to try to classify songs by season as it could explain why sometimes a “random” song becomes very popular. To go further with this, I would to have a look to the longevity of the songs, i.e. how long they can stay on the top of the charts and try to classify them using this longevity. Then, inside those clusters it will be nice to be able to find common patterns and trends between songs.

Following the previous classification, I would be very interested in doing a sentiment analysis on the lyrics of the songs to see if the top songs have more a positive or a negative connotation and also to look at the most frequent words used in those songs. To cross-check what I have written about the summer hits, intuitively I would say that they have probably a positive connotation as this is what people are looking for during summer and holidays. I am not sure that this is the same thing for what can be identify as the greatest hits of all time. This study can also be extended to the different kind of music. 
Depending on the available time and also on the available data, the study can be performed worldwide and / or country by country.

This project will use data from *The Million Song Dataset* and will also use the history of the most popular song rankings. 
The output of this study will probably be an online article with interactive visualizations. This could also lead to a recommender system for music listening if the search for patterns is successful. 
I don’t think that trying to compare songs using frequential analysis could be a realistic goal here, as it is a complex task and as there are lots of other things to do first. But this could be an interesting addition if the rest is done.

