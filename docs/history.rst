Changelog
=========

0.3 - Unreleased
----------------
* refactored namespace to sibboleth [Markus, Russell]

0.2 - Unreleased
----------------
* added https proxy support via httpsproxy_urllib2 [Russell]
* buildout now used for testing [Russell]
* removed dependency on xpath, adds 2.6 compatability [Russell]
* changed name of https proxy urllib2 egg to match names recognised by eggproxy [Russell]
* replaced custom parser with BeautifulSoup [Russell]
* added more handlers to approach the QUT login page [Russell]

0.1 - 2009-10-27
----------------
* pushed try count responsibility to credential manager class [Russell]
* chain now stops when cookie is set for initial host [Russell]
* added shib-login and shib-logout cli tools [Russell]
* updated to use adapter like pattern for processing forms [Russell]
* Initial release
