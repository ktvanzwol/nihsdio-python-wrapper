r"""Wrapper for niHSDIO.h

Generated with:
C:\Users\Karsten\AppData\Local\Programs\Python\Python311\Scripts\ctypesgen -l niHSDIO_64 -o niHSDIO_64.py C:\Program Files (x86)\IVI Foundation\IVI\Include\niHSDIO.h -I C:\Program Files (x86)\IVI Foundation\IVI\Include

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["niHSDIO_64"] = load_library("niHSDIO_64")

# 1 libraries
# End libraries

# No modules

ViUInt32 = c_ulong# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 100

ViInt32 = c_long# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 101

ViUInt16 = c_ushort# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 109

ViInt16 = c_short# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 113

ViUInt8 = c_ubyte# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 117

ViChar = c_char# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 125

ViPChar = POINTER(ViChar)# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 126

ViReal64 = c_double# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 141

ViString = ViPChar# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 150

ViConstString = POINTER(ViChar)# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 152

ViRsrc = ViString# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 158

ViBoolean = ViUInt16# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 163

ViStatus = ViInt32# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 167

ViObject = ViUInt32# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 175

ViSession = ViObject# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 179

ViAttr = ViUInt32# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 183

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 504
if _libs["niHSDIO_64"].has("niHSDIO_InitAcquisitionSession", "cdecl"):
    niHSDIO_InitAcquisitionSession = _libs["niHSDIO_64"].get("niHSDIO_InitAcquisitionSession", "cdecl")
    niHSDIO_InitAcquisitionSession.argtypes = [ViRsrc, ViBoolean, ViBoolean, ViConstString, POINTER(ViSession)]
    niHSDIO_InitAcquisitionSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 510
if _libs["niHSDIO_64"].has("niHSDIO_InitGenerationSession", "cdecl"):
    niHSDIO_InitGenerationSession = _libs["niHSDIO_64"].get("niHSDIO_InitGenerationSession", "cdecl")
    niHSDIO_InitGenerationSession.argtypes = [ViRsrc, ViBoolean, ViBoolean, ViConstString, POINTER(ViSession)]
    niHSDIO_InitGenerationSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 516
if _libs["niHSDIO_64"].has("niHSDIO_close", "cdecl"):
    niHSDIO_close = _libs["niHSDIO_64"].get("niHSDIO_close", "cdecl")
    niHSDIO_close.argtypes = [ViSession]
    niHSDIO_close.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 520
if _libs["niHSDIO_64"].has("niHSDIO_LockSession", "cdecl"):
    niHSDIO_LockSession = _libs["niHSDIO_64"].get("niHSDIO_LockSession", "cdecl")
    niHSDIO_LockSession.argtypes = [ViSession, POINTER(ViBoolean)]
    niHSDIO_LockSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 523
if _libs["niHSDIO_64"].has("niHSDIO_UnlockSession", "cdecl"):
    niHSDIO_UnlockSession = _libs["niHSDIO_64"].get("niHSDIO_UnlockSession", "cdecl")
    niHSDIO_UnlockSession.argtypes = [ViSession, POINTER(ViBoolean)]
    niHSDIO_UnlockSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 528
if _libs["niHSDIO_64"].has("niHSDIO_Initiate", "cdecl"):
    niHSDIO_Initiate = _libs["niHSDIO_64"].get("niHSDIO_Initiate", "cdecl")
    niHSDIO_Initiate.argtypes = [ViSession]
    niHSDIO_Initiate.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 530
if _libs["niHSDIO_64"].has("niHSDIO_Abort", "cdecl"):
    niHSDIO_Abort = _libs["niHSDIO_64"].get("niHSDIO_Abort", "cdecl")
    niHSDIO_Abort.argtypes = [ViSession]
    niHSDIO_Abort.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 532
if _libs["niHSDIO_64"].has("niHSDIO_CommitStatic", "cdecl"):
    niHSDIO_CommitStatic = _libs["niHSDIO_64"].get("niHSDIO_CommitStatic", "cdecl")
    niHSDIO_CommitStatic.argtypes = [ViSession]
    niHSDIO_CommitStatic.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 534
if _libs["niHSDIO_64"].has("niHSDIO_CommitDynamic", "cdecl"):
    niHSDIO_CommitDynamic = _libs["niHSDIO_64"].get("niHSDIO_CommitDynamic", "cdecl")
    niHSDIO_CommitDynamic.argtypes = [ViSession]
    niHSDIO_CommitDynamic.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 536
if _libs["niHSDIO_64"].has("niHSDIO_WaitUntilDone", "cdecl"):
    niHSDIO_WaitUntilDone = _libs["niHSDIO_64"].get("niHSDIO_WaitUntilDone", "cdecl")
    niHSDIO_WaitUntilDone.argtypes = [ViSession, ViInt32]
    niHSDIO_WaitUntilDone.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 539
if _libs["niHSDIO_64"].has("niHSDIO_IsDone", "cdecl"):
    niHSDIO_IsDone = _libs["niHSDIO_64"].get("niHSDIO_IsDone", "cdecl")
    niHSDIO_IsDone.argtypes = [ViSession, POINTER(ViBoolean)]
    niHSDIO_IsDone.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 542
if _libs["niHSDIO_64"].has("niHSDIO_TristateChannels", "cdecl"):
    niHSDIO_TristateChannels = _libs["niHSDIO_64"].get("niHSDIO_TristateChannels", "cdecl")
    niHSDIO_TristateChannels.argtypes = [ViSession, ViConstString, ViBoolean]
    niHSDIO_TristateChannels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 548
if _libs["niHSDIO_64"].has("niHSDIO_AssignStaticChannels", "cdecl"):
    niHSDIO_AssignStaticChannels = _libs["niHSDIO_64"].get("niHSDIO_AssignStaticChannels", "cdecl")
    niHSDIO_AssignStaticChannels.argtypes = [ViSession, ViConstString]
    niHSDIO_AssignStaticChannels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 551
if _libs["niHSDIO_64"].has("niHSDIO_WriteStaticU32", "cdecl"):
    niHSDIO_WriteStaticU32 = _libs["niHSDIO_64"].get("niHSDIO_WriteStaticU32", "cdecl")
    niHSDIO_WriteStaticU32.argtypes = [ViSession, ViUInt32, ViUInt32]
    niHSDIO_WriteStaticU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 554
if _libs["niHSDIO_64"].has("niHSDIO_ReadStaticU32", "cdecl"):
    niHSDIO_ReadStaticU32 = _libs["niHSDIO_64"].get("niHSDIO_ReadStaticU32", "cdecl")
    niHSDIO_ReadStaticU32.argtypes = [ViSession, POINTER(ViUInt32)]
    niHSDIO_ReadStaticU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 557
if _libs["niHSDIO_64"].has("niHSDIO_WriteStaticPFIU32", "cdecl"):
    niHSDIO_WriteStaticPFIU32 = _libs["niHSDIO_64"].get("niHSDIO_WriteStaticPFIU32", "cdecl")
    niHSDIO_WriteStaticPFIU32.argtypes = [ViSession, ViUInt32, ViUInt32]
    niHSDIO_WriteStaticPFIU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 560
if _libs["niHSDIO_64"].has("niHSDIO_ReadStaticPFIU32", "cdecl"):
    niHSDIO_ReadStaticPFIU32 = _libs["niHSDIO_64"].get("niHSDIO_ReadStaticPFIU32", "cdecl")
    niHSDIO_ReadStaticPFIU32.argtypes = [ViSession, POINTER(ViUInt32)]
    niHSDIO_ReadStaticPFIU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 565
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDataVoltageLogicFamily", "cdecl"):
    niHSDIO_ConfigureDataVoltageLogicFamily = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDataVoltageLogicFamily", "cdecl")
    niHSDIO_ConfigureDataVoltageLogicFamily.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDataVoltageLogicFamily.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 569
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDataVoltageCustomLevels", "cdecl"):
    niHSDIO_ConfigureDataVoltageCustomLevels = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDataVoltageCustomLevels", "cdecl")
    niHSDIO_ConfigureDataVoltageCustomLevels.argtypes = [ViSession, ViConstString, ViReal64, ViReal64]
    niHSDIO_ConfigureDataVoltageCustomLevels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 574
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureTriggerVoltageLogicFamily", "cdecl"):
    niHSDIO_ConfigureTriggerVoltageLogicFamily = _libs["niHSDIO_64"].get("niHSDIO_ConfigureTriggerVoltageLogicFamily", "cdecl")
    niHSDIO_ConfigureTriggerVoltageLogicFamily.argtypes = [ViSession, ViInt32]
    niHSDIO_ConfigureTriggerVoltageLogicFamily.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 577
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureTriggerVoltageCustomLevels", "cdecl"):
    niHSDIO_ConfigureTriggerVoltageCustomLevels = _libs["niHSDIO_64"].get("niHSDIO_ConfigureTriggerVoltageCustomLevels", "cdecl")
    niHSDIO_ConfigureTriggerVoltageCustomLevels.argtypes = [ViSession, ViReal64, ViReal64]
    niHSDIO_ConfigureTriggerVoltageCustomLevels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 581
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureEventVoltageLogicFamily", "cdecl"):
    niHSDIO_ConfigureEventVoltageLogicFamily = _libs["niHSDIO_64"].get("niHSDIO_ConfigureEventVoltageLogicFamily", "cdecl")
    niHSDIO_ConfigureEventVoltageLogicFamily.argtypes = [ViSession, ViInt32]
    niHSDIO_ConfigureEventVoltageLogicFamily.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 584
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureEventVoltageCustomLevels", "cdecl"):
    niHSDIO_ConfigureEventVoltageCustomLevels = _libs["niHSDIO_64"].get("niHSDIO_ConfigureEventVoltageCustomLevels", "cdecl")
    niHSDIO_ConfigureEventVoltageCustomLevels.argtypes = [ViSession, ViReal64, ViReal64]
    niHSDIO_ConfigureEventVoltageCustomLevels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 590
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureRefClock", "cdecl"):
    niHSDIO_ConfigureRefClock = _libs["niHSDIO_64"].get("niHSDIO_ConfigureRefClock", "cdecl")
    niHSDIO_ConfigureRefClock.argtypes = [ViSession, ViConstString, ViReal64]
    niHSDIO_ConfigureRefClock.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 594
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSampleClock", "cdecl"):
    niHSDIO_ConfigureSampleClock = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSampleClock", "cdecl")
    niHSDIO_ConfigureSampleClock.argtypes = [ViSession, ViConstString, ViReal64]
    niHSDIO_ConfigureSampleClock.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 598
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDataPosition", "cdecl"):
    niHSDIO_ConfigureDataPosition = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDataPosition", "cdecl")
    niHSDIO_ConfigureDataPosition.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDataPosition.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 602
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDataPositionDelay", "cdecl"):
    niHSDIO_ConfigureDataPositionDelay = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDataPositionDelay", "cdecl")
    niHSDIO_ConfigureDataPositionDelay.argtypes = [ViSession, ViConstString, ViReal64]
    niHSDIO_ConfigureDataPositionDelay.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 606
if _libs["niHSDIO_64"].has("niHSDIO_AdjustSampleClockRelativeDelay", "cdecl"):
    niHSDIO_AdjustSampleClockRelativeDelay = _libs["niHSDIO_64"].get("niHSDIO_AdjustSampleClockRelativeDelay", "cdecl")
    niHSDIO_AdjustSampleClockRelativeDelay.argtypes = [ViSession, ViReal64]
    niHSDIO_AdjustSampleClockRelativeDelay.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 611
if _libs["niHSDIO_64"].has("niHSDIO_SendSoftwareEdgeTrigger", "cdecl"):
    niHSDIO_SendSoftwareEdgeTrigger = _libs["niHSDIO_64"].get("niHSDIO_SendSoftwareEdgeTrigger", "cdecl")
    niHSDIO_SendSoftwareEdgeTrigger.argtypes = [ViSession, ViInt32, ViConstString]
    niHSDIO_SendSoftwareEdgeTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 616
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalLevelPauseTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalLevelPauseTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalLevelPauseTrigger", "cdecl")
    niHSDIO_ConfigureDigitalLevelPauseTrigger.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalLevelPauseTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 620
if _libs["niHSDIO_64"].has("niHSDIO_DisablePauseTrigger", "cdecl"):
    niHSDIO_DisablePauseTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisablePauseTrigger", "cdecl")
    niHSDIO_DisablePauseTrigger.argtypes = [ViSession]
    niHSDIO_DisablePauseTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 622
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchPauseTrigger", "cdecl"):
    niHSDIO_ConfigurePatternMatchPauseTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchPauseTrigger", "cdecl")
    niHSDIO_ConfigurePatternMatchPauseTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigurePatternMatchPauseTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 627
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchPauseTriggerU32", "cdecl"):
    niHSDIO_ConfigurePatternMatchPauseTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchPauseTriggerU32", "cdecl")
    niHSDIO_ConfigurePatternMatchPauseTriggerU32.argtypes = [ViSession, ViConstString, ViUInt32, ViInt32]
    niHSDIO_ConfigurePatternMatchPauseTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 633
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalEdgeScriptTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalEdgeScriptTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalEdgeScriptTrigger", "cdecl")
    niHSDIO_ConfigureDigitalEdgeScriptTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalEdgeScriptTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 638
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalLevelScriptTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalLevelScriptTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalLevelScriptTrigger", "cdecl")
    niHSDIO_ConfigureDigitalLevelScriptTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalLevelScriptTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 643
if _libs["niHSDIO_64"].has("niHSDIO_DisableScriptTrigger", "cdecl"):
    niHSDIO_DisableScriptTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisableScriptTrigger", "cdecl")
    niHSDIO_DisableScriptTrigger.argtypes = [ViSession, ViConstString]
    niHSDIO_DisableScriptTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 646
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSoftwareScriptTrigger", "cdecl"):
    niHSDIO_ConfigureSoftwareScriptTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSoftwareScriptTrigger", "cdecl")
    niHSDIO_ConfigureSoftwareScriptTrigger.argtypes = [ViSession, ViConstString]
    niHSDIO_ConfigureSoftwareScriptTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 650
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalEdgeStartTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalEdgeStartTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalEdgeStartTrigger", "cdecl")
    niHSDIO_ConfigureDigitalEdgeStartTrigger.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalEdgeStartTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 654
if _libs["niHSDIO_64"].has("niHSDIO_DisableStartTrigger", "cdecl"):
    niHSDIO_DisableStartTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisableStartTrigger", "cdecl")
    niHSDIO_DisableStartTrigger.argtypes = [ViSession]
    niHSDIO_DisableStartTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 656
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSoftwareStartTrigger", "cdecl"):
    niHSDIO_ConfigureSoftwareStartTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSoftwareStartTrigger", "cdecl")
    niHSDIO_ConfigureSoftwareStartTrigger.argtypes = [ViSession]
    niHSDIO_ConfigureSoftwareStartTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 658
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchStartTrigger", "cdecl"):
    niHSDIO_ConfigurePatternMatchStartTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchStartTrigger", "cdecl")
    niHSDIO_ConfigurePatternMatchStartTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigurePatternMatchStartTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 663
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchStartTriggerU32", "cdecl"):
    niHSDIO_ConfigurePatternMatchStartTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchStartTriggerU32", "cdecl")
    niHSDIO_ConfigurePatternMatchStartTriggerU32.argtypes = [ViSession, ViConstString, ViUInt32, ViInt32]
    niHSDIO_ConfigurePatternMatchStartTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 668
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchStartTrigger", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchStartTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchStartTrigger", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchStartTrigger.argtypes = [ViSession, ViConstString, ViConstString]
    niHSDIO_ConfigureMultiSamplePatternMatchStartTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 672
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchStartTriggerU32", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchStartTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchStartTriggerU32", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchStartTriggerU32.argtypes = [ViSession, ViConstString, POINTER(ViUInt32), ViInt32]
    niHSDIO_ConfigureMultiSamplePatternMatchStartTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 678
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalEdgeAdvanceTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalEdgeAdvanceTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalEdgeAdvanceTrigger", "cdecl")
    niHSDIO_ConfigureDigitalEdgeAdvanceTrigger.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalEdgeAdvanceTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 682
if _libs["niHSDIO_64"].has("niHSDIO_DisableAdvanceTrigger", "cdecl"):
    niHSDIO_DisableAdvanceTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisableAdvanceTrigger", "cdecl")
    niHSDIO_DisableAdvanceTrigger.argtypes = [ViSession]
    niHSDIO_DisableAdvanceTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 684
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSoftwareAdvanceTrigger", "cdecl"):
    niHSDIO_ConfigureSoftwareAdvanceTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSoftwareAdvanceTrigger", "cdecl")
    niHSDIO_ConfigureSoftwareAdvanceTrigger.argtypes = [ViSession]
    niHSDIO_ConfigureSoftwareAdvanceTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 686
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchAdvanceTrigger", "cdecl"):
    niHSDIO_ConfigurePatternMatchAdvanceTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchAdvanceTrigger", "cdecl")
    niHSDIO_ConfigurePatternMatchAdvanceTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigurePatternMatchAdvanceTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 691
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchAdvanceTriggerU32", "cdecl"):
    niHSDIO_ConfigurePatternMatchAdvanceTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchAdvanceTriggerU32", "cdecl")
    niHSDIO_ConfigurePatternMatchAdvanceTriggerU32.argtypes = [ViSession, ViConstString, ViUInt32, ViInt32]
    niHSDIO_ConfigurePatternMatchAdvanceTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 696
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTrigger", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTrigger", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTrigger.argtypes = [ViSession, ViConstString, ViConstString]
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 700
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTriggerU32", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTriggerU32", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTriggerU32.argtypes = [ViSession, ViConstString, POINTER(ViUInt32), ViInt32]
    niHSDIO_ConfigureMultiSamplePatternMatchAdvanceTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 706
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalEdgeRefTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalEdgeRefTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalEdgeRefTrigger", "cdecl")
    niHSDIO_ConfigureDigitalEdgeRefTrigger.argtypes = [ViSession, ViConstString, ViInt32, ViInt32]
    niHSDIO_ConfigureDigitalEdgeRefTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 711
if _libs["niHSDIO_64"].has("niHSDIO_DisableRefTrigger", "cdecl"):
    niHSDIO_DisableRefTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisableRefTrigger", "cdecl")
    niHSDIO_DisableRefTrigger.argtypes = [ViSession]
    niHSDIO_DisableRefTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 713
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSoftwareRefTrigger", "cdecl"):
    niHSDIO_ConfigureSoftwareRefTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSoftwareRefTrigger", "cdecl")
    niHSDIO_ConfigureSoftwareRefTrigger.argtypes = [ViSession, ViInt32]
    niHSDIO_ConfigureSoftwareRefTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 716
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchRefTrigger", "cdecl"):
    niHSDIO_ConfigurePatternMatchRefTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchRefTrigger", "cdecl")
    niHSDIO_ConfigurePatternMatchRefTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32, ViInt32]
    niHSDIO_ConfigurePatternMatchRefTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 722
if _libs["niHSDIO_64"].has("niHSDIO_ConfigurePatternMatchRefTriggerU32", "cdecl"):
    niHSDIO_ConfigurePatternMatchRefTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigurePatternMatchRefTriggerU32", "cdecl")
    niHSDIO_ConfigurePatternMatchRefTriggerU32.argtypes = [ViSession, ViConstString, ViUInt32, ViInt32, ViInt32]
    niHSDIO_ConfigurePatternMatchRefTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 728
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchRefTrigger", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchRefTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchRefTrigger", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchRefTrigger.argtypes = [ViSession, ViConstString, ViConstString, ViInt32]
    niHSDIO_ConfigureMultiSamplePatternMatchRefTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 733
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureMultiSamplePatternMatchRefTriggerU32", "cdecl"):
    niHSDIO_ConfigureMultiSamplePatternMatchRefTriggerU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigureMultiSamplePatternMatchRefTriggerU32", "cdecl")
    niHSDIO_ConfigureMultiSamplePatternMatchRefTriggerU32.argtypes = [ViSession, ViConstString, POINTER(ViUInt32), ViInt32, ViInt32]
    niHSDIO_ConfigureMultiSamplePatternMatchRefTriggerU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 740
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDigitalEdgeStopTrigger", "cdecl"):
    niHSDIO_ConfigureDigitalEdgeStopTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDigitalEdgeStopTrigger", "cdecl")
    niHSDIO_ConfigureDigitalEdgeStopTrigger.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDigitalEdgeStopTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 744
if _libs["niHSDIO_64"].has("niHSDIO_DisableStopTrigger", "cdecl"):
    niHSDIO_DisableStopTrigger = _libs["niHSDIO_64"].get("niHSDIO_DisableStopTrigger", "cdecl")
    niHSDIO_DisableStopTrigger.argtypes = [ViSession]
    niHSDIO_DisableStopTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 746
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureSoftwareStopTrigger", "cdecl"):
    niHSDIO_ConfigureSoftwareStopTrigger = _libs["niHSDIO_64"].get("niHSDIO_ConfigureSoftwareStopTrigger", "cdecl")
    niHSDIO_ConfigureSoftwareStopTrigger.argtypes = [ViSession]
    niHSDIO_ConfigureSoftwareStopTrigger.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 750
if _libs["niHSDIO_64"].has("niHSDIO_ExportSignal", "cdecl"):
    niHSDIO_ExportSignal = _libs["niHSDIO_64"].get("niHSDIO_ExportSignal", "cdecl")
    niHSDIO_ExportSignal.argtypes = [ViSession, ViInt32, ViConstString, ViConstString]
    niHSDIO_ExportSignal.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 757
if _libs["niHSDIO_64"].has("niHSDIO_AssignDynamicChannels", "cdecl"):
    niHSDIO_AssignDynamicChannels = _libs["niHSDIO_64"].get("niHSDIO_AssignDynamicChannels", "cdecl")
    niHSDIO_AssignDynamicChannels.argtypes = [ViSession, ViConstString]
    niHSDIO_AssignDynamicChannels.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 760
if _libs["niHSDIO_64"].has("niHSDIO_AllocateNamedWaveform", "cdecl"):
    niHSDIO_AllocateNamedWaveform = _libs["niHSDIO_64"].get("niHSDIO_AllocateNamedWaveform", "cdecl")
    niHSDIO_AllocateNamedWaveform.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_AllocateNamedWaveform.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 764
if _libs["niHSDIO_64"].has("niHSDIO_DeleteNamedWaveform", "cdecl"):
    niHSDIO_DeleteNamedWaveform = _libs["niHSDIO_64"].get("niHSDIO_DeleteNamedWaveform", "cdecl")
    niHSDIO_DeleteNamedWaveform.argtypes = [ViSession, ViConstString]
    niHSDIO_DeleteNamedWaveform.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 767
if _libs["niHSDIO_64"].has("niHSDIO_WriteNamedWaveformU32", "cdecl"):
    niHSDIO_WriteNamedWaveformU32 = _libs["niHSDIO_64"].get("niHSDIO_WriteNamedWaveformU32", "cdecl")
    niHSDIO_WriteNamedWaveformU32.argtypes = [ViSession, ViConstString, ViInt32, POINTER(ViUInt32)]
    niHSDIO_WriteNamedWaveformU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 772
if _libs["niHSDIO_64"].has("niHSDIO_WriteNamedWaveformU16", "cdecl"):
    niHSDIO_WriteNamedWaveformU16 = _libs["niHSDIO_64"].get("niHSDIO_WriteNamedWaveformU16", "cdecl")
    niHSDIO_WriteNamedWaveformU16.argtypes = [ViSession, ViConstString, ViInt32, POINTER(ViUInt16)]
    niHSDIO_WriteNamedWaveformU16.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 777
if _libs["niHSDIO_64"].has("niHSDIO_WriteNamedWaveformU8", "cdecl"):
    niHSDIO_WriteNamedWaveformU8 = _libs["niHSDIO_64"].get("niHSDIO_WriteNamedWaveformU8", "cdecl")
    niHSDIO_WriteNamedWaveformU8.argtypes = [ViSession, ViConstString, ViInt32, POINTER(ViUInt8)]
    niHSDIO_WriteNamedWaveformU8.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 782
if _libs["niHSDIO_64"].has("niHSDIO_WriteNamedWaveformWDT", "cdecl"):
    niHSDIO_WriteNamedWaveformWDT = _libs["niHSDIO_64"].get("niHSDIO_WriteNamedWaveformWDT", "cdecl")
    niHSDIO_WriteNamedWaveformWDT.argtypes = [ViSession, ViConstString, ViInt32, ViInt32, POINTER(ViUInt8)]
    niHSDIO_WriteNamedWaveformWDT.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 788
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureGenerationMode", "cdecl"):
    niHSDIO_ConfigureGenerationMode = _libs["niHSDIO_64"].get("niHSDIO_ConfigureGenerationMode", "cdecl")
    niHSDIO_ConfigureGenerationMode.argtypes = [ViSession, ViInt32]
    niHSDIO_ConfigureGenerationMode.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 791
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureGenerationRepeat", "cdecl"):
    niHSDIO_ConfigureGenerationRepeat = _libs["niHSDIO_64"].get("niHSDIO_ConfigureGenerationRepeat", "cdecl")
    niHSDIO_ConfigureGenerationRepeat.argtypes = [ViSession, ViInt32, ViInt32]
    niHSDIO_ConfigureGenerationRepeat.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 795
if _libs["niHSDIO_64"].has("niHSDIO_WriteScript", "cdecl"):
    niHSDIO_WriteScript = _libs["niHSDIO_64"].get("niHSDIO_WriteScript", "cdecl")
    niHSDIO_WriteScript.argtypes = [ViSession, ViConstString]
    niHSDIO_WriteScript.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 798
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureWaveformToGenerate", "cdecl"):
    niHSDIO_ConfigureWaveformToGenerate = _libs["niHSDIO_64"].get("niHSDIO_ConfigureWaveformToGenerate", "cdecl")
    niHSDIO_ConfigureWaveformToGenerate.argtypes = [ViSession, ViConstString]
    niHSDIO_ConfigureWaveformToGenerate.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 801
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureScriptToGenerate", "cdecl"):
    niHSDIO_ConfigureScriptToGenerate = _libs["niHSDIO_64"].get("niHSDIO_ConfigureScriptToGenerate", "cdecl")
    niHSDIO_ConfigureScriptToGenerate.argtypes = [ViSession, ViConstString]
    niHSDIO_ConfigureScriptToGenerate.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 804
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureInitialState", "cdecl"):
    niHSDIO_ConfigureInitialState = _libs["niHSDIO_64"].get("niHSDIO_ConfigureInitialState", "cdecl")
    niHSDIO_ConfigureInitialState.argtypes = [ViSession, ViConstString, ViConstString]
    niHSDIO_ConfigureInitialState.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 808
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureInitialStateU32", "cdecl"):
    niHSDIO_ConfigureInitialStateU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigureInitialStateU32", "cdecl")
    niHSDIO_ConfigureInitialStateU32.argtypes = [ViSession, ViUInt32]
    niHSDIO_ConfigureInitialStateU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 811
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureIdleState", "cdecl"):
    niHSDIO_ConfigureIdleState = _libs["niHSDIO_64"].get("niHSDIO_ConfigureIdleState", "cdecl")
    niHSDIO_ConfigureIdleState.argtypes = [ViSession, ViConstString, ViConstString]
    niHSDIO_ConfigureIdleState.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 815
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureIdleStateU32", "cdecl"):
    niHSDIO_ConfigureIdleStateU32 = _libs["niHSDIO_64"].get("niHSDIO_ConfigureIdleStateU32", "cdecl")
    niHSDIO_ConfigureIdleStateU32.argtypes = [ViSession, ViUInt32]
    niHSDIO_ConfigureIdleStateU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 818
if _libs["niHSDIO_64"].has("niHSDIO_SetNamedWaveformNextWritePosition", "cdecl"):
    niHSDIO_SetNamedWaveformNextWritePosition = _libs["niHSDIO_64"].get("niHSDIO_SetNamedWaveformNextWritePosition", "cdecl")
    niHSDIO_SetNamedWaveformNextWritePosition.argtypes = [ViSession, ViConstString, ViInt32, ViInt32]
    niHSDIO_SetNamedWaveformNextWritePosition.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 829
class struct_niHSDIO_wfmInfo(Structure):
    pass

struct_niHSDIO_wfmInfo.__slots__ = [
    'absoluteTimestamp',
    'relativeTimestamp',
    'dt',
    'actualSamplesRead',
    'reserved1',
    'reserved2',
]
struct_niHSDIO_wfmInfo._fields_ = [
    ('absoluteTimestamp', ViReal64),
    ('relativeTimestamp', ViReal64),
    ('dt', ViReal64),
    ('actualSamplesRead', ViInt32),
    ('reserved1', ViReal64),
    ('reserved2', ViReal64),
]

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 842
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureAcquisitionSize", "cdecl"):
    niHSDIO_ConfigureAcquisitionSize = _libs["niHSDIO_64"].get("niHSDIO_ConfigureAcquisitionSize", "cdecl")
    niHSDIO_ConfigureAcquisitionSize.argtypes = [ViSession, ViInt32, ViInt32]
    niHSDIO_ConfigureAcquisitionSize.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 846
if _libs["niHSDIO_64"].has("niHSDIO_ConfigureDataInterpretation", "cdecl"):
    niHSDIO_ConfigureDataInterpretation = _libs["niHSDIO_64"].get("niHSDIO_ConfigureDataInterpretation", "cdecl")
    niHSDIO_ConfigureDataInterpretation.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_ConfigureDataInterpretation.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 850
if _libs["niHSDIO_64"].has("niHSDIO_GetFetchBacklog", "cdecl"):
    niHSDIO_GetFetchBacklog = _libs["niHSDIO_64"].get("niHSDIO_GetFetchBacklog", "cdecl")
    niHSDIO_GetFetchBacklog.argtypes = [ViSession, ViInt32, POINTER(ViInt32)]
    niHSDIO_GetFetchBacklog.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 854
if _libs["niHSDIO_64"].has("niHSDIO_FetchMultiRecordU32", "cdecl"):
    niHSDIO_FetchMultiRecordU32 = _libs["niHSDIO_64"].get("niHSDIO_FetchMultiRecordU32", "cdecl")
    niHSDIO_FetchMultiRecordU32.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt32), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_FetchMultiRecordU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 862
if _libs["niHSDIO_64"].has("niHSDIO_FetchMultiRecordU16", "cdecl"):
    niHSDIO_FetchMultiRecordU16 = _libs["niHSDIO_64"].get("niHSDIO_FetchMultiRecordU16", "cdecl")
    niHSDIO_FetchMultiRecordU16.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt16), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_FetchMultiRecordU16.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 870
if _libs["niHSDIO_64"].has("niHSDIO_FetchMultiRecordU8", "cdecl"):
    niHSDIO_FetchMultiRecordU8 = _libs["niHSDIO_64"].get("niHSDIO_FetchMultiRecordU8", "cdecl")
    niHSDIO_FetchMultiRecordU8.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt8), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_FetchMultiRecordU8.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 878
if _libs["niHSDIO_64"].has("niHSDIO_FetchWaveformU32", "cdecl"):
    niHSDIO_FetchWaveformU32 = _libs["niHSDIO_64"].get("niHSDIO_FetchWaveformU32", "cdecl")
    niHSDIO_FetchWaveformU32.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt32)]
    niHSDIO_FetchWaveformU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 884
if _libs["niHSDIO_64"].has("niHSDIO_FetchWaveformU16", "cdecl"):
    niHSDIO_FetchWaveformU16 = _libs["niHSDIO_64"].get("niHSDIO_FetchWaveformU16", "cdecl")
    niHSDIO_FetchWaveformU16.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt16)]
    niHSDIO_FetchWaveformU16.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 890
if _libs["niHSDIO_64"].has("niHSDIO_FetchWaveformU8", "cdecl"):
    niHSDIO_FetchWaveformU8 = _libs["niHSDIO_64"].get("niHSDIO_FetchWaveformU8", "cdecl")
    niHSDIO_FetchWaveformU8.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt8)]
    niHSDIO_FetchWaveformU8.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 896
if _libs["niHSDIO_64"].has("niHSDIO_FetchWaveformDirectDMA", "cdecl"):
    niHSDIO_FetchWaveformDirectDMA = _libs["niHSDIO_64"].get("niHSDIO_FetchWaveformDirectDMA", "cdecl")
    niHSDIO_FetchWaveformDirectDMA.argtypes = [ViSession, ViInt32, ViInt32, ViUInt32, POINTER(None), POINTER(struct_niHSDIO_wfmInfo), POINTER(ViUInt32)]
    niHSDIO_FetchWaveformDirectDMA.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 904
if _libs["niHSDIO_64"].has("niHSDIO_ReadWaveformU32", "cdecl"):
    niHSDIO_ReadWaveformU32 = _libs["niHSDIO_64"].get("niHSDIO_ReadWaveformU32", "cdecl")
    niHSDIO_ReadWaveformU32.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt32)]
    niHSDIO_ReadWaveformU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 910
if _libs["niHSDIO_64"].has("niHSDIO_ReadWaveformU16", "cdecl"):
    niHSDIO_ReadWaveformU16 = _libs["niHSDIO_64"].get("niHSDIO_ReadWaveformU16", "cdecl")
    niHSDIO_ReadWaveformU16.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt16)]
    niHSDIO_ReadWaveformU16.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 916
if _libs["niHSDIO_64"].has("niHSDIO_ReadWaveformU8", "cdecl"):
    niHSDIO_ReadWaveformU8 = _libs["niHSDIO_64"].get("niHSDIO_ReadWaveformU8", "cdecl")
    niHSDIO_ReadWaveformU8.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViUInt8)]
    niHSDIO_ReadWaveformU8.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 922
if _libs["niHSDIO_64"].has("niHSDIO_ReadMultiRecordU32", "cdecl"):
    niHSDIO_ReadMultiRecordU32 = _libs["niHSDIO_64"].get("niHSDIO_ReadMultiRecordU32", "cdecl")
    niHSDIO_ReadMultiRecordU32.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt32), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_ReadMultiRecordU32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 930
if _libs["niHSDIO_64"].has("niHSDIO_ReadMultiRecordU16", "cdecl"):
    niHSDIO_ReadMultiRecordU16 = _libs["niHSDIO_64"].get("niHSDIO_ReadMultiRecordU16", "cdecl")
    niHSDIO_ReadMultiRecordU16.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt16), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_ReadMultiRecordU16.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 938
if _libs["niHSDIO_64"].has("niHSDIO_ReadMultiRecordU8", "cdecl"):
    niHSDIO_ReadMultiRecordU8 = _libs["niHSDIO_64"].get("niHSDIO_ReadMultiRecordU8", "cdecl")
    niHSDIO_ReadMultiRecordU8.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32, POINTER(ViUInt8), POINTER(struct_niHSDIO_wfmInfo)]
    niHSDIO_ReadMultiRecordU8.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 946
if _libs["niHSDIO_64"].has("niHSDIO_HWC_FetchSampleErrors", "cdecl"):
    niHSDIO_HWC_FetchSampleErrors = _libs["niHSDIO_64"].get("niHSDIO_HWC_FetchSampleErrors", "cdecl")
    niHSDIO_HWC_FetchSampleErrors.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViReal64), POINTER(ViUInt32), POINTER(ViInt32), POINTER(ViUInt32), POINTER(ViUInt32)]
    niHSDIO_HWC_FetchSampleErrors.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 958
if _libs["niHSDIO_64"].has("niHSDIO_error_message", "cdecl"):
    niHSDIO_error_message = _libs["niHSDIO_64"].get("niHSDIO_error_message", "cdecl")
    niHSDIO_error_message.argtypes = [ViSession, ViStatus, ViChar * int(256)]
    niHSDIO_error_message.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 962
if _libs["niHSDIO_64"].has("niHSDIO_GetError", "cdecl"):
    niHSDIO_GetError = _libs["niHSDIO_64"].get("niHSDIO_GetError", "cdecl")
    niHSDIO_GetError.argtypes = [ViSession, POINTER(ViStatus), ViInt32, POINTER(ViChar)]
    niHSDIO_GetError.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 967
if _libs["niHSDIO_64"].has("niHSDIO_ClearError", "cdecl"):
    niHSDIO_ClearError = _libs["niHSDIO_64"].get("niHSDIO_ClearError", "cdecl")
    niHSDIO_ClearError.argtypes = [ViSession]
    niHSDIO_ClearError.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 971
if _libs["niHSDIO_64"].has("niHSDIO_reset", "cdecl"):
    niHSDIO_reset = _libs["niHSDIO_64"].get("niHSDIO_reset", "cdecl")
    niHSDIO_reset.argtypes = [ViSession]
    niHSDIO_reset.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 973
if _libs["niHSDIO_64"].has("niHSDIO_self_test", "cdecl"):
    niHSDIO_self_test = _libs["niHSDIO_64"].get("niHSDIO_self_test", "cdecl")
    niHSDIO_self_test.argtypes = [ViSession, POINTER(ViInt16), POINTER(ViChar)]
    niHSDIO_self_test.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 977
if _libs["niHSDIO_64"].has("niHSDIO_SelfCal", "cdecl"):
    niHSDIO_SelfCal = _libs["niHSDIO_64"].get("niHSDIO_SelfCal", "cdecl")
    niHSDIO_SelfCal.argtypes = [ViSession]
    niHSDIO_SelfCal.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 979
if _libs["niHSDIO_64"].has("niHSDIO_ResetDevice", "cdecl"):
    niHSDIO_ResetDevice = _libs["niHSDIO_64"].get("niHSDIO_ResetDevice", "cdecl")
    niHSDIO_ResetDevice.argtypes = [ViSession]
    niHSDIO_ResetDevice.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 984
if _libs["niHSDIO_64"].has("niHSDIO_GetAttributeViInt32", "cdecl"):
    niHSDIO_GetAttributeViInt32 = _libs["niHSDIO_64"].get("niHSDIO_GetAttributeViInt32", "cdecl")
    niHSDIO_GetAttributeViInt32.argtypes = [ViSession, ViConstString, ViAttr, POINTER(ViInt32)]
    niHSDIO_GetAttributeViInt32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 989
if _libs["niHSDIO_64"].has("niHSDIO_GetAttributeViReal64", "cdecl"):
    niHSDIO_GetAttributeViReal64 = _libs["niHSDIO_64"].get("niHSDIO_GetAttributeViReal64", "cdecl")
    niHSDIO_GetAttributeViReal64.argtypes = [ViSession, ViConstString, ViAttr, POINTER(ViReal64)]
    niHSDIO_GetAttributeViReal64.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 994
if _libs["niHSDIO_64"].has("niHSDIO_GetAttributeViString", "cdecl"):
    niHSDIO_GetAttributeViString = _libs["niHSDIO_64"].get("niHSDIO_GetAttributeViString", "cdecl")
    niHSDIO_GetAttributeViString.argtypes = [ViSession, ViConstString, ViAttr, ViInt32, POINTER(ViChar)]
    niHSDIO_GetAttributeViString.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1000
if _libs["niHSDIO_64"].has("niHSDIO_GetAttributeViSession", "cdecl"):
    niHSDIO_GetAttributeViSession = _libs["niHSDIO_64"].get("niHSDIO_GetAttributeViSession", "cdecl")
    niHSDIO_GetAttributeViSession.argtypes = [ViSession, ViConstString, ViAttr, POINTER(ViSession)]
    niHSDIO_GetAttributeViSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1005
if _libs["niHSDIO_64"].has("niHSDIO_GetAttributeViBoolean", "cdecl"):
    niHSDIO_GetAttributeViBoolean = _libs["niHSDIO_64"].get("niHSDIO_GetAttributeViBoolean", "cdecl")
    niHSDIO_GetAttributeViBoolean.argtypes = [ViSession, ViConstString, ViAttr, POINTER(ViBoolean)]
    niHSDIO_GetAttributeViBoolean.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1011
if _libs["niHSDIO_64"].has("niHSDIO_SetAttributeViInt32", "cdecl"):
    niHSDIO_SetAttributeViInt32 = _libs["niHSDIO_64"].get("niHSDIO_SetAttributeViInt32", "cdecl")
    niHSDIO_SetAttributeViInt32.argtypes = [ViSession, ViConstString, ViAttr, ViInt32]
    niHSDIO_SetAttributeViInt32.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1016
if _libs["niHSDIO_64"].has("niHSDIO_SetAttributeViReal64", "cdecl"):
    niHSDIO_SetAttributeViReal64 = _libs["niHSDIO_64"].get("niHSDIO_SetAttributeViReal64", "cdecl")
    niHSDIO_SetAttributeViReal64.argtypes = [ViSession, ViConstString, ViAttr, ViReal64]
    niHSDIO_SetAttributeViReal64.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1021
if _libs["niHSDIO_64"].has("niHSDIO_SetAttributeViString", "cdecl"):
    niHSDIO_SetAttributeViString = _libs["niHSDIO_64"].get("niHSDIO_SetAttributeViString", "cdecl")
    niHSDIO_SetAttributeViString.argtypes = [ViSession, ViConstString, ViAttr, ViConstString]
    niHSDIO_SetAttributeViString.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1026
if _libs["niHSDIO_64"].has("niHSDIO_SetAttributeViSession", "cdecl"):
    niHSDIO_SetAttributeViSession = _libs["niHSDIO_64"].get("niHSDIO_SetAttributeViSession", "cdecl")
    niHSDIO_SetAttributeViSession.argtypes = [ViSession, ViConstString, ViAttr, ViSession]
    niHSDIO_SetAttributeViSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1031
if _libs["niHSDIO_64"].has("niHSDIO_SetAttributeViBoolean", "cdecl"):
    niHSDIO_SetAttributeViBoolean = _libs["niHSDIO_64"].get("niHSDIO_SetAttributeViBoolean", "cdecl")
    niHSDIO_SetAttributeViBoolean.argtypes = [ViSession, ViConstString, ViAttr, ViBoolean]
    niHSDIO_SetAttributeViBoolean.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1038
if _libs["niHSDIO_64"].has("niHSDIO_ResetAttribute", "cdecl"):
    niHSDIO_ResetAttribute = _libs["niHSDIO_64"].get("niHSDIO_ResetAttribute", "cdecl")
    niHSDIO_ResetAttribute.argtypes = [ViSession, ViConstString, ViAttr]
    niHSDIO_ResetAttribute.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1044
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_SourceVoltage", "cdecl"):
    niHSDIO_STPMU_SourceVoltage = _libs["niHSDIO_64"].get("niHSDIO_STPMU_SourceVoltage", "cdecl")
    niHSDIO_STPMU_SourceVoltage.argtypes = [ViSession, ViConstString, ViReal64, ViInt32, ViReal64]
    niHSDIO_STPMU_SourceVoltage.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1050
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_SourceCurrent", "cdecl"):
    niHSDIO_STPMU_SourceCurrent = _libs["niHSDIO_64"].get("niHSDIO_STPMU_SourceCurrent", "cdecl")
    niHSDIO_STPMU_SourceCurrent.argtypes = [ViSession, ViConstString, ViReal64, ViReal64, ViReal64, ViReal64]
    niHSDIO_STPMU_SourceCurrent.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1057
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_DisablePMU", "cdecl"):
    niHSDIO_STPMU_DisablePMU = _libs["niHSDIO_64"].get("niHSDIO_STPMU_DisablePMU", "cdecl")
    niHSDIO_STPMU_DisablePMU.argtypes = [ViSession, ViConstString, ViInt32]
    niHSDIO_STPMU_DisablePMU.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1061
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_MeasureVoltage", "cdecl"):
    niHSDIO_STPMU_MeasureVoltage = _libs["niHSDIO_64"].get("niHSDIO_STPMU_MeasureVoltage", "cdecl")
    niHSDIO_STPMU_MeasureVoltage.argtypes = [ViSession, ViConstString, ViReal64, ViInt32, POINTER(ViReal64), POINTER(ViInt32)]
    niHSDIO_STPMU_MeasureVoltage.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1068
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_MeasureCurrent", "cdecl"):
    niHSDIO_STPMU_MeasureCurrent = _libs["niHSDIO_64"].get("niHSDIO_STPMU_MeasureCurrent", "cdecl")
    niHSDIO_STPMU_MeasureCurrent.argtypes = [ViSession, ViConstString, ViReal64, POINTER(ViReal64), POINTER(ViInt32)]
    niHSDIO_STPMU_MeasureCurrent.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1074
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_ExternalForceControl", "cdecl"):
    niHSDIO_STPMU_ExternalForceControl = _libs["niHSDIO_64"].get("niHSDIO_STPMU_ExternalForceControl", "cdecl")
    niHSDIO_STPMU_ExternalForceControl.argtypes = [ViSession, ViConstString, ViInt32, ViInt32]
    niHSDIO_STPMU_ExternalForceControl.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1079
if _libs["niHSDIO_64"].has("niHSDIO_STPMU_ExternalSenseControl", "cdecl"):
    niHSDIO_STPMU_ExternalSenseControl = _libs["niHSDIO_64"].get("niHSDIO_STPMU_ExternalSenseControl", "cdecl")
    niHSDIO_STPMU_ExternalSenseControl.argtypes = [ViSession, ViConstString, ViInt32, ViInt32]
    niHSDIO_STPMU_ExternalSenseControl.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1086
if _libs["niHSDIO_64"].has("niHSDIO_InitExtCal", "cdecl"):
    niHSDIO_InitExtCal = _libs["niHSDIO_64"].get("niHSDIO_InitExtCal", "cdecl")
    niHSDIO_InitExtCal.argtypes = [ViRsrc, ViConstString, POINTER(ViSession)]
    niHSDIO_InitExtCal.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1090
if _libs["niHSDIO_64"].has("niHSDIO_CalConfigureDeviceState", "cdecl"):
    niHSDIO_CalConfigureDeviceState = _libs["niHSDIO_64"].get("niHSDIO_CalConfigureDeviceState", "cdecl")
    niHSDIO_CalConfigureDeviceState.argtypes = [ViSession, ViInt32, ViUInt32, ViUInt32]
    niHSDIO_CalConfigureDeviceState.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1095
if _libs["niHSDIO_64"].has("niHSDIO_CalConfigureChannelState", "cdecl"):
    niHSDIO_CalConfigureChannelState = _libs["niHSDIO_64"].get("niHSDIO_CalConfigureChannelState", "cdecl")
    niHSDIO_CalConfigureChannelState.argtypes = [ViSession, ViConstString, ViUInt32, ViUInt32]
    niHSDIO_CalConfigureChannelState.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1100
if _libs["niHSDIO_64"].has("niHSDIO_CalAdjustViReal64", "cdecl"):
    niHSDIO_CalAdjustViReal64 = _libs["niHSDIO_64"].get("niHSDIO_CalAdjustViReal64", "cdecl")
    niHSDIO_CalAdjustViReal64.argtypes = [ViSession, ViConstString, ViUInt32, ViUInt32, ViReal64]
    niHSDIO_CalAdjustViReal64.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1106
if _libs["niHSDIO_64"].has("niHSDIO_CalAdjustViReal64Array", "cdecl"):
    niHSDIO_CalAdjustViReal64Array = _libs["niHSDIO_64"].get("niHSDIO_CalAdjustViReal64Array", "cdecl")
    niHSDIO_CalAdjustViReal64Array.argtypes = [ViSession, ViConstString, ViUInt32, ViUInt32, ViInt32, POINTER(ViReal64)]
    niHSDIO_CalAdjustViReal64Array.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1113
if _libs["niHSDIO_64"].has("niHSDIO_CalClearState", "cdecl"):
    niHSDIO_CalClearState = _libs["niHSDIO_64"].get("niHSDIO_CalClearState", "cdecl")
    niHSDIO_CalClearState.argtypes = [ViSession]
    niHSDIO_CalClearState.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1115
if _libs["niHSDIO_64"].has("niHSDIO_CalInitChildSession", "cdecl"):
    niHSDIO_CalInitChildSession = _libs["niHSDIO_64"].get("niHSDIO_CalInitChildSession", "cdecl")
    niHSDIO_CalInitChildSession.argtypes = [ViSession, ViUInt8, POINTER(ViSession)]
    niHSDIO_CalInitChildSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1119
if _libs["niHSDIO_64"].has("niHSDIO_CalCloseChildSession", "cdecl"):
    niHSDIO_CalCloseChildSession = _libs["niHSDIO_64"].get("niHSDIO_CalCloseChildSession", "cdecl")
    niHSDIO_CalCloseChildSession.argtypes = [ViSession, ViSession]
    niHSDIO_CalCloseChildSession.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1122
if _libs["niHSDIO_64"].has("niHSDIO_CalAdjustChannelVoltage", "cdecl"):
    niHSDIO_CalAdjustChannelVoltage = _libs["niHSDIO_64"].get("niHSDIO_CalAdjustChannelVoltage", "cdecl")
    niHSDIO_CalAdjustChannelVoltage.argtypes = [ViSession, ViConstString]
    niHSDIO_CalAdjustChannelVoltage.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1125
if _libs["niHSDIO_64"].has("niHSDIO_CalAdjustChannelSkew", "cdecl"):
    niHSDIO_CalAdjustChannelSkew = _libs["niHSDIO_64"].get("niHSDIO_CalAdjustChannelSkew", "cdecl")
    niHSDIO_CalAdjustChannelSkew.argtypes = [ViSession, ViConstString]
    niHSDIO_CalAdjustChannelSkew.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1128
if _libs["niHSDIO_64"].has("niHSDIO_CalAdjustTerminalSkew", "cdecl"):
    niHSDIO_CalAdjustTerminalSkew = _libs["niHSDIO_64"].get("niHSDIO_CalAdjustTerminalSkew", "cdecl")
    niHSDIO_CalAdjustTerminalSkew.argtypes = [ViSession, ViConstString]
    niHSDIO_CalAdjustTerminalSkew.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1131
if _libs["niHSDIO_64"].has("niHSDIO_GetSelfCalSupported", "cdecl"):
    niHSDIO_GetSelfCalSupported = _libs["niHSDIO_64"].get("niHSDIO_GetSelfCalSupported", "cdecl")
    niHSDIO_GetSelfCalSupported.argtypes = [ViSession, POINTER(ViBoolean)]
    niHSDIO_GetSelfCalSupported.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1134
if _libs["niHSDIO_64"].has("niHSDIO_GetSelfCalLastDateAndTime", "cdecl"):
    niHSDIO_GetSelfCalLastDateAndTime = _libs["niHSDIO_64"].get("niHSDIO_GetSelfCalLastDateAndTime", "cdecl")
    niHSDIO_GetSelfCalLastDateAndTime.argtypes = [ViSession, POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32)]
    niHSDIO_GetSelfCalLastDateAndTime.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1141
if _libs["niHSDIO_64"].has("niHSDIO_GetExtCalLastDateAndTime", "cdecl"):
    niHSDIO_GetExtCalLastDateAndTime = _libs["niHSDIO_64"].get("niHSDIO_GetExtCalLastDateAndTime", "cdecl")
    niHSDIO_GetExtCalLastDateAndTime.argtypes = [ViSession, POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32)]
    niHSDIO_GetExtCalLastDateAndTime.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1148
if _libs["niHSDIO_64"].has("niHSDIO_GetSelfCalLastTemp", "cdecl"):
    niHSDIO_GetSelfCalLastTemp = _libs["niHSDIO_64"].get("niHSDIO_GetSelfCalLastTemp", "cdecl")
    niHSDIO_GetSelfCalLastTemp.argtypes = [ViSession, POINTER(ViReal64)]
    niHSDIO_GetSelfCalLastTemp.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1151
if _libs["niHSDIO_64"].has("niHSDIO_GetExtCalLastTemp", "cdecl"):
    niHSDIO_GetExtCalLastTemp = _libs["niHSDIO_64"].get("niHSDIO_GetExtCalLastTemp", "cdecl")
    niHSDIO_GetExtCalLastTemp.argtypes = [ViSession, POINTER(ViReal64)]
    niHSDIO_GetExtCalLastTemp.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1154
if _libs["niHSDIO_64"].has("niHSDIO_ReadCurrentTemperature", "cdecl"):
    niHSDIO_ReadCurrentTemperature = _libs["niHSDIO_64"].get("niHSDIO_ReadCurrentTemperature", "cdecl")
    niHSDIO_ReadCurrentTemperature.argtypes = [ViSession, POINTER(ViReal64)]
    niHSDIO_ReadCurrentTemperature.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1157
if _libs["niHSDIO_64"].has("niHSDIO_GetExtCalRecommendedInterval", "cdecl"):
    niHSDIO_GetExtCalRecommendedInterval = _libs["niHSDIO_64"].get("niHSDIO_GetExtCalRecommendedInterval", "cdecl")
    niHSDIO_GetExtCalRecommendedInterval.argtypes = [ViSession, POINTER(ViInt32)]
    niHSDIO_GetExtCalRecommendedInterval.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1160
if _libs["niHSDIO_64"].has("niHSDIO_ChangeExtCalPassword", "cdecl"):
    niHSDIO_ChangeExtCalPassword = _libs["niHSDIO_64"].get("niHSDIO_ChangeExtCalPassword", "cdecl")
    niHSDIO_ChangeExtCalPassword.argtypes = [ViSession, ViConstString, ViConstString]
    niHSDIO_ChangeExtCalPassword.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1164
if _libs["niHSDIO_64"].has("niHSDIO_SetCalUserDefinedInfo", "cdecl"):
    niHSDIO_SetCalUserDefinedInfo = _libs["niHSDIO_64"].get("niHSDIO_SetCalUserDefinedInfo", "cdecl")
    niHSDIO_SetCalUserDefinedInfo.argtypes = [ViSession, ViConstString]
    niHSDIO_SetCalUserDefinedInfo.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1167
if _libs["niHSDIO_64"].has("niHSDIO_GetCalUserDefinedInfo", "cdecl"):
    niHSDIO_GetCalUserDefinedInfo = _libs["niHSDIO_64"].get("niHSDIO_GetCalUserDefinedInfo", "cdecl")
    niHSDIO_GetCalUserDefinedInfo.argtypes = [ViSession, ViString]
    niHSDIO_GetCalUserDefinedInfo.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1170
if _libs["niHSDIO_64"].has("niHSDIO_GetCalUserDefinedInfoMaxSize", "cdecl"):
    niHSDIO_GetCalUserDefinedInfoMaxSize = _libs["niHSDIO_64"].get("niHSDIO_GetCalUserDefinedInfoMaxSize", "cdecl")
    niHSDIO_GetCalUserDefinedInfoMaxSize.argtypes = [ViSession, POINTER(ViInt32)]
    niHSDIO_GetCalUserDefinedInfoMaxSize.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1173
if _libs["niHSDIO_64"].has("niHSDIO_CloseExtCal", "cdecl"):
    niHSDIO_CloseExtCal = _libs["niHSDIO_64"].get("niHSDIO_CloseExtCal", "cdecl")
    niHSDIO_CloseExtCal.argtypes = [ViSession, ViInt32]
    niHSDIO_CloseExtCal.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1176
if _libs["niHSDIO_64"].has("niHSDIO_RecordExtCalVerification", "cdecl"):
    niHSDIO_RecordExtCalVerification = _libs["niHSDIO_64"].get("niHSDIO_RecordExtCalVerification", "cdecl")
    niHSDIO_RecordExtCalVerification.argtypes = [ViSession, ViConstString]
    niHSDIO_RecordExtCalVerification.restype = ViStatus

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/IviVisaType.h: 56
try:
    _VI_ERROR = ((-2147483647) - 1)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 290
try:
    IVI_STATUS_CODE_BASE = 0x3FFA0000
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 292
try:
    IVI_WARN_BASE = IVI_STATUS_CODE_BASE
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 295
try:
    IVI_SPECIFIC_WARN_BASE = (IVI_WARN_BASE + 0x4000)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 299
try:
    IVI_ERROR_BASE = (_VI_ERROR + IVI_STATUS_CODE_BASE)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 302
try:
    IVI_SPECIFIC_ERROR_BASE = (IVI_ERROR_BASE + 0x4000)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 765
try:
    IVI_ATTR_BASE = 1000000
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 767
try:
    IVI_ENGINE_PUBLIC_ATTR_BASE = (IVI_ATTR_BASE + 50000)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 768
try:
    IVI_SPECIFIC_PUBLIC_ATTR_BASE = (IVI_ATTR_BASE + 150000)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include/ivi.h: 806
try:
    IVI_ATTR_LOGICAL_NAME = (IVI_ENGINE_PUBLIC_ATTR_BASE + 305)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 27
try:
    NIHSDIO_MAJOR_VERSION = 21
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 28
try:
    NIHSDIO_MINOR_VERSION = 5
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 30
try:
    NIHSDIO_SUPPORTED_INSTRUMENT_MODELS = 'NI-PXI-6541, NI-PXI-6542, NI-PCI-6541, NI-PCI-6542, NI-PXIe-6544, NI-PXIe-6545, NI-PXIe-6547, NI-PXIe-6548, NI-PXI-6551, NI-PXI-6552, NI-PCI-6551, NI-PCI-6552, NI-PXIe-6555, NI-PXIe-6556, NI-PXI-6561, NI-PXI-6562, NI-PCI-6561, NI-PCI-6562'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 31
try:
    NIHSDIO_DRIVER_VENDOR = 'National Instruments'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 32
try:
    NIHSDIO_DRIVER_DESCRIPTION = 'NI-HSDIO instrument driver'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 41
try:
    NIHSDIO_ATTR_LOGICAL_NAME = IVI_ATTR_LOGICAL_NAME
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 47
try:
    NIHSDIO_ATTR_DYNAMIC_CHANNELS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 2)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 48
try:
    NIHSDIO_ATTR_STATIC_CHANNELS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 3)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 51
try:
    NIHSDIO_ATTR_TOTAL_ACQUISITION_MEMORY_SIZE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 73)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 52
try:
    NIHSDIO_ATTR_TOTAL_GENERATION_MEMORY_SIZE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 74)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 53
try:
    NIHSDIO_ATTR_SERIAL_NUMBER = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 96)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 54
try:
    NIHSDIO_ATTR_PPMU_CAPABLE_IO_SWITCH_CONTROL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 180)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 55
try:
    NIHSDIO_ATTR_ATTRIBUTE_COMMITTAL_STRATEGY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 182)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 58
try:
    NIHSDIO_ATTR_DATA_VOLTAGE_LOW_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 6)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 59
try:
    NIHSDIO_ATTR_DATA_VOLTAGE_HIGH_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 7)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 60
try:
    NIHSDIO_ATTR_DATA_TERMINATION_VOLTAGE_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 161)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 61
try:
    NIHSDIO_ATTR_DATA_VOLTAGE_RANGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 163)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 62
try:
    NIHSDIO_ATTR_TRIGGER_VOLTAGE_LOW_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 8)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 63
try:
    NIHSDIO_ATTR_TRIGGER_VOLTAGE_HIGH_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 9)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 64
try:
    NIHSDIO_ATTR_EVENT_VOLTAGE_LOW_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 79)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 65
try:
    NIHSDIO_ATTR_EVENT_VOLTAGE_HIGH_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 80)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 68
try:
    NIHSDIO_ATTR_DATA_INTERPRETATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 10)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 69
try:
    NIHSDIO_ATTR_INPUT_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 70)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 70
try:
    NIHSDIO_ATTR_DRIVE_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 139)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 71
try:
    NIHSDIO_ATTR_DATA_TRISTATE_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 160)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 72
try:
    NIHSDIO_ATTR_DATA_TERMINATION_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 175)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 74
try:
    NIHSDIO_ATTR_ACTIVE_LOAD_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 176)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 75
try:
    NIHSDIO_ATTR_ACTIVE_LOAD_SOURCING_CURRENT_VALUE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 177)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 76
try:
    NIHSDIO_ATTR_ACTIVE_LOAD_SINKING_CURRENT_VALUE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 178)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 77
try:
    NIHSDIO_ATTR_ACTIVE_LOAD_COMMUTATING_VOLTAGE_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 179)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 80
try:
    NIHSDIO_ATTR_REF_CLOCK_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 11)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 81
try:
    NIHSDIO_ATTR_REF_CLOCK_RATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 12)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 82
try:
    NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 58)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 83
try:
    NIHSDIO_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 59)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 84
try:
    NIHSDIO_ATTR_SAMPLE_CLOCK_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 13)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 85
try:
    NIHSDIO_ATTR_SAMPLE_CLOCK_RATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 14)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 86
try:
    NIHSDIO_ATTR_SAMPLE_CLOCK_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 60)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 87
try:
    NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 61)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 88
try:
    NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_DELAY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 62)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 89
try:
    NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 63)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 90
try:
    NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_OFFSET = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 83)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 91
try:
    NIHSDIO_ATTR_EXPORTED_ONBOARD_REF_CLOCK_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 85)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 94
try:
    NIHSDIO_ATTR_START_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 32)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 95
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 33)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 96
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 34)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 97
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 98
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 75)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 99
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 98)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 100
try:
    NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_PATTERN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 35)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 101
try:
    NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 36)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 102
try:
    NIHSDIO_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 37)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 103
try:
    NIHSDIO_ATTR_EXPORTED_START_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 118)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 105
try:
    NIHSDIO_ATTR_REF_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 38)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 106
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 39)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 107
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 40)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 108
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 4)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 109
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 77)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 110
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 99)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 111
try:
    NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_PATTERN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 41)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 112
try:
    NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 42)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 113
try:
    NIHSDIO_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 43)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 114
try:
    NIHSDIO_ATTR_EXPORTED_REF_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 119)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 115
try:
    NIHSDIO_ATTR_START_TO_REF_TRIGGER_HOLDOFF = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 86)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 116
try:
    NIHSDIO_ATTR_REF_TO_REF_TRIGGER_HOLDOFF = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 129)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 118
try:
    NIHSDIO_ATTR_SCRIPT_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 44)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 119
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 45)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 120
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 46)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 121
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 5)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 122
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 100)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 123
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 47)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 124
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 48)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 125
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 105)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 126
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 106)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 127
try:
    NIHSDIO_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 49)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 128
try:
    NIHSDIO_ATTR_EXPORTED_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 120)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 130
try:
    NIHSDIO_ATTR_PAUSE_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 50)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 131
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 51)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 132
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 52)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 133
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 15)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 134
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 87)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 135
try:
    NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 101)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 136
try:
    NIHSDIO_ATTR_PATTERN_MATCH_PAUSE_TRIGGER_PATTERN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 53)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 137
try:
    NIHSDIO_ATTR_PATTERN_MATCH_PAUSE_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 54)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 138
try:
    NIHSDIO_ATTR_EXPORTED_PAUSE_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 55)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 139
try:
    NIHSDIO_ATTR_EXPORTED_PAUSE_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 121)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 141
try:
    NIHSDIO_ATTR_ADVANCE_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 88)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 142
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 89)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 143
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_EDGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 90)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 144
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 95)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 145
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 93)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 146
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 107)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 147
try:
    NIHSDIO_ATTR_PATTERN_MATCH_ADVANCE_TRIGGER_PATTERN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 91)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 148
try:
    NIHSDIO_ATTR_PATTERN_MATCH_ADVANCE_TRIGGER_WHEN = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 92)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 149
try:
    NIHSDIO_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 94)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 150
try:
    NIHSDIO_ATTR_EXPORTED_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 122)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 152
try:
    NIHSDIO_ATTR_STOP_TRIGGER_TYPE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 152)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 153
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_SOURCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 153)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 154
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_EDGE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 154)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 155
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 155)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 156
try:
    NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_IMPEDANCE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 156)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 157
try:
    NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 157)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 158
try:
    NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 158)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 161
try:
    NIHSDIO_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 16)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 162
try:
    NIHSDIO_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 17)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 163
try:
    NIHSDIO_ATTR_READY_FOR_START_EVENT_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 102)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 165
try:
    NIHSDIO_ATTR_DATA_ACTIVE_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 19)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 166
try:
    NIHSDIO_ATTR_DATA_ACTIVE_EVENT_LEVEL_ACTIVE_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 20)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 167
try:
    NIHSDIO_ATTR_DATA_ACTIVE_EVENT_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 81)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 168
try:
    NIHSDIO_ATTR_DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 103)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 170
try:
    NIHSDIO_ATTR_MARKER_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 22)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 171
try:
    NIHSDIO_ATTR_MARKER_EVENT_PULSE_POLARITY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 23)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 172
try:
    NIHSDIO_ATTR_MARKER_EVENT_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 82)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 173
try:
    NIHSDIO_ATTR_MARKER_EVENT_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 104)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 175
try:
    NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 109)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 176
try:
    NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_LEVEL_ACTIVE_LEVEL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 110)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 177
try:
    NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 111)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 179
try:
    NIHSDIO_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 112)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 180
try:
    NIHSDIO_ATTR_END_OF_RECORD_EVENT_PULSE_POLARITY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 113)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 181
try:
    NIHSDIO_ATTR_END_OF_RECORD_EVENT_TERMINAL_CONFIGURATION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 114)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 183
try:
    NIHSDIO_ATTR_HWC_SAMPLE_ERROR_EVENT_OUTPUT_TERMINAL = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 136)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 186
try:
    NIHSDIO_ATTR_GENERATION_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 25)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 187
try:
    NIHSDIO_ATTR_REPEAT_MODE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 26)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 188
try:
    NIHSDIO_ATTR_REPEAT_COUNT = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 71)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 189
try:
    NIHSDIO_ATTR_WAVEFORM_TO_GENERATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 27)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 190
try:
    NIHSDIO_ATTR_SCRIPT_TO_GENERATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 28)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 191
try:
    NIHSDIO_ATTR_INITIAL_STATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 64)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 192
try:
    NIHSDIO_ATTR_IDLE_STATE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 65)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 193
try:
    NIHSDIO_ATTR_DATA_TRANSFER_BLOCK_SIZE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 144)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 196
try:
    NIHSDIO_ATTR_SAMPLES_PER_RECORD = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 29)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 197
try:
    NIHSDIO_ATTR_NUM_RECORDS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 126)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 198
try:
    NIHSDIO_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 30)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 199
try:
    NIHSDIO_ATTR_FETCH_BACKLOG = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 31)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 200
try:
    NIHSDIO_ATTR_FETCH_RELATIVE_TO = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 67)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 201
try:
    NIHSDIO_ATTR_FETCH_OFFSET = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 68)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 202
try:
    NIHSDIO_ATTR_RECORDS_DONE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 125)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 203
try:
    NIHSDIO_ATTR_DATA_ACTIVE_INTERNAL_ROUTE_DELAY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 138)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 204
try:
    NIHSDIO_ATTR_SAMPLES_PER_RECORD_IS_FINITE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 159)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 207
try:
    NIHSDIO_ATTR_DATA_POSITION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 56)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 208
try:
    NIHSDIO_ATTR_DATA_POSITION_DELAY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 57)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 209
try:
    NIHSDIO_ATTR_DATA_DESKEW = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 162)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 210
try:
    NIHSDIO_ATTR_TRIGGER_POSITION_DELAY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 164)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 211
try:
    NIHSDIO_ATTR_TRIGGER_DESKEW = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 165)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 212
try:
    NIHSDIO_ATTR_EVENT_POSITION_DELAY = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 166)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 213
try:
    NIHSDIO_ATTR_EVENT_DESKEW = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 167)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 216
try:
    NIHSDIO_ATTR_DATA_WIDTH = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 108)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 219
try:
    NIHSDIO_ATTR_DATA_RATE_MULTIPLIER = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 128)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 222
try:
    NIHSDIO_ATTR_SUPPORTED_DATA_STATES = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 130)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 225
try:
    NIHSDIO_ATTR_OSCILLATOR_PHASE_DAC_VALUE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 72)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 228
try:
    NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BACKLOG = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 132)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 229
try:
    NIHSDIO_ATTR_HWC_NUM_SAMPLE_ERRORS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 133)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 230
try:
    NIHSDIO_ATTR_HWC_SAMPLES_COMPARED = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 134)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 231
try:
    NIHSDIO_ATTR_HWC_CUMULATIVE_ERROR_BITS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 181)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 232
try:
    NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 140)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 233
try:
    NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BUFFER_OVERFLOWED = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 135)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 236
try:
    NIHSDIO_ATTR_SPACE_AVAILABLE_IN_STREAMING_WAVEFORM = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 141)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 237
try:
    NIHSDIO_ATTR_STREAMING_WAVEFORM_NAME = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 142)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 238
try:
    NIHSDIO_ATTR_STREAMING_ENABLED = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 143)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 241
try:
    NIHSDIO_ATTR_DIRECT_DMA_ENABLED = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 146)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 242
try:
    NIHSDIO_ATTR_DIRECT_DMA_WINDOW_SIZE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 147)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 243
try:
    NIHSDIO_ATTR_DIRECT_DMA_WINDOW_ADDRESS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 148)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 246
try:
    NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 149)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 247
try:
    NIHSDIO_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 150)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 248
try:
    NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 151)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 251
try:
    NIHSDIO_ATTR_DEVICE_POWER_CONSUMPTION = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 170)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 252
try:
    NIHSDIO_ATTR_DEVICE_PEAK_POWER_CONSUMED = (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 171)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 261
try:
    NIHSDIO_VAL_HIGH_OR_LOW = 3
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 262
try:
    NIHSDIO_VAL_VALID_OR_INVALID = 4
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 265
try:
    NIHSDIO_VAL_ACTIVE_DRIVE = 75
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 266
try:
    NIHSDIO_VAL_OPEN_COLLECTOR = 76
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 269
try:
    NIHSDIO_VAL_5_0V_LOGIC = 5
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 270
try:
    NIHSDIO_VAL_3_3V_LOGIC = 6
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 271
try:
    NIHSDIO_VAL_2_5V_LOGIC = 7
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 272
try:
    NIHSDIO_VAL_1_8V_LOGIC = 8
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 273
try:
    NIHSDIO_VAL_1_5V_LOGIC = 80
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 274
try:
    NIHSDIO_VAL_1_2V_LOGIC = 81
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 277
try:
    NIHSDIO_VAL_MINUS_2_TO_6_VOLTAGE_RANGE = 86
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 278
try:
    NIHSDIO_VAL_MINUS_1_TO_7_VOLTAGE_RANGE = 87
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 281
try:
    NIHSDIO_VAL_HIGH_IMPEDANCE = 84
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 282
try:
    NIHSDIO_VAL_DRIVE_TERMINATION_VOLTAGE = 85
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 285
try:
    NIHSDIO_VAL_RISING_EDGE = 12
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 286
try:
    NIHSDIO_VAL_FALLING_EDGE = 13
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 289
try:
    NIHSDIO_VAL_IGNORE = 33
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 290
try:
    NIHSDIO_VAL_MATCH_LOW = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 291
try:
    NIHSDIO_VAL_MATCH_HIGH = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 294
try:
    NIHSDIO_VAL_PATTERN_MATCHES = 36
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 295
try:
    NIHSDIO_VAL_PATTERN_DOES_NOT_MATCH = 37
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 298
try:
    NIHSDIO_VAL_ACTIVE_HIGH = 10
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 299
try:
    NIHSDIO_VAL_ACTIVE_LOW = 11
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 302
try:
    NIHSDIO_VAL_WAVEFORM = 14
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 303
try:
    NIHSDIO_VAL_SCRIPTED = 15
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 306
try:
    NIHSDIO_VAL_FINITE = 16
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 307
try:
    NIHSDIO_VAL_CONTINUOUS = 17
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 310
try:
    NIHSDIO_VAL_SAMPLE_CLOCK_RISING_EDGE = 18
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 311
try:
    NIHSDIO_VAL_SAMPLE_CLOCK_FALLING_EDGE = 19
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 312
try:
    NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE = 20
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 315
try:
    NIHSDIO_VAL_NONINVERTED = 21
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 316
try:
    NIHSDIO_VAL_INVERTED = 22
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 317
try:
    NIHSDIO_VAL_DELAYED = 23
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 320
try:
    NIHSDIO_VAL_TRISTATE = 24
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 321
try:
    NIHSDIO_VAL_LOGIC_HIGH = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 322
try:
    NIHSDIO_VAL_LOGIC_LOW = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 323
try:
    NIHSDIO_VAL_HOLD_LAST_VALUE = 27
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 326
try:
    NIHSDIO_VAL_NONE = 28
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 327
try:
    NIHSDIO_VAL_DIGITAL_EDGE = 29
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 328
try:
    NIHSDIO_VAL_DIGITAL_LEVEL = 30
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 329
try:
    NIHSDIO_VAL_PATTERN_MATCH = 31
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 330
try:
    NIHSDIO_VAL_SOFTWARE = 32
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 333
try:
    NIHSDIO_VAL_HIGH = 34
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 334
try:
    NIHSDIO_VAL_LOW = 35
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 337
try:
    NIHSDIO_VAL_START_OF_WAVEFORM = 44
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 338
try:
    NIHSDIO_VAL_CURRENT_POSITION = 45
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 341
try:
    NIHSDIO_VAL_MOST_RECENT_SAMPLE = 46
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 342
try:
    NIHSDIO_VAL_FIRST_SAMPLE = 47
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 343
try:
    NIHSDIO_VAL_REFERENCE_TRIGGER = 48
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 344
try:
    NIHSDIO_VAL_FIRST_PRETRIGGER_SAMPLE = 49
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 345
try:
    NIHSDIO_VAL_CURRENT_READ_POSITION = 50
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 348
try:
    NIHSDIO_VAL_SAMPLE_CLOCK = 51
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 349
try:
    NIHSDIO_VAL_REF_CLOCK = 52
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 350
try:
    NIHSDIO_VAL_START_TRIGGER = 53
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 351
try:
    NIHSDIO_VAL_REF_TRIGGER = 54
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 352
try:
    NIHSDIO_VAL_DATA_ACTIVE_EVENT = 55
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 353
try:
    NIHSDIO_VAL_READY_FOR_START_EVENT = 56
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 354
try:
    NIHSDIO_VAL_READY_FOR_ADVANCE_EVENT = 66
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 355
try:
    NIHSDIO_VAL_END_OF_RECORD_EVENT = 68
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 356
try:
    NIHSDIO_VAL_PAUSE_TRIGGER = 57
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 357
try:
    NIHSDIO_VAL_SCRIPT_TRIGGER = 58
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 358
try:
    NIHSDIO_VAL_MARKER_EVENT = 59
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 359
try:
    NIHSDIO_VAL_ONBOARD_REF_CLOCK = 60
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 360
try:
    NIHSDIO_VAL_ADVANCE_TRIGGER = 61
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 361
try:
    NIHSDIO_VAL_STOP_TRIGGER = 82
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 364
try:
    NIHSDIO_VAL_TIMESTAMP_ABSOLUTE = 69
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 365
try:
    NIHSDIO_VAL_TIMESTAMP_RELATIVE = 70
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 368
try:
    NIHSDIO_VAL_EXT_CAL_COMMIT = 62
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 369
try:
    NIHSDIO_VAL_EXT_CAL_CANCEL = 63
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 372
try:
    NIHSDIO_VAL_LVDS = 64
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 373
try:
    NIHSDIO_VAL_SINGLE_ENDED = 65
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 376
try:
    NIHSDIO_VAL_SINGLE_DATA_RATE = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 377
try:
    NIHSDIO_VAL_DOUBLE_DATA_RATE = 2
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 380
try:
    NIHSDIO_VAL_GROUP_BY_SAMPLE = 71
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 381
try:
    NIHSDIO_VAL_GROUP_BY_CHANNEL = 72
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 384
try:
    NIHSDIO_VAL_STATES_0_1 = 77
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 385
try:
    NIHSDIO_VAL_STATES_0_1_Z = 83
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 386
try:
    NIHSDIO_VAL_STATES_0_1_Z_L_H_X = 78
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 387
try:
    NIHSDIO_VAL_STATES_L_H_X = 79
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 391
try:
    NIHSDIO_VAL_STPMU_LOCAL_SENSE = 88
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 392
try:
    NIHSDIO_VAL_STPMU_REMOTE_SENSE = 89
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 395
try:
    NIHSDIO_VAL_STPMU_RETURN_TO_TRISTATE = 90
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 396
try:
    NIHSDIO_VAL_STPMU_RETURN_TO_PREVIOUS = 91
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 399
try:
    NIHSDIO_VAL_STPMU_CONNECT_EXTERNAL = 92
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 400
try:
    NIHSDIO_VAL_STPMU_DISCONNECT_EXTERNAL = 93
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 403
try:
    NIHSDIO_VAL_STPMU_AUX_IO_CONNECTOR = 94
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 404
try:
    NIHSDIO_VAL_STPMU_REMOTE_SENSE_CONNECTOR = 95
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 408
try:
    NIHSDIO_VAL_ACTIVE_LOAD_DISABLED = 96
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 409
try:
    NIHSDIO_VAL_ACTIVE_LOAD_ENABLED_WHEN_TRISTATE = 97
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 412
try:
    NIHSDIO_VAL_CONNECT = 98
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 413
try:
    NIHSDIO_VAL_DISCONNECT = 99
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 416
try:
    NIHSDIO_VAL_CALIBRATION_CHILD_SESSION_TYPE_ACQUISITION = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 417
try:
    NIHSDIO_VAL_CALIBRATION_CHILD_SESSION_TYPE_GENERATION = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 420
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_UNCONFIGURED = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 421
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_VOLTAGE_REFERENCE_ADJUST = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 422
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_SOURCE_RESISTOR_ADJUST = 2
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 423
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_SINK_RESISTOR_ADJUST = 3
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 424
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_CALIBRATION_PULSE_ADJUST = 4
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 425
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_INPUT_CHANNEL_SKEW_ACCURACY_VERIFY = 5
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 426
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_OUTPUT_CHANNEL_SKEW_ACCURACY_VERIFY = 6
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 427
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_INPUT_VOLTAGE_ACCURACY_VERIFY = 7
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 428
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_OUTPUT_VOLTAGE_ACCURACY_VERIFY = 8
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 429
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_INPUT_CHANNEL_SKEW_ADJUST = 9
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 430
try:
    NIHSDIO_VAL_CALIBRATION_TYPE_OUTPUT_CHANNEL_SKEW_ADJUST = 10
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 433
try:
    NIHSDIO_VAL_DEFERRED_UNTIL_COMMIT = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 434
try:
    NIHSDIO_VAL_IMMEDIATELY_UPON_SET_VOLTAGE = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 437
try:
    NIHSDIO_VAL_DO_NOT_EXPORT_STR = ''
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 438
try:
    NIHSDIO_VAL_PFI0_STR = 'PFI0'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 439
try:
    NIHSDIO_VAL_PFI1_STR = 'PFI1'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 440
try:
    NIHSDIO_VAL_PFI2_STR = 'PFI2'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 441
try:
    NIHSDIO_VAL_PFI3_STR = 'PFI3'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 442
try:
    NIHSDIO_VAL_PFI4_STR = 'PFI4'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 443
try:
    NIHSDIO_VAL_PFI5_STR = 'PFI5'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 444
try:
    NIHSDIO_VAL_PFI24_STR = 'PFI24'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 445
try:
    NIHSDIO_VAL_PFI25_STR = 'PFI25'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 446
try:
    NIHSDIO_VAL_PFI26_STR = 'PFI26'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 447
try:
    NIHSDIO_VAL_PFI27_STR = 'PFI27'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 448
try:
    NIHSDIO_VAL_PFI28_STR = 'PFI28'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 449
try:
    NIHSDIO_VAL_PFI29_STR = 'PFI29'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 450
try:
    NIHSDIO_VAL_PFI30_STR = 'PFI30'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 451
try:
    NIHSDIO_VAL_PFI31_STR = 'PFI31'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 452
try:
    NIHSDIO_VAL_PXI_TRIG0_STR = 'PXI_Trig0'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 453
try:
    NIHSDIO_VAL_PXI_TRIG1_STR = 'PXI_Trig1'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 454
try:
    NIHSDIO_VAL_PXI_TRIG2_STR = 'PXI_Trig2'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 455
try:
    NIHSDIO_VAL_PXI_TRIG3_STR = 'PXI_Trig3'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 456
try:
    NIHSDIO_VAL_PXI_TRIG4_STR = 'PXI_Trig4'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 457
try:
    NIHSDIO_VAL_PXI_TRIG5_STR = 'PXI_Trig5'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 458
try:
    NIHSDIO_VAL_PXI_TRIG6_STR = 'PXI_Trig6'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 459
try:
    NIHSDIO_VAL_PXI_TRIG7_STR = 'PXI_Trig7'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 460
try:
    NIHSDIO_VAL_PXI_STAR_STR = 'PXI_STAR'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 461
try:
    NIHSDIO_VAL_CLK_OUT_STR = 'ClkOut'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 462
try:
    NIHSDIO_VAL_DDC_CLK_OUT_STR = 'DDC_ClkOut'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 463
try:
    NIHSDIO_VAL_ON_BOARD_CLOCK_STR = 'OnBoardClock'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 464
try:
    NIHSDIO_VAL_CLK_IN_STR = 'ClkIn'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 465
try:
    NIHSDIO_VAL_PXI_CLK_STR = 'PXI_CLK'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 466
try:
    NIHSDIO_VAL_STROBE_STR = 'STROBE'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 467
try:
    NIHSDIO_VAL_PXIE_DSTARA_STR = 'PXIe-DStarA'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 468
try:
    NIHSDIO_VAL_NONE_STR = 'None'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 469
try:
    NIHSDIO_VAL_RTSI0_STR = 'RTSI0'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 470
try:
    NIHSDIO_VAL_RTSI1_STR = 'RTSI1'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 471
try:
    NIHSDIO_VAL_RTSI2_STR = 'RTSI2'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 472
try:
    NIHSDIO_VAL_RTSI3_STR = 'RTSI3'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 473
try:
    NIHSDIO_VAL_RTSI4_STR = 'RTSI4'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 474
try:
    NIHSDIO_VAL_RTSI5_STR = 'RTSI5'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 475
try:
    NIHSDIO_VAL_RTSI6_STR = 'RTSI6'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 476
try:
    NIHSDIO_VAL_RTSI7_STR = 'RTSI7'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 479
try:
    NIHSDIO_VAL_SCRIPT_TRIGGER0 = 'scriptTrigger0'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 480
try:
    NIHSDIO_VAL_SCRIPT_TRIGGER1 = 'scriptTrigger1'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 481
try:
    NIHSDIO_VAL_SCRIPT_TRIGGER2 = 'scriptTrigger2'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 482
try:
    NIHSDIO_VAL_SCRIPT_TRIGGER3 = 'scriptTrigger3'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 483
try:
    NIHSDIO_VAL_MARKER_EVENT0 = 'marker0'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 484
try:
    NIHSDIO_VAL_MARKER_EVENT1 = 'marker1'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 485
try:
    NIHSDIO_VAL_MARKER_EVENT2 = 'marker2'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 486
try:
    NIHSDIO_VAL_MARKER_EVENT3 = 'marker3'
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 490
try:
    NI_DIO_0 = 0
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 491
try:
    NI_DIO_1 = 1
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 492
try:
    NI_DIO_Z = 2
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 493
try:
    NI_DIO_L = 3
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 494
try:
    NI_DIO_H = 4
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 495
try:
    NI_DIO_X = 5
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 496
try:
    NI_DIO_T = 6
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 497
try:
    NI_DIO_V = 7
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1185
try:
    NIHSDIO_ERROR_INVALID_RESOURCE_DESCRIPTOR = (IVI_SPECIFIC_ERROR_BASE + 44)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1186
try:
    NIHSDIO_ERROR_INVALID_CHANNEL_STRING_SYNTAX = (IVI_SPECIFIC_ERROR_BASE + 2)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1187
try:
    NIHSDIO_ERROR_NO_DYNAMIC_LINES_ENABLED = (IVI_SPECIFIC_ERROR_BASE + 4)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1188
try:
    NIHSDIO_ERROR_SESSION_IN_RUNNING_STATE = (IVI_SPECIFIC_ERROR_BASE + 5)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1189
try:
    NIHSDIO_ERROR_ONLY_ONE_IDENTIFIER_ALLOWED = (IVI_SPECIFIC_ERROR_BASE + 6)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1190
try:
    NIHSDIO_ERROR_INVALID_LINE_STATE = (IVI_SPECIFIC_ERROR_BASE + 7)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1191
try:
    NIHSDIO_ERROR_MAX_TIME_EXCEEDED = (IVI_SPECIFIC_ERROR_BASE + 8)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1192
try:
    NIHSDIO_ERROR_INCORRECT_DIGITAL_PATTERN = (IVI_SPECIFIC_ERROR_BASE + 9)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1193
try:
    NIHSDIO_ERROR_WAVEFORM_NOT_IN_MEMORY = (IVI_SPECIFIC_ERROR_BASE + 12)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1194
try:
    NIHSDIO_ERROR_WAVEFORM_EMPTY = (IVI_SPECIFIC_ERROR_BASE + 62)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1195
try:
    NIHSDIO_ERROR_SCRIPT_NOT_IN_MEMORY = (IVI_SPECIFIC_ERROR_BASE + 3)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1196
try:
    NIHSDIO_ERROR_DIGITAL_WAVEFORM_EXPECTED = (IVI_SPECIFIC_ERROR_BASE + 13)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1197
try:
    NIHSDIO_ERROR_SCALED_DATA_WIDTH_FAILED = (IVI_SPECIFIC_ERROR_BASE + 14)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1198
try:
    NIHSDIO_ERROR_INVALID_REPEAT_COUNT = (IVI_SPECIFIC_ERROR_BASE + 16)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1199
try:
    NIHSDIO_ERROR_SET_WHEN_SESSION_RUNNING = (IVI_SPECIFIC_ERROR_BASE + 39)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1200
try:
    NIHSDIO_ERROR_GET_WHEN_SESSION_NOT_RUNNING = (IVI_SPECIFIC_ERROR_BASE + 45)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1201
try:
    NIHSDIO_ERROR_SESSION_NOT_IN_RUNNING_STATE = (IVI_SPECIFIC_ERROR_BASE + 17)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1202
try:
    NIHSDIO_ERROR_NO_WFMS_IN_MEM = (IVI_SPECIFIC_ERROR_BASE + 18)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1203
try:
    NIHSDIO_ERROR_ACTIVE_WFM_NOT_SPECIFIED = (IVI_SPECIFIC_ERROR_BASE + 19)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1204
try:
    NIHSDIO_ERROR_RESOURCE_ALREADY_RESERVED = (IVI_SPECIFIC_ERROR_BASE + 20)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1205
try:
    NIHSDIO_ERROR_ROUTING_HARDWARE_BUSY = (IVI_SPECIFIC_ERROR_BASE + 21)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1206
try:
    NIHSDIO_ERROR_SAMPS_PER_REC_TOO_BIG = (IVI_SPECIFIC_ERROR_BASE + 22)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1207
try:
    NIHSDIO_ERROR_NO_SCRIPTS_IN_MEMORY = (IVI_SPECIFIC_ERROR_BASE + 23)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1208
try:
    NIHSDIO_ERROR_ACTIVE_SCRIPT_NOT_SPECIFIED = (IVI_SPECIFIC_ERROR_BASE + 24)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1209
try:
    NIHSDIO_ERROR_INSTRUMENT_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 25)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1210
try:
    NIHSDIO_ERROR_DUPLICATE_CHANNEL_NAME = (IVI_SPECIFIC_ERROR_BASE + 26)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1211
try:
    NIHSDIO_ERROR_ACQUISITION_SESSION_ALREADY_OPEN = (IVI_SPECIFIC_ERROR_BASE + 27)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1212
try:
    NIHSDIO_ERROR_GENERATION_SESSION_ALREADY_OPEN = (IVI_SPECIFIC_ERROR_BASE + 28)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1213
try:
    NIHSDIO_ERROR_CHANNEL_NOT_PREV_TRISTATED = (IVI_SPECIFIC_ERROR_BASE + 29)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1214
try:
    NIHSDIO_ERROR_CHANNEL_RESERVED_FOR_GENERATION = (IVI_SPECIFIC_ERROR_BASE + 31)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1215
try:
    NIHSDIO_ERROR_SAMPLES_NOT_YET_AVAILABLE = (IVI_SPECIFIC_ERROR_BASE + 32)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1216
try:
    NIHSDIO_ERROR_INVALID_START_WRITE_ADDRESS = (IVI_SPECIFIC_ERROR_BASE + 33)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1217
try:
    NIHSDIO_ERROR_WAVEFORM_PREVIOUSLY_ALLOCATED = (IVI_SPECIFIC_ERROR_BASE + 35)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1218
try:
    NIHSDIO_ERROR_ROUTE_RESOURCES_IN_USE_IN_SESSION = (IVI_SPECIFIC_ERROR_BASE + 36)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1219
try:
    NIHSDIO_ERROR_INVALID_WAVEFORM_NAME = (IVI_SPECIFIC_ERROR_BASE + 38)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1220
try:
    NIHSDIO_ERROR_INVALID_GENERATION_CLOCK_SOURCE = (IVI_SPECIFIC_ERROR_BASE + 41)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1221
try:
    NIHSDIO_ERROR_RUNTIME_ABORTED = (IVI_SPECIFIC_ERROR_BASE + 47)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1222
try:
    NIHSDIO_ERROR_DEVICE_ABSENT_OR_UNAVAILABLE = (IVI_SPECIFIC_ERROR_BASE + 50)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1223
try:
    NIHSDIO_ERROR_INVALID_SIGNAL_IDENTIFIER = (IVI_SPECIFIC_ERROR_BASE + 52)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1224
try:
    NIHSDIO_ERROR_UNSUPPORTED_SOFTWARE_TRIGGER_TYPE = (IVI_SPECIFIC_ERROR_BASE + 53)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1225
try:
    NIHSDIO_ERROR_UNSUPPORTED_EXPORT_SIGNAL_TYPE = (IVI_SPECIFIC_ERROR_BASE + 54)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1226
try:
    NIHSDIO_ERROR_UNKNOWN_CHANNEL_NAME = (IVI_SPECIFIC_ERROR_BASE + 15)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1227
try:
    NIHSDIO_ERROR_ATTRIBUTE_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 30)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1228
try:
    NIHSDIO_ERROR_INTERNAL_SOFTWARE_ERROR = (IVI_SPECIFIC_ERROR_BASE + 1)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1229
try:
    NIHSDIO_ERROR_REFERENCE_PAUSE_TRIGGER_CONFLICT = (IVI_SPECIFIC_ERROR_BASE + 37)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1230
try:
    NIHSDIO_ERROR_CALIBRATION_SESSION_ALREADY_OPEN = (IVI_SPECIFIC_ERROR_BASE + 58)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1231
try:
    NIHSDIO_ERROR_FILE_SIGNAL_AND_CHANNEL_MISMATCH = (IVI_SPECIFIC_ERROR_BASE + 59)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1232
try:
    NIHSDIO_ERROR_VOLTAGE_CALIBRATION_FAILED = (IVI_SPECIFIC_ERROR_BASE + 60)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1233
try:
    NIHSDIO_ERROR_CALIBRATION_FUNCTION_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 61)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1234
try:
    NIHSDIO_ERROR_DELAY_VALUE_INVALID_FOR_FREQUENCY = (IVI_SPECIFIC_ERROR_BASE + 63)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1235
try:
    NIHSDIO_ERROR_READ_WRITE_FUNCTION_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 64)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1236
try:
    NIHSDIO_ERROR_INVALID_DATA_WIDTH = (IVI_SPECIFIC_ERROR_BASE + 65)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1237
try:
    NIHSDIO_ERROR_INVALID_CHANNEL_FOR_DATA_WIDTH = (IVI_SPECIFIC_ERROR_BASE + 66)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1238
try:
    NIHSDIO_ERROR_INVALID_CHANNEL_FOR_DATA_RATE_MULTIPLIER = (IVI_SPECIFIC_ERROR_BASE + 67)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1239
try:
    NIHSDIO_ERROR_SESSION_NOT_IN_COMMITED_STATE = (IVI_SPECIFIC_ERROR_BASE + 68)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1240
try:
    NIHSDIO_ERROR_WAVEFORM_DATA_WIDTH_MISMATCH = (IVI_SPECIFIC_ERROR_BASE + 70)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1241
try:
    NIHSDIO_ERROR_DIGITAL_STATE_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 71)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1242
try:
    NIHSDIO_ERROR_TRISTATE_MEMORY_FULL = (IVI_SPECIFIC_ERROR_BASE + 72)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1243
try:
    NIHSDIO_ERROR_FAILED_TO_START_HARDWARE_COMPARE = (IVI_SPECIFIC_ERROR_BASE + 73)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1244
try:
    NIHSDIO_ERROR_SAMPLE_ERRORS_NOT_AVAILABLE = (IVI_SPECIFIC_ERROR_BASE + 74)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1245
try:
    NIHSDIO_ERROR_EXPECTED_DATA_FIFO_OVERFLOW = (IVI_SPECIFIC_ERROR_BASE + 77)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1246
try:
    NIHSDIO_ERROR_EXPECTED_DATA_GENERATION_ERROR = (IVI_SPECIFIC_ERROR_BASE + 78)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1247
try:
    NIHSDIO_ERROR_WAVEFORM_HARDWARE_COMPARE_MISMATCH = (IVI_SPECIFIC_ERROR_BASE + 79)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1248
try:
    NIHSDIO_ERROR_INVALID_FUNCTION_FOR_HARDWARE_COMPARE = (IVI_SPECIFIC_ERROR_BASE + 80)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1249
try:
    NIHSDIO_ERROR_DATATYPE_OF_WFM_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 81)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1250
try:
    NIHSDIO_ERROR_EXPECTED_DATA_READY_TIMEOUT = (IVI_SPECIFIC_ERROR_BASE + 82)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1251
try:
    NIHSDIO_ERROR_SAMPLE_ERROR_BUFFER_OVERFLOW = (IVI_SPECIFIC_ERROR_BASE + 83)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1252
try:
    NIHSDIO_ERROR_INVALID_TRIGGER_TYPE_FOR_HARDWARE_COMPARE = (IVI_SPECIFIC_ERROR_BASE + 84)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1253
try:
    NIHSDIO_ERROR_FILE_CONTAINS_MULTIPLE_WAVEFORMS = (IVI_SPECIFIC_ERROR_BASE + 85)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1254
try:
    NIHSDIO_ERROR_STREAMING_WAVEFORM_NOT_SPECIFIED = (IVI_SPECIFIC_ERROR_BASE + 86)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1255
try:
    NIHSDIO_ERROR_STREAMING_DATA_OVERFLOW = (IVI_SPECIFIC_ERROR_BASE + 87)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1256
try:
    NIHSDIO_ERROR_STREAMING_DATA_UNDERFLOW = (IVI_SPECIFIC_ERROR_BASE + 88)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1257
try:
    NIHSDIO_ERROR_STREAMING_WAVEFORM_TOO_SMALL = (IVI_SPECIFIC_ERROR_BASE + 89)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1258
try:
    NIHSDIO_ERROR_INVALID_DIRECT_DMA_WINDOW_SIZE = (IVI_SPECIFIC_ERROR_BASE + 90)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1259
try:
    NIHSDIO_ERROR_INVALID_DIRECT_DMA_WINDOW_ADDRESS = (IVI_SPECIFIC_ERROR_BASE + 91)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1260
try:
    NIHSDIO_ERROR_CANNOT_SET_WAVEFORM_WRITE_POSITION = (IVI_SPECIFIC_ERROR_BASE + 92)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1261
try:
    NIHSDIO_ERROR_INVALID_CONTINUOUS_CONFIGURATION = (IVI_SPECIFIC_ERROR_BASE + 93)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1262
try:
    NIHSDIO_ERROR_INVALID_COMBINATION_DDR_CLOCK_VOLTAGE = (IVI_SPECIFIC_ERROR_BASE + 94)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1263
try:
    NIHSDIO_ERROR_OSP_FIFO_OVERFLOW = (IVI_SPECIFIC_ERROR_BASE + 95)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1264
try:
    NIHSDIO_ERROR_OSP_FIFO_UNDERFLOW = (IVI_SPECIFIC_ERROR_BASE + 96)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1265
try:
    NIHSDIO_ERROR_FUNCTION_NOT_SUPPORTED_WIN64U = (IVI_SPECIFIC_ERROR_BASE + 97)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1266
try:
    NIHSDIO_ERROR_MB_DATA_DELAY_VALUE_INCONSISTENT_ACROSS_BANK = (IVI_SPECIFIC_ERROR_BASE + 98)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1267
try:
    NIHSDIO_ERROR_WAVEFORM_TYPE_CONFLICT = (IVI_SPECIFIC_ERROR_BASE + 99)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1268
try:
    NIHSDIO_ERROR_INVALID_CHANNEL_FOR_CCT_AND_HWC = (IVI_SPECIFIC_ERROR_BASE + 100)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1269
try:
    NIHSDIO_ERROR_CANNOT_STREAM_WITH_HWC_ENABLED = (IVI_SPECIFIC_ERROR_BASE + 101)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1270
try:
    NIHSDIO_ERROR_FUNCTION_NOT_SUPPORTED_ON_NON_HWC_CCT_DEVICE = (IVI_SPECIFIC_ERROR_BASE + 102)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1271
try:
    NIHSDIO_ERROR_INVALID_DATA_WIDTH_FOR_SUPPORTED_DATA_STATES = (IVI_SPECIFIC_ERROR_BASE + 103)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1272
try:
    NIHSDIO_ERROR_EMPTY_CHANNEL_LIST_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 104)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1273
try:
    NIHSDIO_ERROR_STPMU_FUNCTION_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 105)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1274
try:
    NIHSDIO_ERROR_DEVICE_POWER_LIMIT_EXCEEDED = (IVI_SPECIFIC_ERROR_BASE + 106)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1275
try:
    NIHSDIO_ERROR_INVALID_SENSE_TERMINAL = (IVI_SPECIFIC_ERROR_BASE + 107)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1276
try:
    NIHSDIO_ERROR_INVALID_PMU_RETURN_STATE = (IVI_SPECIFIC_ERROR_BASE + 108)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1277
try:
    NIHSDIO_ERROR_INVALID_PMU_EXTERNAL_ACTION = (IVI_SPECIFIC_ERROR_BASE + 109)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1278
try:
    NIHSDIO_ERROR_INVALID_PMU_CURRENT_RANGE = (IVI_SPECIFIC_ERROR_BASE + 110)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1279
try:
    NIHSDIO_ERROR_INVALID_PMU_CONNECTOR = (IVI_SPECIFIC_ERROR_BASE + 111)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1280
try:
    NIHSDIO_ERROR_DDS_CLOCK_FAILED_TO_LOCK = (IVI_SPECIFIC_ERROR_BASE + 112)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1281
try:
    NIHSDIO_ERROR_STPMU_MULTIPLE_CHANNELS_FOR_EXT_SENSE = (IVI_SPECIFIC_ERROR_BASE + 113)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1282
try:
    NIHSDIO_ERROR_STPMU_SENSE_TERMINAL_MISMATCH = (IVI_SPECIFIC_ERROR_BASE + 114)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1283
try:
    NIHSDIO_ERROR_VOLTAGE_RANGE_RESERVATION = (IVI_SPECIFIC_ERROR_BASE + 115)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1284
try:
    NIHSDIO_ERROR_VOLTAGE_VALUE_NOT_WITHIN_VOLTAGE_RANGE = (IVI_SPECIFIC_ERROR_BASE + 116)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1285
try:
    NIHSDIO_ERROR_STPMU_INVALID_APERTURE_TIME = (IVI_SPECIFIC_ERROR_BASE + 117)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1286
try:
    NIHSDIO_ERROR_STPMU_UNINITIALIZED_CHANNEL = (IVI_SPECIFIC_ERROR_BASE + 118)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1287
try:
    NIHSDIO_ERROR_INVALID_CHANNEL_DELAY_POSITION = (IVI_SPECIFIC_ERROR_BASE + 119)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1288
try:
    NIHSDIO_ERROR_INVALID_DESKEW_BELOW_DCM_THRESHOLD = (IVI_SPECIFIC_ERROR_BASE + 120)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1289
try:
    NIHSDIO_ERROR_STPMU_INVALID_VOLTAGE = (IVI_SPECIFIC_ERROR_BASE + 121)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1290
try:
    NIHSDIO_ERROR_STPMU_INVALID_CURRENT = (IVI_SPECIFIC_ERROR_BASE + 122)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1291
try:
    NIHSDIO_ERROR_STPMU_INVALID_CURRENT_FOR_SELECTED_RANGE = (IVI_SPECIFIC_ERROR_BASE + 123)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1292
try:
    NIHSDIO_ERROR_SELF_CALIBRATION_FAILED = (IVI_SPECIFIC_ERROR_BASE + 124)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1293
try:
    NIHSDIO_ERROR_PIN_RESERVED_FOR_EXTERNAL_CONNECTION = (IVI_SPECIFIC_ERROR_BASE + 125)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1294
try:
    NIHSDIO_ERROR_IMPEDANCE_NOT_SUPPORTED_ON_STROBE = (IVI_SPECIFIC_ERROR_BASE + 126)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1295
try:
    NIHSDIO_ERROR_STPMU_INVALID_VOLTAGE_CLAMP_DIFFERENCE = (IVI_SPECIFIC_ERROR_BASE + 127)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1296
try:
    NIHSDIO_ERROR_TRIG_OR_EVENT_ON_RESERVED_CLOCK_TERMINAL = (IVI_SPECIFIC_ERROR_BASE + 128)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1297
try:
    NIHSDIO_ERROR_VTT_TRISTATE_TERMINATION_MODE_RESERVATION = (IVI_SPECIFIC_ERROR_BASE + 129)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1298
try:
    NIHSDIO_ERROR_CANNOT_TRISTATE_PFI_LINES = (IVI_SPECIFIC_ERROR_BASE + 130)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1299
try:
    NIHSDIO_ERROR_EXTERNAL_CONNECTOR_MISMATCH = (IVI_SPECIFIC_ERROR_BASE + 131)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1300
try:
    NIHSDIO_ERROR_MULTI_SAMPLE_PATTERN_MATCH_WITH_DDR_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 132)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1301
try:
    NIHSDIO_ERROR_TOO_MANY_PATTERN_SAMPLES_GIVEN = (IVI_SPECIFIC_ERROR_BASE + 133)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1302
try:
    NIHSDIO_ERROR_RF_EDGES_IN_SAMPLES_AFTER_FIRST_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 134)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1303
try:
    NIHSDIO_ERROR_MULTI_SAMPLE_PATTERN_MATCH_INVALID_TRIGGER_WHEN_SETTING = (IVI_SPECIFIC_ERROR_BASE + 135)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1304
try:
    NIHSDIO_ERROR_PFI_RESERVATION_CONFLICT = (IVI_SPECIFIC_ERROR_BASE + 136)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1305
try:
    NIHSDIO_ERROR_MUST_ASSIGN_STATIC_PFI_BEFORE_TRISTATE = (IVI_SPECIFIC_ERROR_BASE + 137)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1306
try:
    NIHSDIO_ERROR_NOT_A_SUBSET_OF_ASSIGNED_DYNAMIC_CHANNELS = (IVI_SPECIFIC_ERROR_BASE + 138)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1307
try:
    NIHSDIO_ERROR_AUX_IO_CONNECTOR_NOT_SUPPORTED = (IVI_SPECIFIC_ERROR_BASE + 139)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1308
try:
    NIHSDIO_ERROR_MISMATCHED_PFI_ATTR_CONFIGURATION = (IVI_SPECIFIC_ERROR_BASE + 140)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1309
try:
    NIHSDIO_ERROR_INVALID_VOLTAGE_RANGE_ON_PFI_OR_CLOCK_LINE = (IVI_SPECIFIC_ERROR_BASE + 141)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1310
try:
    NIHSDIO_ERROR_CHILD_SESSION_ALREADY_INITIALIZED = (IVI_SPECIFIC_ERROR_BASE + 142)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1311
try:
    NIHSDIO_ERROR_INVALID_SESSION_TYPE = (IVI_SPECIFIC_ERROR_BASE + 143)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1312
try:
    NIHSDIO_ERROR_UNRECOGNIZED_CHILD_SESSION = (IVI_SPECIFIC_ERROR_BASE + 144)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1313
try:
    NIHSDIO_ERROR_CAL_INVALID_CALIBRATION_REFERENCE_NUMBER = (IVI_SPECIFIC_ERROR_BASE + 145)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1314
try:
    NIHSDIO_ERROR_CAL_INVALID_CALIBRATION_TYPE = (IVI_SPECIFIC_ERROR_BASE + 146)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1315
try:
    NIHSDIO_ERROR_CAL_INVALID_ARRAY_SIZE = (IVI_SPECIFIC_ERROR_BASE + 147)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1316
try:
    NIHSDIO_ERROR_CAL_PULSE_ADJUST_REFERENCE_STEPS_OUT_OF_ORDER = (IVI_SPECIFIC_ERROR_BASE + 148)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1317
try:
    NIHSDIO_ERROR_CAL_ADJUST_STEP_MISSING = (IVI_SPECIFIC_ERROR_BASE + 149)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1318
try:
    NIHSDIO_ERROR_CAL_INVALID_CONNECTOR_SPECIFIED = (IVI_SPECIFIC_ERROR_BASE + 150)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1319
try:
    NIHSDIO_ERROR_CAL_VALUE_OUT_OF_RANGE = (IVI_SPECIFIC_ERROR_BASE + 151)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1324
try:
    NIHSDIO_WARN_NSUP_ID_QUERY = (IVI_SPECIFIC_WARN_BASE + 1)
except:
    pass

# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 1325
try:
    NIHSDIO_WARN_PLL_BECAME_UNLOCKED = (IVI_SPECIFIC_WARN_BASE + 2)
except:
    pass

niHSDIO_wfmInfo = struct_niHSDIO_wfmInfo# C:\\Program Files (x86)\\IVI Foundation\\IVI\\Include\\niHSDIO.h: 829

# No inserted files

# No prefix-stripping

