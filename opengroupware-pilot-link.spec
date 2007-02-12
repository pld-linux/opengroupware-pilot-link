# TODO: spec filename vs Name
%define		datatrunk	200508291711

Summary:	OGo Pilot link
Summary(pl.UTF-8):   pilot-link dla OGo
Name:		opengroupware.org-pilot-link
Version:	r124
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.opengroupware.org/nightly/sources/trunk/%{name}-trunk-%{version}-%{datatrunk}.tar.gz
# Source0-md5:	0df4f7ba3a9e7d90bcc9b3636b984a9a
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OGo Pilot link.

%description -l pl.UTF-8
pilot-link dla OGo.

%package devel
Summary:	opengroupware.org pilot link devel
Summary(pl.UTF-8):   Pakiet programistyczny pilot-link dla opengroupware.org
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-make-devel

%description devel
opengroupware.org pilot link devel package.

%description devel -l pl.UTF-8
Pakiet programistyczny pilot-link dla opengroupware.org.

%prep
%setup -q -n %{name}

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
./configure

%{__make} -w all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -w install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%dir %attr(700,ogo,skyrix)

%files devel
%defattr(644,root,root,755)
#%dir %attr(700,ogo,skyrix)
