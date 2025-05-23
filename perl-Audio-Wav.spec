#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Audio-Wav
Version  : 0.14
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/Audio-Wav-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/Audio-Wav-0.14.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libaudio-wav-perl/libaudio-wav-perl_0.14-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Audio-Wav-license = %{version}-%{release}
Requires: perl-Audio-Wav-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
---------------------------------------------------------------------
---------------------------------------------------------------------

%package dev
Summary: dev components for the perl-Audio-Wav package.
Group: Development
Provides: perl-Audio-Wav-devel = %{version}-%{release}
Requires: perl-Audio-Wav = %{version}-%{release}

%description dev
dev components for the perl-Audio-Wav package.


%package license
Summary: license components for the perl-Audio-Wav package.
Group: Default

%description license
license components for the perl-Audio-Wav package.


%package perl
Summary: perl components for the perl-Audio-Wav package.
Group: Default
Requires: perl-Audio-Wav = %{version}-%{release}

%description perl
perl components for the perl-Audio-Wav package.


%prep
%setup -q -n Audio-Wav-0.14
cd %{_builddir}
tar xf %{_sourcedir}/libaudio-wav-perl_0.14-2.debian.tar.xz
cd %{_builddir}/Audio-Wav-0.14
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Audio-Wav-0.14/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Audio-Wav
cp %{_builddir}/Audio-Wav-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Audio-Wav/18a0f2e0e480f900e610b2f16564eba70f8aede9 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Audio-Wav/b47851d8af6d6bcbaafd6032d3491eb65c95036c || :
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
/usr/share/man/man3/Audio::Wav.3
/usr/share/man/man3/Audio::Wav::Read.3
/usr/share/man/man3/Audio::Wav::Write.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Audio-Wav/18a0f2e0e480f900e610b2f16564eba70f8aede9
/usr/share/package-licenses/perl-Audio-Wav/b47851d8af6d6bcbaafd6032d3491eb65c95036c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
