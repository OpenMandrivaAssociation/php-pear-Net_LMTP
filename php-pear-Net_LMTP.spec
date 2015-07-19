%define	_class	Net
%define	_subclass	LMTP
%define	modname	%{_class}_%{_subclass}

Summary:	An implementation of the RFC2033 LMTP protocol
Name:		php-pear-%{modname}
Version:	1.0.2
Release:	9
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_LMTP/
Source0:	http://download.pear.php.net/package/Net_LMTP-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package provides an implementation of the RFC2033 LMTP using
PEAR's Net_Socket and Auth_SASL class.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/test_lmtp.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

