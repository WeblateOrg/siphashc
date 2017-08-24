siphashc
========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/33758f86fbf44e929d85f47390093771)](https://www.codacy.com/app/Weblate/siphashc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=WeblateOrg/siphashc&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/WeblateOrg/siphashc.svg?branch=master)](https://travis-ci.org/WeblateOrg/siphashc)
[![Build status](https://ci.appveyor.com/api/projects/status/kgeohtb6as3xd9b7/branch/master?svg=true)](https://ci.appveyor.com/project/nijel/siphashc/branch/master)


### Introduction

siphashc is a python c-module for [siphash][1], based on [floodberry's
version][2].

It was merged from two versions of the module:

* https://github.com/cactus/siphashc
* https://github.com/carlopires/siphashc3


### Usage

#### Python2.7.x

~~~ python2.7.x
>>> from siphashc import siphash
>>> siphash('sixteencharstrng', 'i need a hash of this')
10796923698683394048L
~~~

#### Python3.4.x

~~~ python3.4.x
>>> from siphashc import siphash
>>> siphash('sixteencharstrng', 'i need a hash of this')
10796923698683394048
~~~

### License

Released under the [MIT license][3]. See `LICENSE.md` file for details.

[1]: https://131002.net/siphash/
[2]: https://github.com/floodyberry/siphash
[3]: http://www.opensource.org/licenses/mit-license.php
