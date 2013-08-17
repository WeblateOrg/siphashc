siphashc
========

python c-module for [siphash][1], based on [floodberry's version][2].

[![Build Status](https://travis-ci.org/cactus/siphashc.png?branch=master)](https://travis-ci.org/cactus/siphashc)

### Usage

~~~ python
>>> from siphashc import siphash
>>> siphash('sixteencharstrng', 'i need a hash of this')
10796923698683394048L
~~~

[1]: https://131002.net/siphash/
[2]: https://github.com/floodyberry/siphash
