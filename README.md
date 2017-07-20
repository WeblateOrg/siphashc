siphashc
========

python c-module for [siphash][1], based on [floodberry's version][2].

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c85ea9de2884e6f88b23ccf240e6d05)](https://www.codacy.com/app/nijel/siphashc-merge?utm_source=github.com&utm_medium=referral&utm_content=nijel/siphashc-merge&utm_campaign=badger)
[![Build Status](https://travis-ci.org/nijel/siphashc-merge.svg?branch=master)](https://travis-ci.org/nijel/siphashc-merge)
[![Build status](https://ci.appveyor.com/api/projects/status/kgeohtb6as3xd9b7/branch/master?svg=true)](https://ci.appveyor.com/project/nijel/siphashc-merge/branch/master)

This is attempt to merge two versions of the module:

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

Released under the [MIT license](http://www.opensource.org/licenses/mit-license.php). See `LICENSE.md` file for details.

[1]: https://131002.net/siphash/
[2]: https://github.com/floodyberry/siphash
