#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : acrn-hypervisor
Version  : 2019w14.1.140000p
Release  : 179
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2019w14.1-140000p.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2019w14.1-140000p.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0 ISC
Requires: acrn-hypervisor-autostart = %{version}-%{release}
Requires: acrn-hypervisor-bin = %{version}-%{release}
Requires: acrn-hypervisor-config = %{version}-%{release}
Requires: acrn-hypervisor-data = %{version}-%{release}
Requires: acrn-hypervisor-license = %{version}-%{release}
Requires: acrn-hypervisor-services = %{version}-%{release}
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

%package autostart
Summary: autostart components for the acrn-hypervisor package.
Group: Default

%description autostart
autostart components for the acrn-hypervisor package.


%package bin
Summary: bin components for the acrn-hypervisor package.
Group: Binaries
Requires: acrn-hypervisor-data = %{version}-%{release}
Requires: acrn-hypervisor-config = %{version}-%{release}
Requires: acrn-hypervisor-license = %{version}-%{release}
Requires: acrn-hypervisor-services = %{version}-%{release}

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
Requires: acrn-hypervisor-bin = %{version}-%{release}
Requires: acrn-hypervisor-data = %{version}-%{release}
Provides: acrn-hypervisor-devel = %{version}-%{release}

%description dev
dev components for the acrn-hypervisor package.


%package extras
Summary: extras components for the acrn-hypervisor package.
Group: Default

%description extras
extras components for the acrn-hypervisor package.


%package license
Summary: license components for the acrn-hypervisor package.
Group: Default

%description license
license components for the acrn-hypervisor package.


%package services
Summary: services components for the acrn-hypervisor package.
Group: Systemd services

%description services
services components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-acrn-2019w14.1-140000p

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554129128
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags} all sbl-hypervisor BUILD_VERSION=”%{version}_%{release}” BUILD_TAG=”%{version}”


%install
export SOURCE_DATE_EPOCH=1554129128
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/acrn-hypervisor
cp LICENSE %{buildroot}/usr/share/package-licenses/acrn-hypervisor/LICENSE
cp doc/LICENSE %{buildroot}/usr/share/package-licenses/acrn-hypervisor/doc_LICENSE
cp scripts/kconfig/LICENSE.kconfiglib %{buildroot}/usr/share/package-licenses/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
cp tools/acrn-crashlog/license_header %{buildroot}/usr/share/package-licenses/acrn-hypervisor/tools_acrn-crashlog_license_header
%make_install sbl-hypervisor-install hypervisor-install-debug sbl-hypervisor-install-debug
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../acrnd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/acrnd.service
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/acrnd.service %{buildroot}/usr/share/clr-service-restart/acrnd.service
mkdir -p %{buildroot}/usr/share/acrn/conf/add
ln -s ../../samples/apl-mrb/launch_uos.args %{buildroot}/usr/share/acrn/conf/add/vm1.args
ln -s ../../samples/apl-mrb/launch_uos.sh %{buildroot}/usr/share/acrn/conf/add/vm1.sh
## install_append end

%files
%defattr(-,root,root,-)
%exclude /usr/lib/acrn/acrn.efi.map
%exclude /usr/lib/acrn/acrn.efi.out
%exclude /usr/lib/acrn/acrn.sbl.map
%exclude /usr/lib/acrn/acrn.sbl.out
/usr/lib/acrn/acrn.apl-up2.sbl
/usr/lib/acrn/acrn.apl-up2.sbl.map
/usr/lib/acrn/acrn.apl-up2.sbl.out
/usr/lib/acrn/acrn.efi
/usr/lib/acrn/acrn.sbl
/usr/lib/systemd/network/50-acrn.netdev
/usr/lib/systemd/network/50-acrn.network
/usr/lib/systemd/network/50-acrn_tap0.netdev
/usr/lib/systemd/network/50-eth.network

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/acrnd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/acrn-dm
/usr/bin/acrnctl
/usr/bin/acrnd
/usr/bin/acrnlog
/usr/bin/acrnprobe
/usr/bin/acrntrace
/usr/bin/crashlogctl
/usr/bin/debugger
/usr/bin/usercrash-wrapper
/usr/bin/usercrash_c
/usr/bin/usercrash_s

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/acrn-crashlog-dirs.conf

%files data
%defattr(-,root,root,-)
/usr/share/acrn/bios/MD5SUM_ovmf
/usr/share/acrn/bios/MD5SUM_vsbl
/usr/share/acrn/bios/OVMF.fd
/usr/share/acrn/bios/OVMF_debug.fd
/usr/share/acrn/bios/SHA512SUM_ovmf
/usr/share/acrn/bios/SHA512SUM_vsbl
/usr/share/acrn/bios/VSBL.bin
/usr/share/acrn/bios/VSBL_debug.bin
/usr/share/acrn/bios/changelog_ovmf.txt
/usr/share/acrn/bios/changelog_vsbl.txt
/usr/share/acrn/conf/add/vm1.args
/usr/share/acrn/conf/add/vm1.sh
/usr/share/acrn/crashlog/40-watchdog.conf
/usr/share/acrn/crashlog/80-coredump.conf
/usr/share/acrn/samples/apl-mrb/acrn_guest.service
/usr/share/acrn/samples/apl-mrb/launch_uos.args
/usr/share/acrn/samples/apl-mrb/launch_uos.sh
/usr/share/acrn/samples/apl-mrb/mrb-env-setup.sh
/usr/share/acrn/samples/apl-mrb/runC.json
/usr/share/acrn/samples/apl-mrb/sos_bootargs_debug.txt
/usr/share/acrn/samples/apl-mrb/sos_bootargs_release.txt
/usr/share/acrn/samples/apl-up2/launch_uos.sh
/usr/share/acrn/samples/apl-up2/sos_bootargs_debug.txt
/usr/share/acrn/samples/apl-up2/sos_bootargs_release.txt
/usr/share/acrn/samples/nuc/acrn.conf
/usr/share/acrn/samples/nuc/launch_hard_rt_vm.sh
/usr/share/acrn/samples/nuc/launch_uos.sh
/usr/share/acrn/samples/nuc/launch_zephyr.sh
/usr/share/acrn/samples/nuc/runC.json
/usr/share/clr-service-restart/acrnd.service
/usr/share/defaults/telemetrics/acrnprobe.xml

%files dev
%defattr(-,root,root,-)
/usr/include/acrn/acrn_mngr.h
/usr/lib64/*.a

%files extras
%defattr(-,root,root,-)
/usr/lib/acrn/acrn.efi.map
/usr/lib/acrn/acrn.efi.out
/usr/lib/acrn/acrn.sbl.map
/usr/lib/acrn/acrn.sbl.out

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/acrn-hypervisor/LICENSE
/usr/share/package-licenses/acrn-hypervisor/doc_LICENSE
/usr/share/package-licenses/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
/usr/share/package-licenses/acrn-hypervisor/tools_acrn-crashlog_license_header

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/acrnd.service
/usr/lib/systemd/system/acrn_guest.service
/usr/lib/systemd/system/acrnd.service
/usr/lib/systemd/system/acrnlog.service
/usr/lib/systemd/system/acrnprobe.service
/usr/lib/systemd/system/usercrash.service
