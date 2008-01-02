%define name makesig.pl
%define version 0.0.9
%define release  %mkrel 5
%define summary A very flexible random signature generator

Name:			%name
Version:       		%version
Release:       		%release
Summary:		%summary
License:		GPL
Group:			Text tools
Url:			http://www.h.shuttle.de/mitch/makesig_pl.en.html
Source:			%name-%version.tar.bz2
Patch:			makesig.pl.patch.bz2
BuildRoot:		%_tmppath/%name-buildroot
BuildArchitectures:	noarch

%description
makesig.pl is a very flexible random signature generator for those who
don't fear the power of the command line. It comes together with some
tools to format your signature. makesig.pl can also read fortune files.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch -p1

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

