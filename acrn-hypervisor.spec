#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : acrn-hypervisor
Version  : 2018w39.2.140000p
Release  : 92
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w39.2-140000p.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w39.2-140000p.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0 ISC
Requires: acrn-hypervisor-bin
Requires: acrn-hypervisor-config
Requires: acrn-hypervisor-data
Requires: acrn-hypervisor-license
Requires: acpica-unix2
Requires: e2fsprogs-extras
Requires: gdb
Requires: telemetrics-client
BuildRequires : e2fsprogs-dev
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : libevent-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev
BuildRequires : pip
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-kconfiglib
BuildRequires : python3
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
Requires: acrn-hypervisor-license

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


%package dev
Summary: dev components for the acrn-hypervisor package.
Group: Development
Requires: acrn-hypervisor-bin
Requires: acrn-hypervisor-data
Provides: acrn-hypervisor-devel

%description dev
dev components for the acrn-hypervisor package.


%package license
Summary: license components for the acrn-hypervisor package.
Group: Default

%description license
license components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-acrn-2018w39.2-140000p

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537871176
make  %{?_smp_mflags} all sbl-hypervisor BUILD_VERSION=”%{version}_%{release}” BUILD_TAG=”%{version}”

%install
export SOURCE_DATE_EPOCH=1537871176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/acrn-hypervisor
cp LICENSE %{buildroot}/usr/share/doc/acrn-hypervisor/LICENSE
cp doc/LICENSE %{buildroot}/usr/share/doc/acrn-hypervisor/doc_LICENSE
cp scripts/kconfig/LICENSE.kconfiglib %{buildroot}/usr/share/doc/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
cp tools/acrn-crashlog/license_header %{buildroot}/usr/share/doc/acrn-hypervisor/tools_acrn-crashlog_license_header
%make_install sbl-hypervisor-install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
mkdir -p %{buildroot}/usr/share/clr-service-restart
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/acrn/acrn.efi
/usr/lib/acrn/acrn.sbl

%files bin
%defattr(-,root,root,-)
/usr/bin/acrn-dm
/usr/bin/acrnctl
/usr/bin/acrnd
/usr/bin/acrnlog
/usr/bin/acrntrace

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/network/50-acrn.netdev
/usr/lib/systemd/network/50-acrn.network
/usr/lib/systemd/network/50-acrn_tap0.netdev
/usr/lib/systemd/network/50-eth.network
/usr/lib/systemd/system/acrn_guest.service
/usr/lib/systemd/system/acrnd.service
/usr/lib/systemd/system/acrnlog.service

%files data
%defattr(-,root,root,-)
/usr/share/acrn/bios/MD5SUM
/usr/share/acrn/bios/SHA512SUM
/usr/share/acrn/bios/VSBL.bin
/usr/share/acrn/bios/VSBL_debug.bin
/usr/share/acrn/bios/changelog.txt
/usr/share/acrn/samples/apl-mrb/acrn_guest.service
/usr/share/acrn/samples/apl-mrb/launch_uos.sh
/usr/share/acrn/samples/apl-mrb/sos_bootargs_debug.txt
/usr/share/acrn/samples/apl-mrb/sos_bootargs_release.txt
/usr/share/acrn/samples/nuc/acrn.conf
/usr/share/acrn/samples/nuc/launch_uos.sh

%files dev
%defattr(-,root,root,-)
/usr/include/acrn/acrn_mngr.h
/usr/lib64/*.a

%files license
%defattr(-,root,root,-)
/usr/share/doc/acrn-hypervisor/LICENSE
/usr/share/doc/acrn-hypervisor/doc_LICENSE
/usr/share/doc/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
/usr/share/doc/acrn-hypervisor/tools_acrn-crashlog_license_header
