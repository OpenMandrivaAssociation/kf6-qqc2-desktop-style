%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define devname %mklibname KF6QqcDesktopStyle -d
#define git 20240217

Name: kf6-qqc2-desktop-style
Version: 6.16.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/qqc2-desktop-style/-/archive/master/qqc2-desktop-style-master.tar.bz2#/qqc2-desktop-style-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/qqc2-desktop-style-%{version}.tar.xz
%endif
Summary: Qt Quick Controls 2: Desktop Style
URL: https://invent.kde.org/frameworks/qqc2-desktop-style
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ColorScheme)

%description
Qt Quick Controls 2: Desktop Style

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt Quick Controls 2: Desktop Style

%prep
%autosetup -p1 -n qqc2-desktop-style-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%{_qtdir}/qml/org/kde/desktop
%{_qtdir}/qml/org/kde/qqc2desktopstyle
%{_qtdir}/plugins/kf6/kirigami/platform/org.kde.desktop.so

%files -n %{devname}
%{_libdir}/cmake/KF6QQC2DesktopStyle
