%define		engine wgsmarty
Summary:	Drupal wgSmarty theme engine
Summary(pl):	Silnik motywów Drupala wgSmarty
Name:		drupal-themeengine-%{engine}
Version:	4.6.001
Release:	0.3
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

%define		_drupaldir	%{_datadir}/drupal
%define		_enginedir	%{_drupaldir}/themes/engines
%define		_cachedir	/var/cache/drupal

%description
wgSmarty is an implementation of the Smarty template engine as a theme
engine.

Advantages:
- Template files are easier to create and maintain then with
  PHPtemplate
- Templates are compiled into PHP to avoid speed and memory issues
  with search-and-replace template engines like XTemplate
- wgSmarty is much more closely integrated with Drupal than the
  existing Smarty theme engine

Disadvantages:
- wgSmarty is currently experimental and is only available in CVS
- There is very little support for wgSmarty: even when it is released,
  it will still be poorly supported in comparison with PHPTemplate

%description -l pl
wgSmarty to implementacja silnika szablonów Smarty jako silnika
motywów.

Zalety:
- pliki szablonów s± ³atwiejsze do tworzenia i utrzymywania ni¿
  PHPtemplate
- szablony s± kompilowane do PHP, aby zapobiec problemom z szybko¶ci±
  i pamiêci± z silnikami szablonów podmieniaj±cymi ³añcuchy, takimi
  jak XTemplate
- wgSmarty jest du¿o bli¿ej zintegrowany z Drupalem ni¿ istniej±cy
  silnik motywów Smarty

Wady:
- wgSmarty jest aktualnie eksperymentalny i dostêpny tylko w CVS-ie
- jest bardzo ma³e wsparcie dla wgSmarty: nawet kiedy zostanie wydany,
  nadal bêdzie kiepsko wspierany w porównaniu do PHPTemplate

%prep
%setup -q -n %{engine}
%patch0 -p1
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_enginedir}/%{engine},%{_cachedir}/%{engine}}

install *.engine *.php $RPM_BUILD_ROOT%{_enginedir}/%{engine}
cp -a plugins templates $RPM_BUILD_ROOT%{_enginedir}/%{engine}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_enginedir}/%{engine}
%dir %attr(775,root,http) %{_cachedir}/%{engine}
