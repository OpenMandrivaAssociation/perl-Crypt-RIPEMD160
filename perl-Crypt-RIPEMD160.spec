%define upstream_name    Crypt-RIPEMD160
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Crypt-RIPEMD160 module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The %{upstream_name} module/extension allows you to use the RIPEMD160 Message
Digest algorithm from within Perl programs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e "s,/usr/local/bin/perl,%{_bindir}/perl," misc/ripemd160_driver.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std
find misc -type f -exec chmod 0644 {} \;

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README misc/*
%{perl_vendorlib}/*/Crypt/RIPEMD160
%{perl_vendorlib}/*/Crypt/RIPEMD160.pm
%{perl_vendorlib}/*/auto/Crypt/RIPEMD160
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-6mdv2012.0
+ Revision: 765135
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-5
+ Revision: 763649
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-4
+ Revision: 676728
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3
+ Revision: 676705
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-2
+ Revision: 676624
- rebuild

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1
+ Revision: 654039
- update to new version 0.05

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 555722
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 403039
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.04-4mdv2009.0
+ Revision: 256342
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2008.1
+ Revision: 152042
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.04-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdk
- initial Mandriva package

