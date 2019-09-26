# Data Modeling with Postgres

The first Udacity DEND project

We have a Star Scheme that is used for analytical purposes. The central table is the fact table which is **songplays**. The other tables are the dimension tables users, songs, artists, time and al. 

### Songplays
songplays could be viewed as a fact table from a data warehousing perspective. It contains information from the song play perspective i.e. it has the time the song
* **start_time** - time the song started playing
* **user_id** - use who played the song which is also a key to the user dimension table Level - the level of the membership 
* **song_id** - id associated with the song played which also is a key to the song id table 
* **artist_id** - id associated with the artist performing a song also a key to the artist table
* **session_id** - session id associated with a session
* **location** - this is the location where the song was played 
* **user_agent** - information about the software user agent that was used by the artist 


### Users
users in the app. This information provides information about the user dimension. 

* **user_id** - primary key
* **first_name** - users first name
* **last_name** - users last name
* **gender** - gender of the user
* **level** - the current membership level paid or free . This is useful for allowing us to know that user level of the sparkify user.

We could use this to measure adoption rate as well as how long does it take a user to go from free to paid

### Songs
Songs in music database. This is information about the song in the database. Information about the artist associated with the song can be retrieved by joining the artist_id with the artist_id in the artist table. 
 
* **song_id** - primary key
* **title**- Song Title
* **artist_id** - this is the foreign key to the artist table
* **year** - year that tah song was released
* **duration** - duration of the song


### Artists
Artists in music database. This is information about the artist

* **artist_id** - primary key
* **name** - the name of the artist
* **location** - the location of the artist
* **latitude** - the longitude of the artist location
* **longitude** - the latitude of the artists location 

### Time
Timestamps of records in songplays broken down into specific units. This is a very useful table because it will allow us to do analysis by timeframes

* **start_time** - a ts timestamp stored as bigint also a primary key
* **hour** - hour
* **day** - day of month
* **week** - week of calendar year
* **month** - month of year
* **year** - year
* **weekday** - day of teh week



### Growth Analytics:

Since this is a start up growth and retention are important goals for the survival of the business. Below will be lists some important Key Performance Indicators (KPIs) 

When joining the songplay and time tables the important information relating to time can be obtained. 

### Time based KPI’s

**Daily Active Users (DAU)** - This  tells us how many unique visitors during a given day. The user needs to log at least once during a given day to be counted towards DAU

**Weekly Active Users (WAU)** - This  tells us how many unique visitors during a given day. The user needs to log at least once during a given day to be counted towards DAU

**Monthly Active Users (MAU)** - We will define a month here as 28 days because there are an equal number of weekdays in 28. 

This  tells us how many unique visitors during a given Month. The user needs to log at least once during a given 28 day period  to be counted towards MAU

**Churn Rate** - This is the  percentage of customers that we lose relative to our entire user base for a given period

We could do churn for total number of users across the platform 
We could do churn segmented by Paid users so we measure how many people did not use the subscription 

 



**First addition I would make to the table**

Song Play Duration -  if this measure was added to the songplays table we would be able to aggregate the by user to compute the average time spent on the platform. We could also produce the following metrics: 
* Average Daily Time Spent
* Average Weekly Time Spent
* Average Monthly Time Spent 

We can measure if these are improving over time which will provide with a KPI for measuring engagement with the platform.

Business Intelligence that can of value to data savvy music industry insiders. 

We could joining the songplays 
 
