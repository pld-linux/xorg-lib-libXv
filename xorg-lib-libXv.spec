
#
Summary:	X Video extension library
Summary(pl):	Biblioteka rozszerzenia X Video
Name:		xorg-lib-libXv
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXv-%{version}.tar.bz2
# Source0-md5:	e808a81da74d8adcd60bdad93ceecabf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-videoproto-devel
BuildRoot:	%{tmpdir}/libXv-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Video extension library.

%description -l pl
Biblioteka rozszerzenia X Video.


%package devel
Summary:	Header files libXv development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXv
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXv = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-videoproto-devel

%description devel
X Video extension library.

This package contains the header files needed to develop programs that
use these libXv.

%description devel -l pl
Biblioteka rozszerzenia X Video.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXv.


%package static
Summary:	Static libXv libraries
Summary(pl):	Biblioteki statyczne libXv
Group:		Development/Libraries
Requires:	xorg-lib-libXv-devel = %{version}-%{release}

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
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXv.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXv.la
%attr(755,root,wheel) %{_libdir}/libXv.so
%{_pkgconfigdir}/xv.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXv.a
