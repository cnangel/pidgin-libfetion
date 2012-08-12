# $Id: Makefile.am,v 1.0.0-0 2012/08/12 14:58:27 Cnangel Exp $

AUTOMAKE_OPTIONS						= foreign

AM_CFLAGS								= $(st)

AM_CPPFLAGS								= -DDISPLAY_VERSION='"@PACKAGE_VERSION@"' \
										  -DRES_DIR='"$(datadir)/purple/@PACKAGE_NAME@/"' \
										  -DGETTEXT_PACKAGE='"@PACKAGE_NAME@"' \
										  -DLOCALE_DIR='"$(datadir)/purple/@PACKAGE_NAME@/mo/"' \
										  -DENABLE_NLS \
										  $(PURPLE_CFLAGS) \
										  $(XML2_CFLAGS) \
										  $(OPENSSL_CFLAGS) \
										  $(NULL)

# {{{ /* fetion_src_files 				= */
fetion_src_files						= fetion.h \
                                          fx_blist.c \
                                          fx_blist.h \
                                          fx_buddy.c \
                                          fx_buddy.h \
                                          fx_chat.c \
                                          fx_chat.h \
                                          fx_contact.c \
                                          fx_contact.h \
                                          fx_login.c \
                                          fx_login.h \
                                          fx_sip.c \
                                          fx_sip.h \
                                          fx_types.h \
                                          fx_user.c \
                                          fx_user.h \
                                          fx_util.c \
                                          openfetion.c \
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
										  $(XML2_LIBS) \
										  $(OPENSSL_LIBS) \
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

