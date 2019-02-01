#
# Conditional build:
%bcond_without	qt4	# Qt4 build
%bcond_without	qt5	# Qt5 build

Summary:	2D plotting widget extension to the Qt4 GUI
Summary(pl.UTF-8):	Rozszerzenie wykresów 2D dla GUI Qt4
Name:		qwt
Version:	6.1.3
Release:	1
License:	Qwt v1.0
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/qwt/%{name}-%{version}.tar.bz2
# Source0-md5:	19d1f5fa5e22054d22ee3accc37c54ba
Patch0:		%{name}-install.patch
Patch1:		%{name}-qt5.patch
URL:		http://qwt.sourceforge.net/
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtDesigner-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtOpenGL-devel >= 4.5
BuildRequires:	QtScript-devel >= 4.5
BuildRequires:	QtSvg-devel >= 4.5
BuildRequires:	QtXml-devel >= 4.5
BuildRequires:	qt4-build >= 4.5
BuildRequires:	qt4-qmake >= 4.5
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Designer-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5OpenGL-devel >= 5
BuildRequires:	Qt5Script-devel >= 5
BuildRequires:	Qt5Svg-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
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
Summary:	Header files for Qt4 Qwt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Qwt dla Qt4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.5
Requires:	QtGui-devel >= 4.5
Requires:	QtOpenGL-devel >= 4.5
Requires:	QtSvg-devel >= 4.5
Requires:	QtXml-devel >= 4.5

%description devel
Header files for Qt4 Qwt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qwt dla Qt4.

%package -n QtDesigner-plugin-qwt
Summary:	qwt plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka qwt dla Qt Designera
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner >= 4.5
Obsoletes:	qt4-plugin-qwt

%description -n QtDesigner-plugin-qwt
qwt plugin for Qt Designer.

%description -n QtDesigner-plugin-qwt -l pl.UTF-8
Wtyczka qwt dla Qt Designera.

%package -n qwt5
Summary:	2D plotting widget extension to the Qt5 GUI
Summary(pl.UTF-8):	Rozszerzenie wykresów 2D dla GUI Qt5
Group:		X11/Libraries

%description -n qwt5
Qwt is an extension to the Qt GUI library from Troll Tech AS. The Qwt
library contains widgets and components which are primarily useful for
technical and scientifical purposes. It includes a 2-D plotting
widget, different kinds of sliders, and much more.

%description -n qwt5 -l pl.UTF-8
Qwt jest rozszerzeniem do biblioteki Qt z Troll Tech AS. Biblioteka
Qwt zawiera widgety i komponenty użyteczne głównie do celów
technicznych i naukowych. Zawiera widget do rysowania wykresów 2D,
różne rodzaje suwaków i wiele więcej.

%package -n qwt5-devel
Summary:	Header files for Qt5 Qwt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Qwt dla Qt5
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5
Requires:	Qt5Gui-devel >= 5
Requires:	Qt5OpenGL-devel >= 5
Requires:	Qt5Svg-devel >= 5
Requires:	Qt5Widgets-devel >= 5
Requires:	Qt5Xml-devel >= 5

%description -n qwt5-devel
Header files for Qt5 Qwt library.

%description -n qwt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qwt dla Qt5.

%package -n Qt5Designer-plugin-qwt
Summary:	qwt plugin for Qt5 Designer
Summary(pl.UTF-8):	Wtyczka qwt dla Qt5 Designera
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Designer >= 5

%description -n Qt5Designer-plugin-qwt
qwt plugin for Qt5 Designer.

%description -n Qt5Designer-plugin-qwt -l pl.UTF-8
Wtyczka qwt dla Qt5 Designera.

%package apidocs
Summary:	API documentation for Qwt library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Qwt
Group:		Documentation

%description apidocs
API documentation for Qwt library with examples.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Qwt wraz z przykładami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
qmake-qt4 ../qwt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make} -j1
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
qmake-qt5 ../qwt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make} -j1
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%if %{with qt4}
%{__make} -C build-qt4 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_docdir}/qt4-doc/html/man/man3 $RPM_BUILD_ROOT%{_mandir}
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{without qt4}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/qt5-doc/html/man/man3 $RPM_BUILD_ROOT%{_mandir}
%endif
%endif

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/qt?-doc/html

# pointless link
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqwt*.so.?.?

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with qt4}
%files
%defattr(644,root,root,755)
%doc CHANGES-6.1 COPYING README
%attr(755,root,root) %{_libdir}/libqwt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwt.so.6
%attr(755,root,root) %{_libdir}/libqwtmathml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwtmathml.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqwt.so
%attr(755,root,root) %{_libdir}/libqwtmathml.so
%{_includedir}/qt4/qwt
%{_pkgconfigdir}/qwt.pc
%{_pkgconfigdir}/qwtmathml.pc
%{_datadir}/qt4/mkspecs/features/qwt*.pri
%{_datadir}/qt4/mkspecs/features/qwt.prf
%{_datadir}/qt4/mkspecs/features/qwtmathml.prf

%files -n QtDesigner-plugin-qwt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libqwt_designer_plugin.so
%endif

%if %{with qt5}
%files -n qwt5
%defattr(644,root,root,755)
%doc CHANGES-6.1 COPYING README
%attr(755,root,root) %{_libdir}/libqwt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwt5.so.6
%attr(755,root,root) %{_libdir}/libqwtmathml5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwtmathml5.so.6

%files -n qwt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqwt5.so
%attr(755,root,root) %{_libdir}/libqwtmathml5.so
%{_includedir}/qt5/qwt
%{_pkgconfigdir}/Qt5Qwt6.pc
%{_pkgconfigdir}/qwtmathml5.pc
%{_libdir}/qt5/mkspecs/features/qwt*.pri
%{_libdir}/qt5/mkspecs/features/qwt.prf
%{_libdir}/qt5/mkspecs/features/qwtmathml.prf

%files -n Qt5Designer-plugin-qwt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqwt_designer_plugin.so
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.css doc/html/*.html doc/html/*.png examples
%{_mandir}/man3/Qwt*.3*
%{_mandir}/man3/barchartscreenshots.3*
%{_mandir}/man3/controlscreenshots.3*
%{_mandir}/man3/curvescreenshots.3*
%{_mandir}/man3/otherscreenshots.3*
%{_mandir}/man3/qwtchangelog.3*
%{_mandir}/man3/qwtinstall.3*
%{_mandir}/man3/qwtlicense.3*
%{_mandir}/man3/spectrogramscreenshots.3*
%{_examplesdir}/%{name}-%{version}
