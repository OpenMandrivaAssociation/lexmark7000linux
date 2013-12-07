%define	debug_package %{nil}

Summary:	Lexmark 7xxx and 57zzz printer driver for Linux
Name:		lexmark7000linux
Version:	990516
Release:	15
License:	GPLv2
Group:		System/Printing
Url:		http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/olddrv.html
Source0:	http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/%{name}-%{version}.tar.bz2

%description
This is the printer driver for Lexmark 7000 "GDI" printers.

 * Known to work with Lexmark 7000, 7200 and 5700 printers
 * 600x600 dpi Black & White printing
 * Preliminary 600x600 CMY colour printing for 7000, 7200

%prep
%setup -q

# Fix Makefile
sed -i -e 's@-o root -g root@@' Makefile

%build
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}

%makeinstall

%files
%doc README CHANGES lexmark*-filter lexmarkprotocol.txt *.prn *.pbm
%{_bindir}/pbm2l7k
%{_bindir}/pnmraw2cmyk
%{_bindir}/pbm2lex5700
%{_bindir}/pnm2lex7000
%{_bindir}/pnm2lex5700
%{_bindir}/dbman
%{_bindir}/psprint
%{_bindir}/pscprint

