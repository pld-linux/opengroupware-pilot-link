%define		pilot-link_makeflags	-w
%define		__source	.
Summary:	OGo Pilot link
Name:		opengroupware.org-pilot-link
Version:	1.0a
Release:	8
Vendor:		http://www.opengroupware.org
License:	LGPL
Group:		Development/Libraries
AutoReqProv:	off
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
#Patch:
URL:		http://www.gnustep.org
#Requires:
#BuildPreReq:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Requires:	readline
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gnustep-make >= 1.10
BuildRequires:	readline-devel >= 4.3
BuildRequires:	libiconv-devel >= 1.9.2
BuildRequires:	perl
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	compat-libg++-2.7
BuildRequires:	libpng-devel >= 1.2.7
BuildRequires:	libxml2-devel
BuildRequires:	postgresql-devel
BuildRequires:	openldap-devel >= 2.2.17
BuildRequires:	libxml2-progs


libc6-dev
gobjc
libpisock-devel

# BuildRequires:	ElectricFence >= 2.2.2

%description

%description -l pl

%package opengroupware.org-pilot-link-devel
Summary:	opengroupware.org pilot link devel
Group:		Development/Libraries
#Requires:  gnustep-make
AutoReqProv:	off

%description opengroupware.org-pilot-link-devel
opengroupware.org pilot link devel package.


%package opengroupware.org-pilot-link
Summary:	opengroupware.org pilot link
Group:		Development/Libraries
#Requires:  gnustep-make
AutoReqProv:	off

%description opengroupware.org-pilot-link
opengroupware.org pilot link  package.



%prep
%setup -q -n %{name}

%build
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%configure
%{__make} %{pilot-link_makeflags} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} %{pilot-link_makeflags} INSTALL_ROOT_DIR=${RPM_BUILD_ROOT} \
                       GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}%{_prefix} \
                       FHS_INSTALL_ROOT=${RPM_BUILD_ROOT}%{_prefix} \
                       install


%pre


%post


%postun

%clean
rm -fr ${RPM_BUILD_ROOT}


%files opengroupware.org-pilot-link
%defattr(644,root,root,755)
%dir %attr(700,ogo,skyrix)


%files opengroupware.org-pilot-link-devel
%defattr(644,root,root,755)
%dir %attr(700,ogo,skyrix)
