%define upstream_name    Crypt-RIPEMD160
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
