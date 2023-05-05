#define snapshot 20220107

Name:		buho
Version:	2.2.2
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://invent.kde.org/maui/buho/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/buho-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/buho-%{snapshot}.tar.bz2}
Group:		Applications/Productivity
Summary:	Note taking app for Plasma Mobile
License:	GPLv3
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:  cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5WebView)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(MauiKit)
BuildRequires:  cmake(MauiKitFileBrowsing)
BuildRequires:  cmake(MauiKitAccounts)

%description
Note taking app for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/buho
%{_datadir}/applications/org.kde.buho.desktop
%{_datadir}/icons/hicolor/scalable/apps/buho.svg
%{_datadir}/metainfo/org.kde.buho.metainfo.xml
