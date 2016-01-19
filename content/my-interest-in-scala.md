Title: My Interest in Scala
Author: Sheldon Kreger
Category: Programming
Tags: Programming, Career
Date: 2014-11-29 14:00

As you may know, despite a breif academic background in high performance computing, I have spent the last few years working almost exclusively with the content management system Drupal, building and maintaing websites for both small nonprofits and large corporations. Most of my work has been in managing application configuration through user interfaces, or building custom functionality with PHP (I have also worked with front end languages like CSS and SCSS).

Today, Drupal is hotter than ever, with a bright future in Drupal 8.

So, why am I so fascinated by Scala, when it has no immediate applications to my day job? There are two overarching reasons, practical and intellectual.

From a practical perspective, I see too many shortcomings with the current system I work with to be comfortable continuing to invest much time into it.

Working at Intel, on an enterprise sized application, my perspective has grown tremendously. Scalability has become a tremendous problem for our team. And, our team is not just developers - we serve a much larger group of people who add content to site (web ops), collect data on site usage (business intelligence), and leaders for ongoing and new projects (management, marketing). Each of these teams has unique needs, and a monolithic PHP application is, frankly, serving them poorly -
despite the best efforts of our team.

While it may be possible to use PHP in a more robust architecture (a topic for anoother day), it still does not resolve my intellectual desires. In fact, there is a good chance my team will do just this - which is totally OK!

Frankly, I do not want to be limitted to one single knowledge base, one conceptual framewoork, one programming langauge. I want to know more about different software systems, how they are implemented, and why. I do not want to be known as just a PHP developer - I want to be a web engineer with extensive PHP experience, plus XYZ. The best developers I have met can coompare and contrast many frameworks and their practicality for a given application. I want to be able to do that.

Although I have no desire to return to college (yet another topic for another day), I do haave a desire to learn and expand my skills. The best way to do that is to step outside my comfort zone and take on something new and exciting.

Enter Scala. It is pretty much the opposite of PHP - functional, compiled, and practical for things outside web. It is not easy to just pick up and run with - the syntax is unfamiliar, and pretty much illegile unless the programmer has an underlying conceptual understanding of functional programming. And, I have yet to see a single line of asynchronous PHP code (although I have heard it exists at Facebook as HipHop).

I figured Scala was a big jump - but not too big. Since I am familiar with parallel processing, understanding futures, promises, streams, actors, and mapping has been relatively easy. But, they were all terms I had never heard before studying functional programming and reactive programming on Coursera.

Scala is used in a variety of applications. Web applications in Scala use an MVC framework called Play. And, while I had never heard of play, I knew about MVC frameworks, and the basic architecture of web applications. So, learning about Play has served as a good bridge for learning Scala.

Outside web, my primary interest is data science, specifically  predictive analytics. My most exciting programming  project to date is a content recommendation engine we built with Python, Neo4j, and Cypher. Again . . . not Scala. But, learning about functional programming through Scala has opened up a whole new world of possibilities in content recommendation. For example, I had never thought of my Cypher queries as operations on an immutibble graph . . . but they are. Exectuing queries
in parallel was difficult to conceptualize in the larger picture of an application written in Python. Without futures, streams, and observables, there is not any good way to perform calculations and also handle incoming data. We simply updated the data daily, from a single source. Now, I now how to write an application which coould handle data from multiple sources, being updated in short intervals (or even real time), and write them to handle failure, perform calculations in parallel, and
share data to multiple applications simultaneously.

I always compare programming to mathematics. Whether you know it or not, you are surrounded by problems which can only be solved with specific tools. But, you cannot see the problems at all, until you have been taught how to solve them. By making a big jump to a functional language geared toward high performance, threaded, and service-oriented applications, I have started to see my programming problems in a new and exciting way. Scala is awesome.
