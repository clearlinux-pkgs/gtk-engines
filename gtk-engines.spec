#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-engines
Version  : 2.20.2
Release  : 2
URL      : https://download.gnome.org/core/3.20/3.20.2/sources/gtk-engines-2.20.2.tar.gz
Source0  : https://download.gnome.org/core/3.20/3.20.2/sources/gtk-engines-2.20.2.tar.gz
Summary  : Default GTK+ theme engines
Group    : Development/Tools
License  : LGPL-2.1
Requires: gtk-engines-lib
Requires: gtk-engines-data
Requires: gtk-engines-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-2.0)

%description
These are the graphical engines for the various GTK+ toolkit themes.

%package data
Summary: data components for the gtk-engines package.
Group: Data

%description data
data components for the gtk-engines package.


%package dev
Summary: dev components for the gtk-engines package.
Group: Development
Requires: gtk-engines-lib
Requires: gtk-engines-data
Provides: gtk-engines-devel

%description dev
dev components for the gtk-engines package.


%package lib
Summary: lib components for the gtk-engines package.
Group: Libraries
Requires: gtk-engines-data

%description lib
lib components for the gtk-engines package.


%package locales
Summary: locales components for the gtk-engines package.
Group: Default

%description locales
locales components for the gtk-engines package.


%prep
%setup -q -n gtk-engines-2.20.2

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gtk-engines

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gtk-engines/clearlooks.xml
/usr/share/gtk-engines/crux-engine.xml
/usr/share/gtk-engines/glide.xml
/usr/share/gtk-engines/hcengine.xml
/usr/share/gtk-engines/industrial.xml
/usr/share/gtk-engines/mist.xml
/usr/share/gtk-engines/redmond95.xml
/usr/share/gtk-engines/thinice.xml
/usr/share/themes/Clearlooks/gtk-2.0/gtkrc
/usr/share/themes/Crux/gtk-2.0/gtkrc
/usr/share/themes/Industrial/gtk-2.0/gtkrc
/usr/share/themes/Mist/gtk-2.0/gtkrc
/usr/share/themes/Redmond/gtk-2.0/gtkrc
/usr/share/themes/ThinIce/gtk-2.0/gtkrc

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/2.10.0/engines/libclearlooks.so
/usr/lib64/gtk-2.0/2.10.0/engines/libcrux-engine.so
/usr/lib64/gtk-2.0/2.10.0/engines/libglide.so
/usr/lib64/gtk-2.0/2.10.0/engines/libhcengine.so
/usr/lib64/gtk-2.0/2.10.0/engines/libindustrial.so
/usr/lib64/gtk-2.0/2.10.0/engines/libmist.so
/usr/lib64/gtk-2.0/2.10.0/engines/libredmond95.so
/usr/lib64/gtk-2.0/2.10.0/engines/libthinice.so

%files locales -f gtk-engines.lang 
%defattr(-,root,root,-)

