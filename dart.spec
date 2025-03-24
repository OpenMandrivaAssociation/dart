%global debug_package %{nil}

Name:           dart
Version:        3.7.2
Release:        1
Summary:        Dart SDK
License:        BSD
URL:            https://dart.dev/
Source0:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-x64-release.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-arm64-release.zip


%description
The Dart SDK has the libraries and command-line tools that you need to develop Dart web, command-line, and server apps.

%prep

%ifarch x86_64
%autosetup -T -b 0 -n dart-sdk
%elifarch aarch64
%autosetup -T -b 1 -n dart-sdk
%endif

%install
install -dp %{buildroot}%{_bindir}
install -dp %{buildroot}%{_libdir}/dart
cp -pr . %{buildroot}%{_libdir}/dart
%{__ln_s} -f ../%{_lib}/dart/bin/dart %{buildroot}%{_bindir}/dart


%files
%license LICENSE
%{_bindir}/dart
%{_libdir}/dart/*
