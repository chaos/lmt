Name: 
Version: 
Release: 

License: GPL
Group: Applications/System
Summary: Lustre Montitoring Tools Client
URL: http://sourceforge.net/projects/lmt/
Packager: Christopher J. Morrone <morrone2@llnl.gov>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ant, ant-nodeps
BuildRequires: mysql, mysql-devel
BuildRequires: cerebro >= 1.3-5
BuildRequires: ncurses-devel
%if 0%{?ch4}
BuildRequires: java-1.5.0-ibm-devel, java-1.5.0-ibm
BuildRequires: glibc >= 2.5-18
%else
BuildRequires: jre >= 1.4.2, java-devel >= 1.4.2
%endif
Requires: jre >= 1.4.2, ncurses
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%define lmtlibdir %{_datadir}/lmt/lib

%description
Lustre Monitoring Tools (LMT) Client

%prep
%setup

%build
%configure
make

%install
rm -rf   $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{lmtlibdir}

cp scripts/lwatch              $RPM_BUILD_ROOT%{_bindir}
cp scripts/lstat               $RPM_BUILD_ROOT%{_bindir}
cp scripts/ltop                $RPM_BUILD_ROOT%{_bindir}
cp lmt-complete.jar            $RPM_BUILD_ROOT%{lmtlibdir}/lmt-complete.jar
cp charva/c/lib/libTerminal.so $RPM_BUILD_ROOT%{lmtlibdir}/libTerminal.so
#rm -rf charva/c/lib/libTerminal.so.debug

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS DISCLAIMER COPYING
%{_bindir}/lwatch
%{_bindir}/lstat
%{_bindir}/ltop
%dir %{_datadir}/lmt
%dir %{lmtlibdir}
%attr(0644,root,root) %{lmtlibdir}/lmt-complete.jar
%attr(0644,root,root) %{lmtlibdir}/libTerminal.so
