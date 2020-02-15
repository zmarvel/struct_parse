
struct-parse
============

``struct_parse`` builds on the struct_ module in the standard library.
``struct`` lets you parse buffers by describing the format similarly to C struct
definitions. ``struct_parse`` aims to comply with the ``struct`` module's format
strings, but instead returns a (very flat) abstract syntax tree (AST).


Example
-------

.. code-block:: python

  import struct_parse

  field_list = struct_parse.parse('hhl')
  print(field_list.fields)

This will print::

  [<FieldType.FLOAT: 16>, <FieldType.FLOAT: 16>, <FieldType.LONG: 9>]


Use cases
---------

For simply unpacking packed binary data, the ``struct`` module does the trick.
The goal of this module is to enable the user to do other stuff with the format
string--we return a sequence of types instead of a sequence of values.


Compatibility
-------------

This library supports only Python 3.

.. _struct: https://docs.python.org/3/library/struct.html
