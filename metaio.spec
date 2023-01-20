# TODO: matlab (octave?)
Summary:	Library for parsing LIGO_LW Table files
Summary(pl.UTF-8):	Biblioteka do analizy plików tablic LIGO_LW
Name:		metaio
Version:	8.5.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.gz
# Source0-md5:	ba697ca9f77d80bf111c531a0f53e5fb
Patch0:		format-security.patch
URL:		https://wiki.ligo.org/Computing/DASWG/MetaIO
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool >= 2:2
BuildRequires:	zlib-devel >= 1.2
Requires:	zlib >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a library for parsing LIGO_LW Table files, plus
several C programs based on the library. The metiao library can read
XML files compressed with the gzip compression algorithm.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę do analizy plików tablic LIGO_LW oraz
kilka programów w C opartych na tej bibliotece. Biblioteka metaio
potrafi czytać pliki XML skompresowane algorytmem gzip.

%package devel
Summary:	Header files for metaio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki metaio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for metaio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki metaio.

%package static
Summary:	Static metaio library
Summary(pl.UTF-8):	Statyczna biblioteka metaio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static metaio library.

%description static -l pl.UTF-8
Statyczna biblioteka metaio.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmetaio.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY README
%attr(755,root,root) %{_bindir}/_getMetaLoopHelper
%attr(755,root,root) %{_bindir}/concatMeta
%attr(755,root,root) %{_bindir}/lwtcut
%attr(755,root,root) %{_bindir}/lwtdiff
%attr(755,root,root) %{_bindir}/lwtprint
%attr(755,root,root) %{_bindir}/lwtscan
%attr(755,root,root) %{_bindir}/lwtselect
%attr(755,root,root) %{_libdir}/libmetaio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetaio.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmetaio.so
%{_includedir}/ligo_lw_header.h
%{_includedir}/metaio.h
%{_pkgconfigdir}/libmetaio.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmetaio.a
