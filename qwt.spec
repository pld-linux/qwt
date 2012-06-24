Summary:	2D plotting widget extension to the Qt GUI
Summary(pl):	Rozszerzenie wykres�w 2D dla GUI Qt
Name:		qwt
Version:	4.2.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/qwt/%{name}-%{version}.tar.bz2
# Source0-md5:	9c828c9a39a83df5d7fa9630ddf812a4
URL:		http://qwt.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS. The Qwt
library contains widgets and components which are primarily useful for
technical and scientifical purposes. It includes a 2-D plotting
widget, different kinds of sliders, and much more.

%description -l pl
Qwt jest rozszerzeniem do biblioteki Qt z Troll Tech AS. Biblioteka
Qwt zawiera widgety i komponenty u�yteczne g��wnie do cel�w
technicznych i naukowych. Zawiera widget do rysowania wykres�w 2D,
r�ne rodzaje suwak�w i wiele wi�cej.

%package devel
Summary:	Header files for qwt library
Summary(pl):	Pliki nag��wkowe biblioteki qwt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt-devel

%description devel
Header files for qwt library.

%description devel -l pl
Pliki nag��wkowe biblioteki qwt.

%package -n qt-plugin-qwt
Summary:	qwt plugin for Qt Designer
Summary(pl):	Wtyczka qwt dla Qt Designera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt-designer

%description -n qt-plugin-qwt
qwt plugin for Qt Designer.

%description -n qt-plugin-qwt -l pl
Wtyczka qwt dla Qt Designera.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
qmake qwt.pro

%{__make}

cd examples
	qmake examples.pro
	%{__make}
	%{__make} distclean
	rm -fr .*.cache */.*.cache */*/.*.cache Makefile */moc */obj */*/moc */*/obj
cd ..

cd designer
	qmake qwtplugin.pro
	%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir}/qt/plugins-mt/designer,%{_mandir}/man3}

for n in include/*.h ; do
    install -m 644 $n $RPM_BUILD_ROOT%{_includedir}/%{name}
done

for n in lib/libqwt.so* ; do
    cp -d $n $RPM_BUILD_ROOT%{_libdir}
done

 cd designer
 %{__make} install \
 	INSTALL_ROOT=$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/
# If you find better idea to put this file into proper directory, change this fix
mv $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/usr/plugins/designer/libqwtplugin.so \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/designer/libqwtplugin.so

 cd ..
 echo "%{_libdir}/qt/plugins-mt/designer/libqwtplugin.so" > plugin.list

for n in doc/man/man3/*.3 ; do
    install -m 644 $n $RPM_BUILD_ROOT%{_mandir}/man3
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.css doc/html/*.html doc/html/*.gif doc/html/*.png
%doc examples
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_mandir}/man3/*

%files -n qt-plugin-qwt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins-mt/designer/libqwtplugin.so
