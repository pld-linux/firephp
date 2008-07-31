# TODO
# - make it generic for gecko based browsers (browser-plugins should first support this)
#   call it one of: (RFC welcome)
#   - browser-extension-gecko-firephp
#   - gecko-addon-firephp
#   - gecko-extension-firephp
#   - mozilla-extension-firephp
#   - mozilla-addon-firephp
Summary:	Firefox Extension for FirePHP
Name:		firephp
Version:	0.1.0
Release:	0.1
License:	New BSD License
Group:		Development/Languages/PHP
URL:		https://addons.mozilla.org/en-US/firefox/addon/6149
BuildRequires:	sed >= 4.0
Source0:	http://www.firephp.org/DownloadRelease/FirePHP-FirefoxExtension-%{version}
# Source0-md5:	7546aedfb63f1fa5213fb99629cc5077
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		extensiondir	%{_datadir}/mozilla-firefox/extensions/firephp

%description
FirePHP enables you to print to your Firebug Console using a simple
PHP function call.

You must have Firebug installed and the "Net" panel enabled to use
this extension.

%prep
%setup -qc
%{__sed} -i -e 's,\r$,,' update.rdf.tpl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensiondir}
cp -a chrome.manifest install.rdf update.rdf.tpl chrome $RPM_BUILD_ROOT%{extensiondir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%dir %{extensiondir}
%{extensiondir}/chrome
%{extensiondir}/install.rdf
%{extensiondir}/update.rdf.tpl
%{extensiondir}/chrome.manifest
