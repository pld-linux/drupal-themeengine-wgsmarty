%define		modname wgsmarty
Summary:	Drupal wgSmarty theme engine
Name:		drupal-themeengine-%{modname}
Version:	4.6.001
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/webg8/wgsmarty-cvs.tar.gz
# Source0-md5:	bb289aa9808ff90f3fd3a85a34dbe0be
Patch0:		%{name}-PLD.patch
URL:		http://drupal.org/node/26897
Requires:	Smarty >= 2.6.2
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enginedir			%{_datadir}/drupal/themes/engines
%define		_cachedir			/var/cache/drupal

%description
wgSmarty is an implementation of the Smarty template engine as a theme
engine.

Advantages
- Template files are easier to create and maintain then with PHPtemplate
- Templates are compiled into PHP to avoid speed and memory issues
  with search-and-replace template engines like XTemplate
- wgSmarty is much more closely integrated with Drupal than the
  existing smarty theme engine

Disadvantages
- wgSmarty is currently experimental and is only available in CVS
- There is very little support for wgSmarty: even when it is released,
  it will still be poorly supported in comparison with PHPTemplate

%prep
%setup -q -n %{modname}
%patch0 -p1
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_enginedir}/%{modname},%{_cachedir}/%{modname}}

install *.engine *.php $RPM_BUILD_ROOT%{_enginedir}/%{modname}
cp -a plugins templates $RPM_BUILD_ROOT%{_enginedir}/%{modname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_enginedir}/%{modname}
%dir %attr(775,root,http) %{_cachedir}/%{modname}