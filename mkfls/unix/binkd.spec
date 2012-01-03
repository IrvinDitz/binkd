Summary: Binkd - the binkp daemon
Name: binkd
Version: 0.9.12
Release: g1
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL: ftp://happy.kiev.ua/pub/fidosoft/mailer/binkd/
Provides: binkd
Requires: 
BuildRoot: /var/tmp/%{name}-%{version}-root
Group: Applications/Internet

%description
Binkd is the daemon for FTN communications over reliable links.

%prep
%setup -q -n %{name}-%{version}
cp -p mkfls/unix/{Makefile*,configure*,install-sh,mkinstalldirs} .

%build
%configure \
        --prefix=%{_prefix} \
        --sysconfdir=%{_sysconfdir} \
        --localstatedir=%{_localstatedir} \
        --with-https --with-ntlm 
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
# fix for stupid symlink creation
rm $RPM_BUILD_ROOT%{_prefix}/sbin/binkd
ln -s `basename $RPM_BUILD_ROOT%{_prefix}/sbin/binkd*` \
        $RPM_BUILD_ROOT%{_prefix}/sbin/binkd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog
* Tue Mar 25 2008 Gremlin from Kremlin <gremlin-at-owl.openwall.com> 0.9.9
- first build
