%define version 1.0.0
%define python python3
%define prefix  /opt/horizondaas/
%define logpath /var/log/horizondaas
%define _python_bytecompile_errors_terminate_build 0

Name:		DAM-pamola-horizondaas
Version:	%{version}
Release:	1%{?dist}

License:	Apache-2.0
Packager:	terje.nomeland@basefarm.com
URL:            https://basefarm.com/

Source0:        file:///home/tjnome/SOURCE/DAM-pamola-horizondaas-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_topdir}/BUILDROOT/%{name}-%{version}
Provides:       pamola-horizondaas
Requires:       DAM-pamola-filesystem
AutoReqProv:    no

Summary:        VMware CIM CLI Horizon tool to be used with Pamola.

%description
VMware CIM CLI Horizon tool to be used with Pamola.
 
%changelog
* Thu Mar 26 2020 terje.nomeland@basefarm.com - 1.0.0
- First release version
* Thu Mar 26 2020 terje.nomeland@basefarm.com - 0.0.6
- Fix for float value
* Wed Mar 25 2020 terje.nomeland@basefarm.com - 0.0.5
- Bug fixes
* Mon Mar 23 2020 terje.nomeland@basefarm.com - 0.0.4
- New way to package and pip install
* Wed Mar 11 2020 terje.nomeland@basefarm.com - 0.0.3
- New class to handle metric
* Mon Mar 09 2020 terje.nomeland@basefarm.com - 0.0.2
- First tested release
* Tue Feb 25 2020 terje.nomeland@basefarm.com - 0.0.1
- Initial Packaging
 
%prep
%setup -q
 
%install
%__mkdir_p %{buildroot}%{prefix}/bin/
%__mkdir_p %{buildroot}%{prefix}/etc/
%__mkdir_p %{buildroot}%{prefix}/venv/
%__mkdir_p %{buildroot}%{logpath}
cp %{_builddir}/%{name}-%{version}/bin/horizondaas %{buildroot}%{prefix}/bin/
cp %{_builddir}/%{name}-%{version}/etc/horizondaas-example.yml %{buildroot}%{prefix}/etc/
 
%{python} -m venv %{_builddir}/%{name}-%{version}/venv/
source %{_builddir}/%{name}-%{version}/venv/bin/activate
pip install --upgrade pip
pip install pywbem
pip install PyYAML
pip install influxdb
deactivate

cp -r %{_builddir}/%{name}-%{version}/venv/ %{buildroot}%{prefix}/

%clean
rm -rf %{buildroot}
 
%files
%attr(  755,  root,  root )                %{prefix}/bin/horizondaas
%attr(  444,  root,  root )                %{prefix}/etc/horizondaas-example.yml
%attr(  755,  root,  root )                %{prefix}/venv/
%attr(  2755,  telegraf,  telegraf ) %dir  %{logpath}/
