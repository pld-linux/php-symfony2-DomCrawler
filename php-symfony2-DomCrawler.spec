%define		package	DomCrawler
%define		php_min_version 5.3.9
Summary:	Symfony2 DomCrawler Component
Name:		php-symfony2-DomCrawler
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	0c955bdddd6da73bcd370f77e39a2606
URL:		http://symfony.com/doc/2.7/components/dom_crawler.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-dirs >= 1.6
Suggests:	php-symfony2-CssSelector
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DomCrawler Component eases DOM navigation for HTML and XML
documents.

While possible, the DomCrawler component is not designed for
manipulation of the DOM or re-dumping HTML/XML.

%prep
%setup -q -n dom-crawler-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/DomCrawler
%{php_data_dir}/Symfony/Component/DomCrawler/*.php
%{php_data_dir}/Symfony/Component/DomCrawler/Field
