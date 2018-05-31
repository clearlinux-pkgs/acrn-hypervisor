#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : acrn-hypervisor
Version  : 2018w22.4.163000p
Release  : 16
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w22.4-163000p.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w22.4-163000p.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0
Requires: acrn-hypervisor-bin
Requires: acrn-hypervisor-config
Requires: acrn-hypervisor-data
Requires: acpica-unix2
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : libevent-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev
BuildRequires : telemetrics-client-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains configuration files to ignore errors found in
the build and test process which are known to the developers and for
now can be safely ignored.

%package bin
Summary: bin components for the acrn-hypervisor package.
Group: Binaries
Requires: acrn-hypervisor-data
Requires: acrn-hypervisor-config

%description bin
bin components for the acrn-hypervisor package.


%package config
Summary: config components for the acrn-hypervisor package.
Group: Default

%description config
config components for the acrn-hypervisor package.


%package data
Summary: data components for the acrn-hypervisor package.
Group: Data

%description data
data components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-acrn-2018w22.4-163000p

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527765821
make  %{?_smp_mflags} all sbl-hypervisor

%install
export SOURCE_DATE_EPOCH=1527765821
rm -rf %{buildroot}
%make_install install sbl-hypervisor-install

%files
%defattr(-,root,root,-)
/usr/lib/acrn/acrn.efi
/usr/lib/acrn/acrn.sbl

%files bin
%defattr(-,root,root,-)
/usr/bin/acrn-dm
/usr/bin/acrnctl
/usr/bin/acrnlog
/usr/bin/acrnprobe
/usr/bin/acrnprobe_prepare.sh
/usr/bin/acrntrace
/usr/bin/debugger
/usr/bin/usercrash_c
/usr/bin/usercrash_s

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system.conf.d/40-watchdog.conf
/usr/lib/systemd/system/acrnprobe.service
/usr/lib/systemd/system/prepare.service
/usr/lib/systemd/system/usercrash.service

%files data
%defattr(-,root,root,-)
/usr/share/acrn/samples/apl-mrb/launch_uos.sh
/usr/share/acrn/samples/apl-mrb/sos_bootargs_debug.txt
/usr/share/acrn/samples/apl-mrb/sos_bootargs_release.txt
/usr/share/acrn/samples/nuc/acrn.conf
/usr/share/acrn/samples/nuc/bridge.sh
/usr/share/acrn/samples/nuc/launch_uos.sh
/usr/share/defaults/telemetrics/acrnprobe.xml
