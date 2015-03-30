# TODO:
# - fix build without qwt-devel:
# x86_64-pld-linux-g++ ... libqwt_designer_plugin.so ... -L../lib
#   -lqwt -lQtScript -lQtXml -lQtGui -lQtCore -lQtDesigner -lpthread
# /usr/bin/ld: cannot find -lqwt
Summary:	2D plotting widget extension to the Qt GUI
Summary(pl.UTF-8):	Rozszerzenie wykresów 2D dla GUI Qt
Name:		qwt
Version:	5.2.1
Release:	2
License:	Qwt v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/qwt/%{name}-%{version}.tar.bz2
# Source0-md5:	4a595b8db0ec3856b117836c1d60cb27
URL:		http://qwt.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSvg-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake >= 4.3.3-3
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
Summary:	Header files for qwt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qwt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui-devel

%description devel
Header files for qwt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki qwt.

%package -n qt4-plugin-qwt
Summary:	qwt plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka qwt dla Qt Designera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner

%description -n qt4-plugin-qwt
qwt plugin for Qt Designer.

%description -n qt4-plugin-qwt -l pl.UTF-8
Wtyczka qwt dla Qt Designera.

%prep
%setup -q

%build
qmake-qt4 qwt.pro

%{__make} -j1 \
	CC="%{__cc}" \
	CXX="%{__cxx}"

### can't build without qwt-devel ver 5.1.0 installed
#cd examples
#qmake-qt4 examples.pro
#%{__make} -j1
#%{__make} distclean
#rm -fr .*.cache */.*.cache */*/.*.cache Makefile */moc */obj */*/moc */*/obj
#cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir}/qt4/plugins-mt/designer,%{_mandir}/man3}

for n in src/*.h; do
	cp -p $n $RPM_BUILD_ROOT%{_includedir}/%{name}
done

for n in lib/libqwt.so*; do
	cp -d $n $RPM_BUILD_ROOT%{_libdir}
done

%{__make} -C designer install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# pointless link
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqwt.so.?.?

# XXX, what for?
echo "%{_libdir}/qt4/plugins/designer/libqwtplugin.so" > plugin.list

for n in doc/man/man3/*.3; do
	cp -p $n $RPM_BUILD_ROOT%{_mandir}/man3
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqwt.so.5

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.css doc/html/*.html doc/html/*.gif doc/html/*.png
%doc examples
%{_libdir}/libqwt.so
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

%files -n qt4-plugin-qwt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libqwt_designer_plugin.so
