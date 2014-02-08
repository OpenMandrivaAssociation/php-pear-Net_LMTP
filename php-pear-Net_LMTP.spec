%define		_class		Net
%define		_subclass	LMTP
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	2
Summary:	An implementation of the RFC2033 LMTP protocol
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LMTP/
Source0:	http://download.pear.php.net/package/Net_LMTP-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package provides an implementation of the RFC2033 LMTP using
PEAR's Net_Socket and Auth_SASL class.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/test_lmtp.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-13mdv2011.0
+ Revision: 667629
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-12mdv2011.0
+ Revision: 607124
- rebuild

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-11mdv2010.1
+ Revision: 468709
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-10mdv2010.0
+ Revision: 426660
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2009.1
+ Revision: 321883
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 224782
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2008.1
+ Revision: 178528
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2007.0
+ Revision: 81178
- Import php-pear-Net_LMTP

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- new group (Development/PHP)

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package (PLD import)


