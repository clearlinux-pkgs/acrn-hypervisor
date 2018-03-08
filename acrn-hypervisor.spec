#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : acrn-hypervisor
Version  : 1.0
Release  : 4
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/v1.0.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/v1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: acrn-hypervisor-data
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Embedded-Hypervisor
###################
This open source embedded hypervisor defines a software architecture for
running multiple software subsystems managed securely on a consolidated
system (by means of a virtual machine manager), and defines a reference
framework Device Model implementation for devices emulation

%package data
Summary: data components for the acrn-hypervisor package.
Group: Data

%description data
data components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520523227
make  %{?_smp_mflags} PLATFORM=uefi

%install
export SOURCE_DATE_EPOCH=1520523227
rm -rf %{buildroot}
%make_install PLATFORM=uefi

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/acrn/acrn.efi
/usr/share/acrn/demo/acrn.conf
