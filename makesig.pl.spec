%define name makesig.pl
%define version 0.0.9
%define release  11
%define summary A very flexible random signature generator

Name:			%name
Version:       		%version
Release:       		%release
Summary:		%summary
License:		GPLv2
Group:			Text tools
Url:			https://www.h.shuttle.de/mitch/makesig_pl.en.html
Source:			%name-%version.tar.bz2
Patch0:			makesig.pl.patch
BuildRoot:		%_tmppath/%name-buildroot
BuildArchitectures:	noarch

%description
makesig.pl is a very flexible random signature generator for those who
don't fear the power of the command line. It comes together with some
tools to format your signature. makesig.pl can also read fortune files.

%prep
rm -rf $RPM_BUILD_ROOT
%setup
%patch0 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
cp makesig.pl $RPM_BUILD_ROOT%_bindir
cp tools/*.pl $RPM_BUILD_ROOT%_bindir

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
%{_bindir}/*
%defattr(0755,root,root)
%doc HISTORY COPYING tools/README.tools examples/README.makesig examples/README.examples examples/asciiart.txt examples/background.txt examples/demo.txt examples/left.conf examples/moresigs.txt examples/right.conf examples/somesigs.txt examples/tools.sh



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-10mdv2011.0
+ Revision: 612806
- the mass rebuild of 2010.1 packages

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.0.9-9mdv2010.1
+ Revision: 513154
- del patch who was unpacking
- Unpacking the patch
- fix license

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.9-8mdv2010.0
+ Revision: 429949
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.0.9-7mdv2009.0
+ Revision: 251813
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.0.9-5mdv2008.1
+ Revision: 129645
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import makesig.pl


* Tue Oct 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-5mdk
- rebuild

* Mon Sep 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-4mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-3mdk
- rebuild

* Tue Aug 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-2mdk
- rebuild

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-1mdk
- updated to 0.0.9
- refresh patch

* Fri Nov 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-1mdk
- updated to 0.0.7

* Mon Nov 06 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.4-1mdk
- used srpm from Guillaume Rousse <g.rousse@linux-mandrake.com> :
	first Mandrake release

