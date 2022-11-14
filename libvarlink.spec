%global _hardened_build 1

Name:           libvarlink
Version:        23
Release:        1
Summary:        Varlink C Library
License:        ASL 2.0 and BSD-3-Clause
URL:            https://github.com/varlink/libvarlink
Source0:        https://github.com/varlink/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glibc-langpack-de

%description
Varlink C Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libvarlink-devel package contains libraries and header files for
developing applications that use libvarlink.

%package        util
Summary:        Varlink command line tools

%description    util
The libvarlink-util package contains varlink command line tools.

%prep
%autosetup

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
%meson_test

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libvarlink.so.*

%files util
%{_bindir}/varlink
%{_datadir}/bash-completion/completions/varlink
%{_datadir}/vim/vimfiles/after/*

%files devel
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc

%changelog
* Wed Jun 08 2022 fushanqing <fushanqing@kylinos.cn> - 23-1
- update to 23

* Wed Jan 26 2022 fushanqing <fushanqing@kylinos.cn> - 21-1
- Initial package