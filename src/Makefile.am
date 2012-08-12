# $Id: Makefile.am,v 1.0.0-0 2012/08/12 14:58:27 Cnangel Exp $

AUTOMAKE_OPTIONS						= foreign

AM_CFLAGS								= $(st)

AM_CPPFLAGS								= -DDISPLAY_VERSION='"@PACKAGE_VERSION@"' \
										  $(PURPLE_CFLAGS) \
										  $(NULL)

# {{{ /* fetion_src_files 				= */
fetion_src_files						= f_buddy.c \
                                          f_buddy.h \
                                          f_chat.c \
                                          f_chat.h \
                                          fetion.c \
                                          fetion.h \
                                          f_gchat.c \
                                          f_gchat.h \
                                          f_group.c \
                                          f_group.h \
                                          f_login.c \
                                          f_login.h \
                                          f_portrait.c \
                                          f_portrait.h \
                                          f_sysmsg.c \
                                          f_sysmsg.h \
                                          f_user.c \
                                          f_user.h \
                                          f_util.c \
                                          f_util.h \
                                          f_zone.c \
                                          f_zone.h \
                                          internal.h \
                                          sipmsg.c \
                                          sipmsg.h \
										  $(NULL)
# }}}

pluginsdir								= $(libdir)/purple-2
pkgdir									= $(pluginsdir)

if STATIC_FETION

st										= -DPURPLE_STATIC_PRPL
noinst_LIBRARIES						= libfetion.a
libfetion_a_SOURCES						= $(fetion_src_files)
libfetion_a_CFLAGS						= $(AM_CFLAGS)

else

st										= -DPURPLE_PLUGINS
pkg_LTLIBRARIES							= libfetion.la
libfetion_la_SOURCES					= $(fetion_src_files)
libfetion_la_LDFLAGS					= -module -avoid-version \
										  $(PURPLE_LIBS) \
										  -lssl \
										  $(NULL)
endif


#/*
# * Local variables:
# * tab-width: 4
# * c-basic-offset: 4
# * End:
# * vim600: noet sw=4 ts=4 fdm=marker
# * vim<600: noet sw=4 ts=4
# */

