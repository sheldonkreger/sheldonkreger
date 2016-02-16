Title: Site Rebuild in Pelican
Date: 2014-11-26 18:00
Author: Sheldon Kreger
Category: Programming

I chose to rebuild sheldonkreger.com using the Python-based static HTML generator Pelican. I admit I wanted to use MonkeyMan, but it is not supported very well.

While there are many great static HTML generators out there, I chose Pelican because it is widely supported, and I already know how to use PIP. But, why choose a static HTML generator over a CMS like Drupal - which, after all, is my area of experise?

1. CMS systems are harder to theme.
2. The site is simple and I do not need any special functionality.
3. Static HTML sites are very fast (espeically on GitHub Pages, using their CDN for free)!
4. I wanted to try something new.
5. Most importantly - deployments with git push.

It only took about 10 hours to put the whole thing together - and most of that time was spent fighting DNS and URL redirect settings from the previous site.

If you are setting up a simple blog, I highly suggest a static HTML generator due to their simplicity.
