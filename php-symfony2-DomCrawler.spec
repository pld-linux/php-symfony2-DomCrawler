%define		pearname	DomCrawler
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 DomCrawler Component
Name:		php-symfony2-DomCrawler
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	053ef008f19879b001bdf83b5f6f38b2
URL:		http://symfony.com/doc/2.4/components/dom_crawler.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-CssSelector
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DomCrawler Component eases DOM navigation for HTML and XML
documents.

While possible, the DomCrawler component is not designed for
manipulation of the DOM or re-dumping HTML/XML.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/DomCrawler
%{php_pear_dir}/Symfony/Component/DomCrawler/*.php
%{php_pear_dir}/Symfony/Component/DomCrawler/Field
