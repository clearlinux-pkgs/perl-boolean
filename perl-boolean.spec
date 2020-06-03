#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-boolean
Version  : 0.46
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/boolean-0.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/boolean-0.46.tar.gz
Summary  : 'Boolean support for Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-boolean-license = %{version}-%{release}
Requires: perl-boolean-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
boolean - Boolean support for Perl
VERSION
This document describes boolean version 0.46.

%package dev
Summary: dev components for the perl-boolean package.
Group: Development
Provides: perl-boolean-devel = %{version}-%{release}
Requires: perl-boolean = %{version}-%{release}

%description dev
dev components for the perl-boolean package.


%package license
Summary: license components for the perl-boolean package.
Group: Default

%description license
license components for the perl-boolean package.


%package perl
Summary: perl components for the perl-boolean package.
Group: Default
Requires: perl-boolean = %{version}-%{release}

%description perl
perl components for the perl-boolean package.


%prep
%setup -q -n boolean-0.46
cd %{_builddir}/boolean-0.46

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-boolean
cp %{_builddir}/boolean-0.46/LICENSE %{buildroot}/usr/share/package-licenses/perl-boolean/c466e7fc80c07cdf28b43f8514a6ee652027a3d0
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/boolean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-boolean/c466e7fc80c07cdf28b43f8514a6ee652027a3d0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/boolean.pm
/usr/lib/perl5/vendor_perl/5.30.3/boolean.pod
