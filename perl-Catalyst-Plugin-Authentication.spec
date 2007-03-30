#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Authentication
Summary:	Catalyst::Plugin::Authentication - Authentication infrastructure plugin for the Catalyst framework.
#Summary(pl.UTF-8):	
Name:		perl-Catalyst-Plugin-Authentication
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/Catalyst-Plugin-Authentication-%{version}.tar.gz
# Source0-md5:	59be3895b1c79609545d5472ec4e4bb5
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Authentication/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.10
BuildRequires:	perl(Class::Inspector)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The authentication plugin provides generic user support for Catalyst apps. It
is the basis for both authentication (checking the user is who they claim to
be), and authorization (allowing the user to do what the system authorises
them to do).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Authentication
%{_mandir}/man3/*
