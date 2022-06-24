%define		kodi_ver	19
%define		next_kodi_ver	%(echo $((%{kodi_ver}+1)))
%define		codename	Matrix
%define		addon		inputstream.ffmpegdirect

Summary:	Kodi InputStream ffmpegdirect addon
Name:		kodi-addon-inputstream-ffmpegdirect
Version:	%{kodi_ver}.0.3
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/xbmc/inputstream.ffmpegdirect/archive/%{version}-%{codename}/%{version}-%{codename}.tar.gz
# Source0-md5:	6478a316f5078b1c623753375539001b
URL:		https://github.com/xbmc/inputstream.ffmpegdirect
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.5
BuildRequires:	ffmpeg-devel
BuildRequires:	kodi-devel >= %{kodi_ver}
BuildRequires:	kodi-devel < %{next_kodi_ver}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Requires:	kodi >= %{kodi_ver}
Requires:	kodi < %{next_kodi_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Kodi input stream addon for streams that can be opened by
either FFmpeg's libavformat or Kodi's cURL. Common stream formats such
as plain TS, HLS and DASH are supported as well as many others. Note
that the only DASH streams supported are those without DRM.

The addon also has support for Archive/Catchup services where there is
a replay window (usually in days) and can timeshift across that span.
In addition the addon can also provide timeshift to live streams where
rewind/pause and fast-forward woud not have previously been possible.

%prep
%setup -q -n %{addon}-%{version}-%{codename}

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/kodi/addons/%{addon}
%attr(755,root,root) %{_libdir}/kodi/addons/%{addon}/%{addon}.so.%{version}
%dir %{_datadir}/kodi/addons/%{addon}
%{_datadir}/kodi/addons/%{addon}/addon.xml
%{_datadir}/kodi/addons/%{addon}/changelog.txt
%{_datadir}/kodi/addons/%{addon}/fanart.jpg
%{_datadir}/kodi/addons/%{addon}/icon.png
%{_datadir}/kodi/addons/%{addon}/resources
