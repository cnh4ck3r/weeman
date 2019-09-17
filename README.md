###WEEMAN - HTTP SERVER FOR PHISHING
=================================

![Weeman](https://4.bp.blogspot.com/-ngMJZqKmznE/VyBIIXHmJDI/AAAAAAAAFeU/4UgzhUEk9bsf2wYBWBKAU4QTtDNegnqLACLcB/s640/weeman_curr.png)

DISCLAIMER
==========
Usage of Weeman for attacking targets without prior mutual consent is illegal.
Weeman developer not responsible to any damage caused by Weeman.

ABOUT
======
HTTP server for phishing in python.
Weeman has support for most of the (bigest) websites.

Usually you will want run Weeman with DNS spoof attack. (see dsniff, ettercap).


WEEMAN WILL DO THE FOLLOWING STEPS:
----------------------------------------------------------------------
1. Create fake html page.
2. Wait for clients
3. Grab the data (POST).
4. Try to login the client to the original page :smiley:

REQUIREMENTS
=============
* Python <= 2.7.
* Python BeautifulSoup 4

INSTALL BEAUTIFULSOUP
-----------------------------------------
* Archlinux        - sudo pacman -S python2-beautifulsoup4
* Ubuntu/Linuxmint - sudo apt-get install python-bs4
* For another OS:  - sudo pip install beautifulsoup4

PLATFORMS
--------------------
* Linux (any)
* Mac (Not tested)
* Windows (Not tested)

[!] If weeman runs on your platform (Mac/Windows), please let me know.

USAGE
======
Just type `help`

RUN SERVER:
------------------
* For port 80 you need to run Weeman as root!

* Host to clone (Ex: http://twitter.com)
> set url http://twitter.com


> set action_url http://twitter.com

* The port Weeman server will listen
> set port 1111

* Start the server
> run

The settings will be saved for the next time you run weeman.py.

GET WEEMAB
=============
git clone https://github.com/cnh4ck3r/weeman
  
