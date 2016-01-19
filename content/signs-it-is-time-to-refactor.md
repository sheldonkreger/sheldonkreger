Title: Signs it is Time to Refactor
Author: Sheldon Kreger
Date: 2014-12-11 11:00
Category: Programming
Tags: Programming

Software systems are expensive. After building a big application, one might hope there is a reasonable lifetime for it to live in the wild before it needs to be replaced. I have worked on sites that were implemented successfully and will have a lifetime of many years. But, especially on large systems, such success is rare. Frequently, we find ourselves reworking our code, starting the minute the initial build is finished.

Contrary to my initial impression, this is not necessarily a bad thing. Reading from and speaking with highly experienced programmers has taught me that many projects never actually "finish", they just continue to be rebuilt as time passes. This is not because the developers did not know what they were doing, but because this is often the best practice in the software industry today.

Here are some common reasons why it may be time to refactor or rebuild an application.

## 1. Changing Requirements
Oftentimes, the requirements for a project expand or change while the software is being developed. And, almost always, the requirements also change after the project is finished. Once requirements change dramatically, it may make sense to rebuild an application from the ground up using different tools, languages, and frameworks.

## 2. You Have Reached the Point of No Return
If you have reached a point where adding more developers to your team no longer results in more work getting done, then it is time to rebuild. If you cannot get any benefit from adding team members, then you have outgrown your softare and it is time to move on.

## 3. Endless Performance Issues
If you spend a lot of time trying to enhance performance in your application, yet it continues to become slower and slower, it is time to rebuild. There is no reason to waste time putting more lipstick on your pig.

## 4. Overriding Core Technology
If you rely on a fundamental piece of technology which you have used to build your application, but you have to continuously override its normal behavior, then it is time to rebuild. The further you stray from what the technology is supposed to actually do, the harder it will be to work on your application. Software updates which should be quick and easy will become time consuming or even impossible - and that could include security updates that need to go live fast. If your requirements are
no longer in alignment with your core technology, do yourself a favor and move on.

## 5. Bug Reports Coming In Faster Than You Can Fix Them
If your software is so buggy that you cannot keep up with all the new issues coming in, it may be time to rebuild. However, newly launched products may experience this kind of problem for some time after the initial deployment, so do not panic early.

## 6. All Your Developers Keep Quitting
If you have problems retaining talent on your team, there are likely two issues: Mismanagement of the project requirements and frustration with existing infrastructure will force programmers to walk away. If you keep hiring people and they leave within a short period of time, there is a good chance that your underlying technology is mismatched with the requirements of the project. The developer can see this after a few months, and if they do not see any sign of change, they will probably just find another
job.

## 7. Outdated Technology
Finally - and this is pretty obvious - if your underlying software system is losing support in terms of technical updates (especially security updates), then it is time to rebuild.
