Summary:	2D plotting widget extension to the Qt GUI
Summary(pl.UTF-8):	Rozszerzenie wykresów 2D dla GUI Qt
Name:		qwt
Version:	5.2.3
Release:	2
License:	Qwt v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/qwt/%{name}-%{version}.tar.bz2
# Source0-md5:	7d37a11d02bc7d095d0ca6427ec97b8d
Patch0:		%{name}-install.patch
URL:		http://qwt.sourceforge.net/
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtDesigner-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtScript-devel >= 4.5
BuildRequires:	QtSvg-devel >= 4.5
BuildRequires:	QtXml-devel >= 4.5
BuildRequires:	qt4-build >= 4.5
BuildRequires:	qt4-qmake >= 4.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS. The Qwt
library contains widgets and components which are primarily useful for
technical and scientifical purposes. It includes a 2-D plotting
widget, different kinds of sliders, and much more.

%description -l pl.UTF-8
Qwt jest rozszerzeniem do biblioteki Qt z Troll Tech AS. Biblioteka
Qwt zawiera widgety i komponenty użyteczne głównie do celów
technicznych i naukowych. Zawiera widget do rysowania wykresów 2D,
różne rodzaje suwaków i wiele więcej.

%package devel
Summary:	Header files for Qwt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Qwt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.5
Requires:	QtGui-devel >= 4.5

%description devel
Header files for Qwt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qwt.

%package apidocs
Summary:	API documentation for Qwt library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Qwt
Group:		Documentation

%description apidocs
API documentation for Qwt library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Qwt.

%package -n QtDesigner-plugin-qwt
Summary:	qwt plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka qwt dla Qt Designera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner >= 4.5
Obsoletes:	qt4-plugin-qwt

%description -n QtDesigner-plugin-qwt
qwt plugin for Qt Designer.

%description -n QtDesigner-plugin-qwt -l pl.UTF-8
Wtyczka qwt dla Qt Designera.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 qwt.pro \
	INSTALLBASE=%{_prefix} \
	DOCDIR=%{_docdir} \
	LIBDIR=%{_libdir} \
	INCDIR=%{_includedir}/qwt \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/man/man3 $RPM_BUILD_ROOT%{_mandir}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/html

# pointless link
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqwt.so.?.?

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libqwt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwt.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqwt.so
%{_includedir}/qwt
%{_mandir}/man3/Qwt*.3*
%{_mandir}/man3/controlscreenshots.3*
%{_mandir}/man3/curvescreenshots.3*
%{_mandir}/man3/deprecated.3*
%{_mandir}/man3/histogramscreenshots.3
%{_mandir}/man3/qwtinstall.3*
%{_mandir}/man3/qwtlicense.3*
%{_mandir}/man3/scatterscreenshots.3
%{_mandir}/man3/spectrogramscreenshots.3*
%{_examplesdir}/%{name}-%{version}

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.css doc/html/*.html doc/html/*.png examples

%files -n QtDesigner-plugin-qwt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libqwt_designer_plugin.so
