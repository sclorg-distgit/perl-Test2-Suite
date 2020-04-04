%{?scl:%scl_package perl-Test2-Suite}

# Break lines according to Unicode rules
%if ! (0%{?scl:1})
%bcond_without perl_Test2_Suite_enables_unicode
%else
%bcond_with perl_Test2_Suite_enables_unicode
%endif

Name:           %{?scl_prefix}perl-Test2-Suite
Version:        0.000127
Release:        2%{?dist}
Summary:        Set of tools built upon the Test2 framework
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Suite
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Suite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(Importer) >= 0.024
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Module::Pluggable) >= 2.7
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Scope::Guard)
BuildRequires:  %{?scl_prefix}perl(Sub::Info) >= 0.002
BuildRequires:  %{?scl_prefix}perl(Term::Table) >= 0.013
BuildRequires:  %{?scl_prefix}perl(Term::Table::Cell)
BuildRequires:  %{?scl_prefix}perl(Term::Table::LineBreak)
BuildRequires:  %{?scl_prefix}perl(Term::Table::Util)
BuildRequires:  %{?scl_prefix}perl(Test2::API) >= 1.302158
BuildRequires:  %{?scl_prefix}perl(Test2::API::Context)
BuildRequires:  %{?scl_prefix}perl(Test2::Event)
BuildRequires:  %{?scl_prefix}perl(Test2::Event::Exception)
# Test2::Event::Note loaded by send_event()
BuildRequires:  %{?scl_prefix}perl(Test2::Event::Note)
# Test2::Event::Skip loaded by send_event()
BuildRequires:  %{?scl_prefix}perl(Test2::Event::Skip)
BuildRequires:  %{?scl_prefix}perl(Test2::EventFacet)
BuildRequires:  %{?scl_prefix}perl(Test2::EventFacet::Info::Table)
BuildRequires:  %{?scl_prefix}perl(Test2::Hub::Interceptor)
BuildRequires:  %{?scl_prefix}perl(Test2::Hub::Subtest)
BuildRequires:  %{?scl_prefix}perl(Test2::IPC)
BuildRequires:  %{?scl_prefix}perl(Test2::Tools::Tiny)
BuildRequires:  %{?scl_prefix}perl(Test2::Util)
BuildRequires:  %{?scl_prefix}perl(Test2::Util::HashBase)
BuildRequires:  %{?scl_prefix}perl(Test2::Util::Trace)
BuildRequires:  %{?scl_prefix}perl(threads)
BuildRequires:  %{?scl_prefix}perl(Time::HiRes)
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(vars)
# Optional run-time:
# Sub::Util or Sub::Name
BuildRequires:  %{?scl_prefix}perl(Sub::Util)
%if %{with perl_Test2_Suite_enables_unicode}
BuildRequires:  %{?scl_prefix}perl(Unicode::GCString)
%endif
# Tests:
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(PerlIO)
BuildRequires:  %{?scl_prefix}perl(Test2::EventFacet::Assert)
BuildRequires:  %{?scl_prefix}perl(Test2::Formatter::TAP)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Importer) >= 0.024
Requires:       %{?scl_prefix}perl(Module::Pluggable) >= 2.7
Requires:       %{?scl_prefix}perl(Sub::Info) >= 0.002
# Sub::Util or Sub::Name
Requires:       %{?scl_prefix}perl(Sub::Util)
Requires:       %{?scl_prefix}perl(Term::Table) >= 0.013
Requires:       %{?scl_prefix}perl(Test2::API) >= 1.302158
Requires:       %{?scl_prefix}perl(Test2::Event)
# Test2::Event::Note loaded by send_event()
Requires:       %{?scl_prefix}perl(Test2::Event::Note)
# Test2::Event::Skip loaded by send_event()
Requires:       %{?scl_prefix}perl(Test2::Event::Skip)
Requires:       %{?scl_prefix}perl(Test2::EventFacet)
Requires:       %{?scl_prefix}perl(threads)
Requires:       %{?scl_prefix}perl(utf8)
%if %{with perl_Test2_Suite_enables_unicode}
# Unicode::GCString for formating double-width strings
Requires:       %{?scl_prefix}perl(Unicode::GCString)
%endif
# perl-Test2-AsyncSubtest-0:0.000020-1.fc28 merged
Provides:       %{?scl_prefix}perl-Test2-AsyncSubtest = %{version}-%{release}
Obsoletes:      %{?scl_prefix}perl-Test2-AsyncSubtest < 0.000020-2
# perl-Test2-Workflow-0:0.000018-4.fc27 merged
Provides:       %{?scl_prefix}perl-Test2-Workflow = %{version}-%{release}
Obsoletes:      %{?scl_prefix}perl-Test2-Workflow < 0.000018-5

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^%{?scl_prefix}perl\\((Importer|Module::Pluggable|Sub::Info|Term::Table|Test2::API)\\)$

%description
Rich set of tools, plugins, bundles, etc. built upon the Test2 testing
library. If you are interested in writing Perl tests this is the distribution
for you.

%prep
%setup -q -n Test2-Suite-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.000127-2
- SCL

* Thu Oct 31 2019 Petr Pisar <ppisar@redhat.com> - 0.000127-1
- 0.000127 bump

* Thu Aug 29 2019 Petr Pisar <ppisar@redhat.com> - 0.000126-1
- 0.000126 bump

* Tue Aug 20 2019 Petr Pisar <ppisar@redhat.com> - 0.000125-1
- 0.000125 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 0.000124-1
- 0.000124 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000122-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.000122-2
- Perl 5.30 rebuild

* Mon May 20 2019 Petr Pisar <ppisar@redhat.com> - 0.000122-1
- 0.000122 bump

* Thu May 09 2019 Petr Pisar <ppisar@redhat.com> - 0.000121-1
- 0.000121 bump

* Mon Apr 29 2019 Petr Pisar <ppisar@redhat.com> - 0.000120-1
- 0.000120 bump

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 0.000119-1
- 0.000119 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Petr Pisar <ppisar@redhat.com> - 0.000118-1
- 0.000118 bump

* Wed Dec 05 2018 Petr Pisar <ppisar@redhat.com> - 0.000117-1
- 0.000117 bump

* Thu Nov 29 2018 Petr Pisar <ppisar@redhat.com> - 0.000116-1
- 0.000116 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Petr Pisar <ppisar@redhat.com> - 0.000115-1
- 0.000115 bump

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.000114-2
- Perl 5.28 rebuild

* Fri Apr 20 2018 Petr Pisar <ppisar@redhat.com> - 0.000114-1
- 0.000114 bump

* Thu Mar 15 2018 Petr Pisar <ppisar@redhat.com> - 0.000111-1
- 0.000111 bump

* Mon Mar 12 2018 Petr Pisar <ppisar@redhat.com> - 0.000108-1
- 0.000108 bump

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.000106-1
- 0.000106 bump

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 0.000104-1
- 0.000104 bump

* Mon Mar 05 2018 Petr Pisar <ppisar@redhat.com> - 0.000102-1
- 0.000102 bump

* Wed Feb 14 2018 Petr Pisar <ppisar@redhat.com> - 0.000100-1
- 0.000100 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000097-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 0.000097-1
- 0.000097 bump

* Fri Dec 08 2017 Petr Pisar <ppisar@redhat.com> - 0.000094-2
- Remove unused dependency on Term::ReadKey

* Tue Dec 05 2017 Petr Pisar <ppisar@redhat.com> - 0.000094-1
- 0.000094 bump

* Mon Nov 20 2017 Petr Pisar <ppisar@redhat.com> - 0.000084-1
- 0.000084 bump

* Fri Oct 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000083-1
- 0.000083 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000082-1
- 0.000082 bump

* Tue Oct 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000080-1
- 0.000080 bump

* Thu Sep 14 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000077-1
- 0.000077 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000072-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Petr Pisar <ppisar@redhat.com> - 0.000072-1
- 0.000072 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000070-2
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 0.000070-1
- 0.000070 bump

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 0.000069-1
- 0.000069 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000067-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Petr Pisar <ppisar@redhat.com> - 0.000067-1
- 0.000067 bump

* Tue Dec 20 2016 Petr Pisar <ppisar@redhat.com> - 0.000065-1
- 0.000065 bump

* Mon Dec 19 2016 Petr Pisar <ppisar@redhat.com> - 0.000063-1
- 0.000063 bump

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 0.000060-1
- 0.000060 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 0.000058-1
- 0.000058 bump

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000055-1
- 0.000055 bump

* Fri Jul 29 2016 Petr Pisar <ppisar@redhat.com> - 0.000054-1
- 0.000054 bump

* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 0.000052-1
- 0.000052 bump

* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000050-1
- 0.000050 bump

* Mon Jul 04 2016 Petr Pisar <ppisar@redhat.com> - 0.000048-1
- 0.000048 bump

* Tue Jun 28 2016 Petr Pisar <ppisar@redhat.com> - 0.000042-1
- 0.000042 bump

* Mon Jun 27 2016 Petr Pisar <ppisar@redhat.com> - 0.000038-1
- 0.000038 bump

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 0.000032-1
- 0.000032 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000030-2
- Perl 5.24 rebuild

* Wed May 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000030-1
- 0.000030 bump

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 0.000029-1
- 0.000029 bump

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 0.000028-1
- 0.000028 bump

* Thu Apr 14 2016 Petr Pisar <ppisar@redhat.com> - 0.000027-1
- 0.000027 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000026-1
- 0.000026 bump

* Tue Apr 05 2016 Petr Pisar <ppisar@redhat.com> - 0.000025-1
- 0.000025 bump

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 0.000024-1
- 0.000024 bump

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 0.000023-1
- 0.000023 bump

* Tue Mar 08 2016 Petr Pisar <ppisar@redhat.com> - 0.000022-1
- 0.000022 bump

* Mon Mar 07 2016 Petr Pisar <ppisar@redhat.com> - 0.000021-1
- 0.000021 bump

* Thu Feb 11 2016 Petr Pisar <ppisar@redhat.com> 0.000020-1
- Specfile autogenerated by cpanspec 1.78.
