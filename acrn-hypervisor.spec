#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : acrn-hypervisor
Version  : 2020w18.4.140000p
Release  : 284
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2020w18.4-140000p.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2020w18.4-140000p.tar.gz
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
BuildRequires : acpica-unix2
BuildRequires : e2fsprogs-dev
BuildRequires : gdb
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : libevent-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev
BuildRequires : numactl-dev
BuildRequires : pip
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-kconfiglib
BuildRequires : python3
BuildRequires : systemd-dev
BuildRequires : telemetrics-client
BuildRequires : telemetrics-client-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
folder structure
Kconfig		: Select working scenario and target board, configure ACRN hypervisor capabilities and features.
target		: Get target board information under native Linux environment and generate board_info XML.
board_config	: Parse board_info XML and scenario XML to generate board related configuration files under misc/acrn-config/xmls/board-xmls/ folder.
scenario_config	: Parse board_info XML and scenario XML to generate scenario based VM configuration files under misc/acrn-config/xmls/config-xmls/$(BOARD)/ folder.
launch_config	: Parse board_info XML, scenario XML and devicemodel param XML to generate launch script for post-launched vm under misc/acrn-config/xmls/config-xmls/$(BOARD)/ folder.
library		: The folder stores shared software modules or libs for acrn-config offline tool.

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
Requires: acrn-hypervisor = %{version}-%{release}

%description dev
dev components for the acrn-hypervisor package.


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


%package staticdev
Summary: staticdev components for the acrn-hypervisor package.
Group: Default
Requires: acrn-hypervisor-dev = %{version}-%{release}

%description staticdev
staticdev components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-acrn-2020w18.4-140000p
cd %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588238758
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  RELEASE=0 all sbl-hypervisor BUILD_VERSION=%{version}_%{release} BUILD_TAG=acrn-%{version}


%install
export SOURCE_DATE_EPOCH=1588238758
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/acrn-hypervisor
cp %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p/LICENSE %{buildroot}/usr/share/package-licenses/acrn-hypervisor/3cc9b5c24d3ab78578359aa1b98166ee5cf6df9b
cp %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p/doc/LICENSE %{buildroot}/usr/share/package-licenses/acrn-hypervisor/50862f16be94cd4a0162ee82eb55697c5b54c70e
cp %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p/misc/acrn-config/kconfig/LICENSE.kconfiglib %{buildroot}/usr/share/package-licenses/acrn-hypervisor/0256be14ad1f607cb4bd89d716442115dab0294c
cp %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p/misc/acrn-config/library/hypervisor_license %{buildroot}/usr/share/package-licenses/acrn-hypervisor/e769dc34d30330fcb407f27559c817e502fdfb13
cp %{_builddir}/acrn-hypervisor-acrn-2020w18.4-140000p/misc/tools/acrn-crashlog/license_header %{buildroot}/usr/share/package-licenses/acrn-hypervisor/b63d865a65562d341e07541b47e5b542a3e2ca67
%make_install RELEASE=0 sbl-hypervisor-install hypervisor-install-debug sbl-hypervisor-install-debug
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
/usr/lib/acrn/acrn.apl-mrb.sbl.sdc.32.out
/usr/lib/acrn/acrn.apl-mrb.sbl.sdc.map
/usr/lib/acrn/acrn.apl-mrb.sbl.sdc.out
/usr/lib/acrn/acrn.apl-up2.hybrid.efi
/usr/lib/acrn/acrn.apl-up2.hybrid.efi.map
/usr/lib/acrn/acrn.apl-up2.hybrid.efi.out
/usr/lib/acrn/acrn.apl-up2.sbl.sdc.32.out
/usr/lib/acrn/acrn.apl-up2.sbl.sdc.map
/usr/lib/acrn/acrn.apl-up2.sbl.sdc.out
/usr/lib/acrn/acrn.apl-up2.uefi.hybrid.32.out
/usr/lib/acrn/acrn.apl-up2.uefi.hybrid.map
/usr/lib/acrn/acrn.apl-up2.uefi.hybrid.out
/usr/lib/acrn/acrn.nuc7i7dnb.industry.efi
/usr/lib/acrn/acrn.nuc7i7dnb.industry.efi.map
/usr/lib/acrn/acrn.nuc7i7dnb.industry.efi.out
/usr/lib/acrn/acrn.nuc7i7dnb.sdc.efi
/usr/lib/acrn/acrn.nuc7i7dnb.sdc.efi.map
/usr/lib/acrn/acrn.nuc7i7dnb.sdc.efi.out
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.industry.32.out
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.industry.map
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.industry.out
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.sdc.32.out
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.sdc.map
/usr/lib/acrn/acrn.nuc7i7dnb.uefi.sdc.out
/usr/lib/systemd/network/50-acrn.netdev
/usr/lib/systemd/network/50-acrn.network
/usr/lib/systemd/network/50-eth.network
/usr/lib/systemd/network/50-tap0.netdev

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
/usr/share/acrn/samples/apl-mrb/runC.json
/usr/share/acrn/samples/apl-up2/launch_uos.sh
/usr/share/acrn/samples/nuc/acrn.conf
/usr/share/acrn/samples/nuc/launch_hard_rt_vm.sh
/usr/share/acrn/samples/nuc/launch_uos.sh
/usr/share/acrn/samples/nuc/launch_vxworks.sh
/usr/share/acrn/samples/nuc/launch_win.sh
/usr/share/acrn/samples/nuc/launch_zephyr.sh
/usr/share/acrn/samples/nuc/runC.json
/usr/share/clr-service-restart/acrnd.service
/usr/share/defaults/telemetrics/acrnprobe.xml

%files dev
%defattr(-,root,root,-)
/usr/include/acrn/acrn_common.h
/usr/include/acrn/acrn_mngr.h
/usr/include/acrn/dm.h
/usr/include/acrn/dm_string.h
/usr/include/acrn/macros.h
/usr/include/acrn/types.h
/usr/include/acrn/vhm_ioctl_defs.h
/usr/include/acrn/vmm.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/acrn-hypervisor/0256be14ad1f607cb4bd89d716442115dab0294c
/usr/share/package-licenses/acrn-hypervisor/3cc9b5c24d3ab78578359aa1b98166ee5cf6df9b
/usr/share/package-licenses/acrn-hypervisor/50862f16be94cd4a0162ee82eb55697c5b54c70e
/usr/share/package-licenses/acrn-hypervisor/b63d865a65562d341e07541b47e5b542a3e2ca67
/usr/share/package-licenses/acrn-hypervisor/e769dc34d30330fcb407f27559c817e502fdfb13

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/acrnd.service
/usr/lib/systemd/system/acrn_guest.service
/usr/lib/systemd/system/acrnd.service
/usr/lib/systemd/system/acrnlog.service
/usr/lib/systemd/system/acrnprobe.service
/usr/lib/systemd/system/usercrash.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libacrn-mngr.a
