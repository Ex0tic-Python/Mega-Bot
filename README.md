# Mega-Bot
Mega-Bot is a multipurpose bot that has tons of random utilities for no real reason other than me feeling like implementing them. For example, it has access to:

* Old School RuneScape data (GE Tracking, Wiki Data, Player Data, etc.)
* Genshin Impact Data (Wiki Data and User Data)
* Spotify data
* GitHub data
* Wakatime data
* Image Utilities
* Audio Utilities
* Fun Commands (Games and more)
* And more

I will add stuff as I go just because I feel like it. This is a rather ambitious project because of the size of it but it's rather simple as a lot of it is just requests and whatnot.

## For developers
Wondering how it works? I'll note some major points here for other developers wanting to program something similar of their own.  

### NOTE
This bot is currently not made with tons of servers in mind or for handling many users. Because I don't plan to make this bot public, it's made with little optimization or accommodations for big data sets, such as using SQLite as opposed to something like PostgreSQL or using an inefficient way of caching user-deleted messages and whatnot. If I did make this for more servers, I would find better ways to store data and optimize it by using async and whatnot and also use PostgreSQL but for now at least, I'll just use simple code for it.

### OldSchool RuneScape Commands
The OldSchool RuneScape commands work by using a bare-bones (It works and has some useful functions but it's not very optimized, doesn't use async, etc. just basic requests overall) custom wrapper I built after the only wrapper I found for OSRS was no longer maintained and had no documentation. I don't know how to make it a pip library as of yet so I made it a library in my way. Feel free to find the repo for it [here](https://github.com/Ex0tic-Python/OSRS-Wrapper) or at https://github.com/Ex0tic-Python/OSRS-Wrapper

### Genshin Impact Commands
To Finish
