Summary:	X Video extension library
Summary(pl):	Biblioteka rozszerzenia X Video
Name:		xorg-lib-libXv
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXv-%{version}.tar.bz2
# Source0-md5:	e2000d3d8ac1e3649902e0ea49883569
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Video extension library.

%description -l pl
Biblioteka rozszerzenia X Video.

%package devel
Summary:	Header files libXv development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXv
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-videoproto-devel
Obsoletes:	libXv-devel

%description devel
X Video extension library.

This package contains the header files needed to develop programs that
use these libXv.

%description devel -l pl
Biblioteka rozszerzenia X Video.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXv.

%package static
Summary:	Static libXv library
Summary(pl):	Biblioteka statyczna libXv
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXv-static

%description static
X Video extension library.

This package contains the static libXv library.

%description static -l pl
Biblioteka rozszerzenia X Video.

Pakiet zawiera statyczn± bibliotekê libXv.

%prep
%setup -q -n libXv-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT \
	libmandir=%{_mandir}/man3 \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXv.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXv.so
%{_libdir}/libXv.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xv.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXv.a
