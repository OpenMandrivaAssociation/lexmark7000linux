Summary:	Lexmark 7xxx and 57zzz printer driver for Linux
Name:		lexmark7000linux
Version:	990516
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
Source:		http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/%{name}-%{version}.tar.bz2
URL:		http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/olddrv.html
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
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
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 990516-11mdv2011.0
+ Revision: 666074
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 990516-10mdv2011.0
+ Revision: 606403
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 990516-9mdv2010.1
+ Revision: 519018
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 990516-8mdv2010.0
+ Revision: 425508
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 990516-7mdv2009.1
+ Revision: 318501
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 990516-6mdv2009.0
+ Revision: 222425
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 990516-5mdv2008.1
+ Revision: 150444
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 990516-4mdv2008.0
+ Revision: 75341
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 990516-3mdv2008.0
+ Revision: 64161
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 990516-2mdv2008.0
+ Revision: 61089
- rebuild

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 990516-1mdv2008.0
+ Revision: 60977
- Import lexmark7000linux



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 990516-1mdv2008.0
- initial Mandriva package

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:08:53 (8371)
- Copying release 990516-1cl to releases/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:08:51 (8370)
- Copying release 990516-1cl to pristine/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:08:47 (8369)
- Imported package from 8.0.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:08:42 (8368)
- Created package directory
