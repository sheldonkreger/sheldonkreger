Title: Drupal for Prototyping
Author: Sheldon Kreger
Category: Programming
Tags: Programming, Drupal
Date: 2014-12-19 12:00

I have spent the last few years working almost exclusively with Drupal 7. My current project has revealed many of the problems Drupal has with scalability in many regards, and as a result, I have set a lot of time aside to explore new frameworks as our team prepares to rebuild the site.

While this post is not about the shortcomings of Drupal, I do want to mention that I no longer plan to make many more websites in Drupal 7. That brings me to the real topic at hand: Drupal 7 is still a great choice for rapid prototyping.

Once a site builder masters the basics of Drupal - getting the LAMP stack up, building content types, and building views - then it is very easy to put together the basic outline of a website very quickly. I can launch a D7 development site using Vagrant in a matter of minutes. I can build out content types and create lists of content in a few short hours. At this point, it does not even require any deep thinking on my part. I have done it enough times that it happens naturally.

Such a prototype will have many shortcomings. It will not do exactly what you and your client want it to do. It will be unthemed. It will be ugly. But, if your site is relatively simple, it will display the basic functionality with very little investment. From this, your clients will have something to poke at and provide feedback. This will give you the chance to sort out major architectural decisions BEFORE you have invested a lot of time into building the real thing - and that is a BIG DEAL.

And, from there, you can build out your production system in any framework you choose. Even if it is going to be Drupal 7, you can build the prototype before you put in lots of work for custom rules, displays like panels, export your features, configuring your cache, and so on. Giving your stakeholders something to click on is a big confidence boost for both you and the client - it will give them a more concrete way to express their needs before you ever commit to foundation-level architectural decisions. Big win!
