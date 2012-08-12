#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.59])
AC_INIT([pidgin-libfetion], [1.1.0], [https://github.com/cnangel/pidgin-libfetion])
AC_CONFIG_SRCDIR([src/fetion.h])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([1.9 tar-pax])
AM_INIT_AUTOMAKE([pidgin-libfetion], [1.1.0])

PACKAGE_RELEASE=1
BITS=`if [[ 64 -eq $(getconf LONG_BIT) ]]; then echo -n $(getconf LONG_BIT); fi`
PACKAGE_URL=https://github.com/cnangel/pidgin-libfetion
DOXYGEN_OUTPUT_DIR=doc/doxygen
PURPLE_PLUGINDIR=$(pkg-config --variable=plugindir purple)
pluginsdir=${PURPLE_PLUGINDIR}

AC_SUBST(PACKAGE_RELEASE)
AC_SUBST(BITS)
AC_SUBST(PACKAGE_URL)
AC_SUBST(DOXYGEN_OUTPUT_DIR)
AC_SUBST(PURPLE_PLUGINDIR)
AC_SUBST(pluginsdir)

# Checks for programs.
AC_PROG_CXX
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AM_DISABLE_STATIC
AC_LIBTOOL_DLOPEN
AC_PROG_LIBTOOL

# Check for pkg-config 
PKG_PROG_PKG_CONFIG

PKG_CHECK_MODULES([GLIB],[glib-2.0])

PKG_CHECK_MODULES([PURPLE],[purple >= 2.7.0],,AC_MSG_ERROR([
				   *** libpurple 2.0+ >=2.7.0 is required to build.]))

PKG_CHECK_MODULES([XML2],[libxml-2.0 >= 2.6.0],,AC_MSG_ERROR([
				   *** libxml-2.0 >= 2.6.0 is required to build.]))

PKG_CHECK_MODULES([OPENSSL],[openssl >= 0.9.6],,AC_MSG_ERROR([
				   *** openssl >= 0.9.6 is required to build.]))

# Checks for libraries.

# Checks for header files.
AC_CHECK_HEADERS([arpa/inet.h fcntl.h locale.h netdb.h netinet/in.h stdint.h stdlib.h string.h sys/ioctl.h sys/socket.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_INLINE

# Checks for library functions.
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([memmove memset setlocale strstr strtol])

AM_CONDITIONAL([STATIC_FETION],[false])

AC_CONFIG_FILES([Doxyfile
				 Makefile
                 data/Makefile
                 doc/Makefile
                 locale/po/Makefile
				 pidgin-libfetion.spec
                 pixmaps/protocols/16/Makefile
                 pixmaps/protocols/22/Makefile
                 src/Makefile])
AC_OUTPUT
