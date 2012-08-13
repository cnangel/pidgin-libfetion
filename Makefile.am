# $Id: Makefile.am,v 1.0.0-0 2012/08/12 14:50:33 Cnangel Exp $

AUTOMAKE_OPTIONS						= foreign
EXTRA_DIST								= @PACKAGE@.spec \
										  .gitignore \
										  Makefile.mingw \
										  Message.sh \
										  $(NULL)

ACLOCAL_AMFLAGS							= -I m4
SUBDIRS									= doc \
										  data \
										  pixmaps \
										  locale/po \
										  src \
										  $(NULL)

# define rpm build root
RPMBUILDTOPDIR		= $(shell unset RPMBUILDTOPDIR; if [ -f ${HOME}/.rpmmacros ]; then export RPMBUILDTOPDIR=`grep _topdir ${HOME}/.rpmmacros|head -1|awk '{print $$2}'`; else if [ -z $(RDIR) ]; then export RPMBUILDTOPDIR=target; else export RPMBUILDTOPDIR=$(RDIR); fi; fi; echo $${RPMBUILDTOPDIR};)
PROCESSOR = $(shell uname -p)

.PHONY: rpm doc

doc:
	$(mkdir_p) @DOXYGEN_OUTPUT_DIR@
	doxygen
	sed -i -e "s/charset=iso-8859-1/charset=utf-8/g" $(top_builddir)/doc/doxygen/html/*.html

rpm: dist @PACKAGE@.spec
	$(mkdir_p) ${RPMBUILDTOPDIR}/{BUILD,RPMS,SOURCES,SPECS,SRPMS,BUILDROOT}
	$(RM) ${RPMBUILDTOPDIR}/SOURCES/$(distdir).tar.gz
	$(RM) ${RPMBUILDTOPDIR}/SPECS/@PACKAGE@.spec
	$(LN_S) `pwd`/$(distdir).tar.gz ${RPMBUILDTOPDIR}/SOURCES
	$(LN_S) `pwd`/@PACKAGE@.spec ${RPMBUILDTOPDIR}/SPECS
	rpmbuild -ba ${RPMBUILDTOPDIR}/SPECS/@PACKAGE@.spec $(OPTIONS)
	cp -f ${RPMBUILDTOPDIR}/RPMS/${PROCESSOR}/@PACKAGE@*@VERSION@* ${RPMBUILDTOPDIR}


CLEANDIRS								= doc/doxygen
CLEANFILES								= *~ *.log

clean-local:
	-test -z "$(CLEANDIRS)" || rm -rf $(CLEANDIRS)

