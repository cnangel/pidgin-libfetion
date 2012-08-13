# $Id: Makefile.am,v 1.0.0-0 2012/08/13 10:11:36 Cnangel Exp $

AUTOMAKE_OPTIONS = foreign

EXTRA_DIST = protocols
			 $(NULL)

install: install-localdata-local

install-localdata-local:
	@echo install res files to $(datadir)
	@test -d $(datadir)/pixmaps/pidgin || mkdir -p $(datadir)/pixmaps/pidgin
	@cp -r $(top_srcdir)/pixmaps/protocols $(datadir)/pixmaps/pidgin

uninstall: uninstall-localdata-local

uninstall-localdata-local:
	@echo uninstall res files from $(datadir)
	@rm -f $(datadir)/pixmaps/pidgin/protocols/16/fetion.png
	@rm -f $(datadir)/pixmaps/pidgin/protocols/22/fetion.png
	@rm -f $(datadir)/pixmaps/pidgin/protocols/48/fetion.png
	

