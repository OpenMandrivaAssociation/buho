#define snapshot 20220107

Name:		buho
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://invent.kde.org/maui/buho/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/buho-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/buho-%{snapshot}.tar.bz2}
Patch0:   https://invent.kde.org/maui/buho/-/merge_requests/7.patch
Group:		Applications/Productivity
Summary:	Note taking app for Plasma Mobile
License:	GPLv3
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitAccounts4)
BuildRequires:  cmake(MauiKitTextEditor4)

%description
Note taking app for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang buho

%files -f buho.lang
%{_bindir}/buho
%{_datadir}/applications/org.kde.buho.desktop
%{_datadir}/icons/hicolor/scalable/apps/buho.svg
%{_datadir}/metainfo/org.kde.buho.metainfo.xml
