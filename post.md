# Immutable objects in Python

To keep programs easy to reason about, I try to avoid side effects and aim for a functional style of programming using immutable objects.
I'm happy to trade a few CPU cycles for a reduced demand of brain power.

Because we're talking about Python here, and [we're all responsible users](https://docs.python-guide.org/writing/style/#we-are-all-responsible-users), it's impossible to create actual *objects* that are *impossible* to mutate.
You can, however, create things that behave like objects that are impossible to mutate or actual objects that cannot be mutated by mistake.

## Named Tuples

The Python project I'm currently working on started before [data classes](https://docs.python.org/3/library/dataclasses.html) were available.
Additionally, this project is created for a client that prefers the use of as few dependencies as possible.
In that context, the following class for points emerged:

```python
from collections import namedtuple


class Point(namedtuple("_Point", ["x", "y"])):
    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
```

When you try to mutate an instance of this class, you'll be greeted with an `AttributeError`:

```sh
>>> from collections import namedtuple
>>> Point = namedtuple("_Point", ["x", "y"])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.x = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```

That looks pretty much like immutability to me.
One of the downsides of this approach is that `p` isn't an actual object.
It's a tuple.

```sh
>>> SomethingCompletelyDifferent = namedtuple("SomethingCompletelyDifferent", "a b")
>>> a = SomethingCompletelyDifferent(1, 2)
>>> p == a
True
>>> p == (1, 2)
True
```

Depending on how you're using instances of this class, this could be a big deal.
The documentation for the [attrs](https://www.attrs.org/en/stable/index.html) package list [a few more downsides](https://www.attrs.org/en/stable/why.html#namedtuples).

## Attrs

If you don't mind dependencies, you could use the aforementioned [attrs](https://www.attrs.org/en/stable/index.html) package and do this:

```python
import attr


@attr.s(frozen=True)
class Point:
    x = attr.ib()
    y = attr.ib()

    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
```

This behaves like you expect it to:

```sh
>>> import attr
>>> @attr.s(frozen=True)
... class Point:
...     x = attr.ib()
...     y = attr.ib()
...
>>> p = Point(1, 2)
>>> p.x
1
>>> p.x = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/lucengelen/.local/share/virtualenvs/python-immutable-1HIt_5XS/lib/python3.7/site-packages/attr/_make.py", line 428, in _frozen_setattrs
    raise FrozenInstanceError()
attr.exceptions.FrozenInstanceError
>>> p == (1, 2)
False
>>> p == Point(1, 2)
True
>>> p == Point(2, 1)
False
```

You can still mutate instances of this class, but not by accident:

```sh
>>> p = Point(1, 2)
>>> p.__dict__["x"] = 100
>>> p
Point(x=100, y=2)
```

## Data Classes

Since Python 3.7, you can use [data classes](https://docs.python.org/3/library/dataclasses.html) to achieve something similar to the variant using [attrs](https://www.attrs.org/en/stable/index.html):

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def scale(self, scale):
        return Point(self.x * scale, self.y * scale)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
```

This also behaves like you would expect:

```sh
>>> from dataclasses import dataclass
>>> @dataclass(frozen=True)
... class Point:
...     x: int
...     y: int
...
>>> p = Point(1, 2)
>>> p.x = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 3, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'x'
>>> p = Point(1, 2)
>>> p == Point(1, 2)
True
>>> p == Point(2, 1)
False
>>> p == (1, 2)
False
```

You can mutate instances in the same way as above, but I won't believe you if say you did this by mistake.

## Playground

If you want to play around with these variants, you could use the Python shell.
You could also take a look at the following repo: [https://github.com/ljpengelen/immutable-python-objects](https://github.com/ljpengelen/immutable-python-objects).
