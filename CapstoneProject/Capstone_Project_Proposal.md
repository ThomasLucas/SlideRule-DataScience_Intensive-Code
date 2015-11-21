
# Capstone Project Proposal #

*Data Science Intensive - Thomas Lucas*


----------

## **Identify the trends and characteristics of popular songs over the years** ##

### **Summary** ###

The objective of this project is to try to identify if there are some patterns and common characteristics among the most popular songs of all time. In other words, I want to try to find if there is a “magic recipe” to create a song and have it on top of the charts. If there is no global trend over the years, it will be interesting to look at the data on a smaller time scale to try to identify some potential copycats. For example, if a song reaches the top of the charts and presents some new characteristics by comparison with what has been done in the past, it could be interesting to see if in the same year other songs will used the same “model”.


----------


### **Part A** - Looking for the data, getting and cleaning it ###

- Get the data from the Million Songs Dataset (for testing I will only use the subset of 10k songs)
- Play around with the files which are in HDF5 format with Python to see how they can be used
- Have a look at other music websites to see how I can have access to the data:
	- [http://www.billboard.com/](http://www.billboard.com/) for the rankings over the years
	- [http://webscope.sandbox.yahoo.com/](http://webscope.sandbox.yahoo.com/) for the user ratings
	- [https://www.musixmatch.com/](https://www.musixmatch.com/) for the lyrics of the songs
	- [http://secondhandsongs.com/](http://secondhandsongs.com/) to identify original songs and second hand songs


### **Part B** - Analyzing the data ###

**Looking for patterns between songs over time** - *Clustering*

- Pick up the first 100 songs from the charts / rankings for each decade between 1960 and 2010 (included), if available
- Look at the similarities / differences between these clusters (criterias of similarities have to be defined)
- The first idea is to analyze if inside a decade the successful songs are similar to each others 
- Then I will be interesting to compare the songs over decades to see if we can create new clusters of similar songs. This could help to identify if there are some cycles in music, or if it is more a succession of new trends
- Try to create visualizations to understand the results better



### **Part C** - Going further ###

**Analyzing the lyrics of the songs over time** - *Text Analysis and Sentiment Analysis*

- Using the different clusters identified in the previous part, it will be interesting to have access to the lyrics of the songs and perform a sentiment analysis on them to try to find the mood of the songs and then see if the songs are still similar
- Refine the clusters
- It could give us an idea of what themes or mood was popular in each decade and see if this is a constant over the time
- Try to create visualizations to understand the results better


### **Additional Inputs** - If time permits... ###

- Try to predict the year of a song using the previously identified criterias
- Cross-check the results of the previous parts with the data from the second hand songs website
- Find advanced correlation between the mood of the song and the events that have happened in the decade / year (could be studied in part C)
- Music tagging
- Increase the number of songs
- ...

----------

### **Deliverables** ###

The project will involve some Python code. I don't know yet if everything will be included in an iPython notebook or if it will be done in some .py files. It can be probably a mix of both. In addition, some javascript files will be used for visualizing data using d3.js.

The output of this study will be an online article with interactive visualizations. This could also lead to a recommender system for music listening if the search for patterns is successful.

----------

### **Potential Clients** ###

It is probably too ambitious to say that this project is intended for music industry professional who can use this analysis to compose new hits. 
It is more realistic to say that this project will target people with an interest in music (and also people interested in data science). The objective is to highlight some interesting features to be able to enhance the musical experience of the users, and maybe give them some new listening perspectives.


