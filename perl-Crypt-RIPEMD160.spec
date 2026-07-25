%define modname	Crypt-RIPEMD160
%define modver	0.14

Summary:	Crypt-RIPEMD160 module for perl 
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/cpan-authors/Crypt-RIPEMD160
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/Crypt-RIPEMD160-%{modver}.tar.gz
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
The %{modname} module/extension allows you to use the RIPEMD160 Message
Digest algorithm from within Perl programs.

%prep
%setup -qn %{modname}-%{modver}
perl -pi -e "s,/usr/local/bin/perl,%{_bindir}/perl," misc/ripemd160_driver.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
find misc -type f -exec chmod 0644 {} \;

%files
%doc README misc/*
%{perl_vendorlib}/*/Crypt/RIPEMD160
%{perl_vendorlib}/*/Crypt/RIPEMD160.pm
%{perl_vendorlib}/*/auto/Crypt/RIPEMD160
%{_mandir}/man3/*

