siphashc
========

## Current status of project

Ongoing maintenance of the project (and pypi package) has transferred to Michal
Čihař ([nijel][4]).  
[WeblateOrg/siphashc][5] is now the canonical location.


### Introduction

[![Build Status](https://travis-ci.org/cactus/siphashc.png?branch=master)](https://travis-ci.org/cactus/siphashc)

siphashc is a python2 c-module for [siphash][1], based on [floodberry's
version][2].


### Usage

~~~ python
>>> from siphashc import siphash
>>> siphash('sixteencharstrng', 'i need a hash of this')
10796923698683394048L
~~~

### License

Released under the [MIT license][3]. See `LICENSE.md` file for details.

[1]: https://131002.net/siphash/
[2]: https://github.com/floodyberry/siphash
[3]: http://www.opensource.org/licenses/mit-license.php
[4]: https://github.com/nijel
[5]: https://github.com/WeblateOrg/siphashc
