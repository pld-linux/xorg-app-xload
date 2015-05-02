Summary:	xload application - system load average display for X
Summary(pl.UTF-8):	Aplikacja xload - wyświetlanie obciążenia systemu pod X
Name:		xorg-app-xload
Version:	1.1.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xload-%{version}.tar.bz2
# Source0-md5:	b9e9808db18acecf4cdec134d86b157c
Source1:	xload.desktop
Source2:	xload.png
Source3:	xload.1x.it
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xload program displays a periodically updating histogram of the
system load average.

%description -l pl.UTF-8
Program xload wyświetla okresowo uaktualniany histogram średniego
obciążenia systemu (load average).

%prep
%setup -q -n xload-%{version}

%build
%{__aclocal} -I m4
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
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/it/man1/xload.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xload
%{_datadir}/X11/app-defaults/XLoad
%{_desktopdir}/xload.desktop
%{_pixmapsdir}/xload.png
%{_mandir}/man1/xload.1*
%lang(it) %{_mandir}/it/man1/xload.1*
