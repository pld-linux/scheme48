Summary:	Implementation of Scheme
Summary(pl):	Implementacja Scheme
Name:		scheme48
Version:	1.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://s48.org/%{version}/%{name}-%{version}.tgz
# Source0-md5:	43507090660f0635e14764a72c5f7b08
URL:		http://s48.org/
BuildRequires:	elfutils-devel
BuildRequires:	rpmbuild(macros) >= 1.213
ExcludeArch:	%{x8664} alpha ia64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scheme 48 is an implementation of Scheme written by Richard Kelsey and
Jonathan Rees. It is based on a byte-code interpreter and is designed
to be used as a testbed for experiments in implementation techniques
and as an expository tool.

%description -l pl
Scheme 48 to implementacja Scheme napisana przez Richarda Kelseya i
Jonathana Reesa. Jest oparta na interpreterze byte-codu i zosta³a
zaprojektowana z my¶l± o wykorzystaniu do eksperymentów w technikach
implementacji i jako narzêdzie demonstracyjne.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
