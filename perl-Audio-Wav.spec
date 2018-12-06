#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Audio-Wav
Version  : 0.14
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/Audio-Wav-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/Audio-Wav-0.14.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libaudio-wav-perl/libaudio-wav-perl_0.14-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Audio-Wav-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
---------------------------------------------------------------------
---------------------------------------------------------------------

%package dev
Summary: dev components for the perl-Audio-Wav package.
Group: Development
Provides: perl-Audio-Wav-devel = %{version}-%{release}

%description dev
dev components for the perl-Audio-Wav package.


%package license
Summary: license components for the perl-Audio-Wav package.
Group: Default

%description license
license components for the perl-Audio-Wav package.


%prep
%setup -q -n Audio-Wav-0.14
cd ..
%setup -q -T -D -n Audio-Wav-0.14 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Audio-Wav-0.14/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Audio-Wav
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Audio-Wav/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Audio-Wav/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1Audio/Wav.pm
/usr/lib/perl5/vendor_perl/5.28.1Audio/Wav/Read.pm
/usr/lib/perl5/vendor_perl/5.28.1Audio/Wav/Tools.pm
/usr/lib/perl5/vendor_perl/5.28.1Audio/Wav/Write.pm
/usr/lib/perl5/vendor_perl/5.28.1Audio/Wav/Write/Header.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Audio::Wav.3
/usr/share/man/man3/Audio::Wav::Read.3
/usr/share/man/man3/Audio::Wav::Write.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Audio-Wav/LICENSE
/usr/share/package-licenses/perl-Audio-Wav/deblicense_copyright
