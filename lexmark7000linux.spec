Summary:	Lexmark 7xxx and 57zzz printer driver for Linux
Name:		lexmark7000linux
Version:	990516
Release:	%mkrel 2
License:	GPL
Group:		File tools
Source:		http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/%{name}-%{version}.tar.bz2
URL:		http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/olddrv.html
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the printer driver for Lexmark 7000 "GDI" printers.

 * Known to work with Lexmark 7000, 7200 and 5700 printers
 * 600x600 dpi Black & White printing
 * Preliminary 600x600 CMY colour printing for 7000, 7200

%prep

%setup -q

# Fix Makefile
perl -pi -e 's@-o root -g root@@' Makefile

%build
make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc README CHANGES lexmark*-filter lexmarkprotocol.txt *.prn *.pbm
%attr(0755,root,root)%{_bindir}/pbm2l7k
%attr(0755,root,root)%{_bindir}/pnmraw2cmyk
%attr(0755,root,root)%{_bindir}/pbm2lex5700
%attr(0755,root,root)%{_bindir}/pnm2lex7000
%attr(0755,root,root)%{_bindir}/pnm2lex5700
%attr(0755,root,root)%{_bindir}/dbman
%attr(0755,root,root)%{_bindir}/psprint
%attr(0755,root,root)%{_bindir}/pscprint
