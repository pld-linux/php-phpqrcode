%define		pkgname	phpqrcode
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP library for generating two-dimensional barcodes
Name:		php-%{pkgname}
Version:	1.1.4
Release:	1
License:	LGPL v3
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/phpqrcode/phpqrcode-2010100721_%{version}.zip
# Source0-md5:	64c2459b64b7efdb2e82fd714bbe03e7
Patch0:		cache-path.patch
URL:		http://phpqrcode.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(gd)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}
%define		_cachedir		/var/cache/php/%{pkgname}

%description
PHP QR Code is a library for generating QR Codes, 2-dimensional
barcodes. It is based on the libqrencode C library and provides an API
for creating QR Code barcode images (PNG and JPEG).

Some of the library features include:
- Supports QR Code versions (size) 1-40
- Numeric, Alphanumeric, 8-bit and Kanji encoding.
- Exports to PNG, JPEG images, also exports as bit-table
- TCPDF 2-D barcode API integration
- Easy to configure
- Data cache for calculation speed-up
- Debug data dump, error logging, time benchmarking

%prep
%setup -qc
mv phpqrcode/* .
%undos -f php CHANGELOG INSTALL README
%patch0 -p1

install -d examples
mv index.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_cachedir}}
# NOTE:
# phpqrcode.php is merged version of qr*.php files, see tools/merge.php
cp -a phpqrcode.php bindings $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL CHANGELOG
%{php_data_dir}/phpqrcode
%attr(730,root,http) %dir %verify(not group mode) /var/cache/php/phpqrcode
%{_examplesdir}/%{name}-%{version}
