%define real_name Crypt-RIPEMD160

Summary:	Crypt-RIPEMD160 module for perl 
Name:		perl-%{real_name}
Version:	0.04
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel

%description
The %{real_name} module/extension allows you to use the RIPEMD160 Message
Digest algorithm from within Perl programs.

%prep
%setup -q -n %{real_name}-%{version} 
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


