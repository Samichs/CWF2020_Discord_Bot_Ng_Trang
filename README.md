# CWF2020_Discord_Bot_Ng_Trang

Kyle's submission for Code with Friends Fall 2020!

This is my first personal coding project that I've ever done, a Discord bot! 

The purpose of this bot is to create polls within a text channel that members can vote on using reactions. Currently this bot is able to create polls with a maximum of 9 options, using the basic 1 through 9 emojis as reactions. I hope to utilize a server's specific emojis as reactions some time down the line. This bot is also able to keep track of the current running poll and recall it in a new message. It is not very refined and there's lots of room for improvement in terms of efficient functionality, but I'm happy with what this bot can do given the limited time spent on the project.

Something I'd like to do for this project in the future is create a directory hierarchy that is similar to what you would see in production-level codebases. You can see the outlines for some areas like test and source directories, but they are not extensively used currently. Of course, this would also mean populating those directories such as writing unit tests for my Discord bot. In terms of functionalities, I plan on adding random features that utilize different parts of Discord that I haven't seen before (not sure what these are at the moment but I'm exploring). Some fun commands for RNG applciations such as flipping a coin or rolling dice are on my list as well since my friends and I often use these random techniques to make decisions for us. 

All of my other projects have either been for school or work, so it was refreshing to work on something that was purely for my own interests. It was a lot of fun working on something that I would actually be using too, and could see tangible results for very easily. I did not join a check-in group for this event, so as expected of myself I had a bit of trouble in terms of accountability. Even then, I'm quite content with the fact that I was able to get something up and running at all! This project really helped me realize how simple it is to create your own software projects. There are a ton of resources online either through Stack Overflow, Youtube -- well literally all of Google -- and you can find an answer for practically any question you have. Parts of this project, such as command parsing in a message, could have been quite tedious if coded manually (like they would teach you in school for the sake of concepts) but utilizing existing libraries, Discord.py in my case, made seemingly complex functionalities turn into basic function calls. This really helped in my mental block of thinking I would have to manage every part of the project on my own.

Special thanks to Mayuko, Scott, and the rest of the CWF2020 team for putting on such an amazing event. I am very thankful to be a part of such a wonderful community!

Files:
src/first_bot.py - This is the first bot I made to test out the Discord.py library
src/bot_class.py - This is the "final" bot I've iterated over, I've created my own class to keep track of the poll and other data that is not normally saved