%define build_number 1
%define debug_package %{nil}

Name:           pidgin-libfetion
Version:        1.1.0
Release:        1%{?dist}
Summary:        The fetion plugin for pidgin 

Group:          Applications/Internet
License:        GPLv2
URL:            https://github.com/cnangel/pidgin-libfetion
Source0:        %{name}-%{version}.tar.gz
Requires:		libpurple pidgin
BuildRequires:  libpurple-devel


%description	
%{name} is a pidgin plugin, you can send sms for your friend.

%prep 
%setup -q

%build 
%configure 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib/purple-2/libfetion.so
%exclude /usr/lib/purple-2/libfetion.la
%{_datadir}
