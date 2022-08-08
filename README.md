# PyOpenV2G
#### PyOpenV2G is a Python binding to OpenV2G, that uses the standard ctypes library.

## OpenV2G
OpenV2G - an open source project implementing the basic functionality of the ISO IEC 15118 vehicle to grid (V2G) communication interface 
Version 0.9.5, released March 11, 2022

http://openv2g.sourceforge.net/

For more information, please visit https://github.com/Martin-P/OpenV2G

NOTE: The project is in its early stages.

Usage examples can be found in the open_v2g_tests.py.

To compile and generate the OpenV2G library (.so):
$ ./compile.sh

Most of OpenV2G structs and constants were generated automatically by parsing the OpenV2G library with regex expressions.

There are still several structures/bindings that aren't fixed.
