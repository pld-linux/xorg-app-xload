Summary:	xload application
Summary(pl):	Aplikacja xload
Name:		xorg-app-xload
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/xload-%{version}.tar.bz2
# Source0-md5:	ba013813f9c21eb015559466f8d02a44
Source1:	xload.desktop
Source2:	xload.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xload application.

%description -l pl
Aplikacja xload.

%prep
%setup -q -n xload-%{version}

%build
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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xload.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xload.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/X11/app-defaults/*
%{_desktopdir}/xload.desktop
%{_pixmapsdir}/xload.png
%{_mandir}/man1/*.1x*
