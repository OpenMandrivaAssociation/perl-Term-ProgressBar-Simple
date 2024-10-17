%define upstream_name    Term-ProgressBar-Simple
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Simpler progress bars
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Term::ProgressBar::Quiet)
BuildArch:	noarch

%description
Progress bars are handy - they tell you how much work has been done, how
much is left to do and estimate how long it will take.

But they can be fiddly!

This module does the right thing in almost all cases in a really convenient
way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 654304
- rebuild for updated spec-helper

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 485960
- import perl-Term-ProgressBar-Simple


* Sun Jan 03 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
