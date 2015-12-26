Summary:	This package contains a library for parsing LIGO_LW Table files
Name:		metaio
Version:	8.3.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	https://www.lsc-group.phys.uwm.edu/daswg/download/software/source/%{name}-%{version}.tar.gz
# Source0-md5:	4d244197051fc1c1a9c2c5f82e14dc4c
Patch0:		format-security.patch
URL:		https://www.lsc-group.phys.uwm.edu/daswg/projects/metaio.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a library for parsing LIGO_LW Table files, plus
several C programs based on the library, plus a few Tcl scripts which
do related things. The metiao library can read XML files compressed
with the gzip compression algorithm. Metaio is available via the
lscsoft repository, from source of via LIGOtools.

%package devel
Summary:	Devel files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files.

%package static
Summary:	Static metaio library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static metaio library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetaio.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmetaio.la
%{_libdir}/libmetaio.so
%{_includedir}/ligo_lw_header.h
%{_includedir}/metaio.h
%{_pkgconfigdir}/libmetaio.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
