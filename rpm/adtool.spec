## Define global settings
%global _hardened_build 1
%global major_version 1
%global minor_version 3
%global micro_version 3

Name:		adtool
Version:	%{major_version}.%{minor_version}.%{micro_version}
Release:	2%{?dist}
Summary:	Active Directory administration utility for Unix

License:	GPLv2
URL:		http://gp2x.org/adtool
Source0:	https://gp2x.org/adtool/adtool-%{major_version}.%{minor_version}.%{micro_version}.tar.gz

BuildRequires:	openldap-devel
BuildRequires:	openssl
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:  make
BuildRequires:  tar
Requires:	openldap
Requires:	openssl

%description
adtool is a unix command line utility for Active Directory administration.

Features include user and group creation, deletion, modification, password setting and directory query and search capabilities. 

%prep
%setup -q

%build
%configure --sysconfdir=%{_sysconfdir}/%{name}
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%defattr(-, root, root, -)
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Oct 29 2020 Louis Abel <tucklesepk@gmail.com> - 1.3.3-2
- Fixing failing fedora builds

* Fri May 31 2019 Louis Abel <tucklesepk@gmail.com> - 1.3.3-1
- Initial release of adtool to copr

