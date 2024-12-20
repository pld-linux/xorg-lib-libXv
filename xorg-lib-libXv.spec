Summary:	X Video (Xv) extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Video (Xv)
Name:		xorg-lib-libXv
Version:	1.0.13
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXv-%{version}.tar.xz
# Source0-md5:	8a26503185afcb1bbd2c65e43f775a67
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXv < 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXv is a library for the X Video (Xv) extension to the X Window
System.

%description -l pl.UTF-8
libXv to biblioteka rozszerzenia X Video (Xv) systemu X Window.

%package devel
Summary:	Header files for libXv library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXv
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-xextproto-devel
Obsoletes:	libXv-devel < 2.3

%description devel
libXv is a library for the X Video (Xv) extension to the X Window
System.

This package contains the header files needed to develop programs that
use libXv.

%description devel -l pl.UTF-8
libXv to biblioteka rozszerzenia X Video (Xv) systemu X Window.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXv.

%package static
Summary:	Static libXv library
Summary(pl.UTF-8):	Biblioteka statyczna libXv
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXv-static < 2.3

%description static
libXv is a library for the X Video (Xv) extension to the X Window
System.

This package contains the static libXv library.

%description static -l pl.UTF-8
libXv to biblioteka rozszerzenia X Video (Xv) systemu X Window.

Pakiet zawiera statyczną bibliotekę libXv.

%prep
%setup -q -n libXv-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXv.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXv.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXv.so
%{_includedir}/X11/extensions/Xvlib.h
%{_pkgconfigdir}/xv.pc
%{_mandir}/man3/Xv*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXv.a
