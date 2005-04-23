# TODO: spec filename vs Name
%define		pilot-link_makeflags	-w
Summary:	OGo Pilot link
Summary(pl):	pilot-link dla OGo
Name:		opengroupware.org-pilot-link
Version:	1.0a
Release:	8
License:	LGPL
Group:		Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
URL:		http://www.opengroupware.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make >= 1.10
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	openldap-devel >= 2.2.17
BuildRequires:	perl-base
BuildRequires:	pilot-link-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel >= 4.3
# we don't want these
#BuildRequires:	compat-libg++-2.7
#BuildRequires:	libiconv-devel >= 1.9.2
#AutoReqProv:	off
# should be autodetected
#Requires:	readline
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OGo Pilot link.

%description -l pl
pilot-link dla OGo.

%package devel
Summary:	opengroupware.org pilot link devel
Summary(pl):	Pakiet programistyczny pilot-link dla opengroupware.org
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-make-devel

%description devel
opengroupware.org pilot link devel package.

%description devel -l pl
Pakiet programistyczny pilot-link dla opengroupware.org.

%prep
%setup -q -n %{name}

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%configure
%{__make} %{pilot-link_makeflags} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} %{pilot-link_makeflags} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix} \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%dir %attr(700,ogo,skyrix)

%files devel
%defattr(644,root,root,755)
#%dir %attr(700,ogo,skyrix)
