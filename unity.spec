%define _disable_ld_no_undefined 1

%define major	5
%define abi		5.0
%define libname	%mklibname unity-core	%{major}
%define develname	%mklibname unity-core	-d

Summary:	A desktop experience designed for efficiency of space and interaction
Name:		unity
Version:	7.6.0
Release:	1
License:	GPLv3 LGPLv3
Url:		http://launchpad.net/unity
Group:		Graphical desktop/Other
Source0:	https://gitlab.com/ubuntu-unity/unity/unity/-/archive/master/unity-master.tar.bz2
#Patch0:		unity-5.12.0-disable-tests.patch
#Patch1:		unity-5.12.0-libdir-hack.patch
#Patch3:		unity-5.12.0_linking.patch
#Patch4:		unity-5.12.0-schema_error.patch
# disable launcher test as depends on xfixes 6
#Patch5:		unity-5.12.0-disable_launcher_test.patch
BuildRequires:	cmake
BuildRequires:	vala
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	compiz-devel
BuildRequires:	pkgconfig(gmock)
BuildRequires:	vala-devel
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(dbusmenu-glib-0.4)
BuildRequires:	pkgconfig(dee-1.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libbamf3)
BuildRequires:	pkgconfig(libcompizconfig)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libgeis)
BuildRequires:	pkgconfig(nux-4.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(unity)
BuildRequires:	pkgconfig(unity-misc)
BuildRequires:  pkgconfig(unity-settings-daemon)
BuildRequires:	pkgconfig(grail)
#BuildRequires:  pkgconfig(gdu)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xpathselect)
BuildRequires:  pkgconfig(zeitgeist-2.0)
#BuildRequires:	compiz-plugins-main-devel
BuildRequires:  lib64ido-devel

Requires:	compiz >= 0.9.2.1
#Requires:	compizconfig-settings-manager >= 0.9.2.1

#-- Indicators (suggested/available)
#Suggests:	indicator-appmenu
#Suggests:	indicator-application
#Suggests:	indicator-datetime
#Suggests:	indicator-me
#Suggests:	indicator-messages
#Suggests:	indicator-session
#Suggests:	indicator-sound
#-- Lens packages (available)
#Suggests:	unity-lens-applications
#Suggests:	unity-lens-files
#-- Unity requiresments
#Suggests:	unity-asset-pool

Requires:	%{libname} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description
Unity is a desktop experience that sings. Designed by Canonical and the Ayatana
community, Unity is all about the combination of familiarity and the future. We
bring together the visual design, analysis of experience testing, modern
graphics technologies and a deep understanding of the free software landscape,

%package common
Summary:	Common files for the Unity interface
Group:		Graphical desktop/Other
BuildArch:	noarch

%description common
Common files for the Unity interface.

%package services
Summary:	Services for the Unity interface
Group:		Graphical desktop/Other

%description services
Services for the Unity interface

%package -n %{libname}
Summary:	Core shared library of the Unity Desktop
Group:		System/Libraries

%description -n %{libname}
Unity is a desktop experience that sings. Designed by Canonical and the Ayatana
community, Unity is all about the combination of familiarity and the future. We
bring together the visual design, analysis of experience testing, modern
graphics technologies and a deep understanding of the free software landscape,

This package provides the shared core libraries for the Unity Desktop.

%package -n %{develname}
Summary:	Development files of the Unity Desktop
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for Unity and libunity-core

%prep
%setup -q -n unity-master
%autopatch -p1

%build
%cmake \
  -DCOMPIZ_BUILD_WITH_RPATH=FALSE \
  -DCOMPIZ_PACKAGING_ENABLED=ON \
  -DCOMPIZ_PLUGIN_INSTALL_TYPE=package \
  -DCOMPIZ_INSTALL_GCONF_SCHEMA_DIR=%{_sysconfdir}/gconf/schemas \
  -DGSETTINGS_LOCALINSTALL=OFF
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/unity
%{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/unitymtgrabhandles/
%{_mandir}/man1/unity.1*

%files common
%doc README COPYING COPYING.LGPL
%dir %{_prefix}/lib/unity
%dir %{_datadir}/unity
%dir %{_datadir}/unity/themes
%{_prefix}/lib/unity/*.py
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/unity/4/
%{_datadir}/ccsm/
%{_datadir}/unity/themes/dash-widgets.json

%files services
%{_prefix}/lib/unity/unity-panel-service
%{_datadir}/dbus-1/services/com.canonical.Unity.Panel.Service.service
%{_mandir}/man1/unity-panel-service*.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/Unity-%{abi}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

