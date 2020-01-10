%define tarball xf86-video-mach64
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 mach64 video driver
Name:	    xorg-x11-drv-mach64
Version:    6.9.4
Release:    8%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support

Source0:    http://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

Patch0:	    mach64-6.8.1-defaultdepth.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.1.5

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 mach64 video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .defaultdepth

%build
autoreconf -vif
%configure --disable-static --disable-dri --disable-exa
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{driverdir}/mach64_drv.so
#{_mandir}/man4/mach64.4*

%changelog
* Mon Apr 28 2014 Adam Jackson <ajax@redhat.com> - 6.9.4-8
- Fix rhel arch list

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 6.9.4-6
- autoreconf for aarch64

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.4-5
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.4-4
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.4-3
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.4-2
- ABI rebuild

* Wed Jan 09 2013 Adam Jackson <ajax@redhat.com> 6.9.4-1
- mach64 6.9.4

* Mon Oct 01 2012 Adam Jackson <ajax@redhat.com> 6.9.3-5
- mach64-6.9.3-shadowfb.patch: Allow Render even when doing ShadowFB.
- Disable EXA as well, it's completely broken.
- mach64-6.9.3-fix-no-exa-build.patch: Fix building with neither XAA nor EXA.

* Wed Sep 26 2012 Adam Jackson <ajax@redhat.com> 6.9.3-4
- Disable DRI support, we've never built the 3D driver and it's been nuked
  from upstream Mesa anyway.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 6.9.3-2
- add build fix patch for 32-bit

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 6.9.3-1
- mach64 6.9.3

* Fri Apr 27 2012 Adam Jackson <ajax@redhat.com> 6.9.1-1
- mach64 6.9.1

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 6.9.0-10
- RHEL arch exclude updates

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.0-9
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.0-8
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.0-7
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 6.9.0-6
- Rebuild for server 1.12

* Fri Dec 16 2011 Adam Jackson <ajax@redhat.com> - 6.9.0-5
- Drop xinf file

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 6.9.0-4
- ABI rebuild

* Wed Nov 09 2011 ajax <ajax@redhat.com> - 6.9.0-3
- ABI rebuild

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 6.9.0-2
- Rebuild for xserver 1.11 ABI

* Tue Jun 21 2011 Adam Jackson <ajax@redhat.com> 6.9.0-1
- mach64 6.9.0

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 6.8.2-8
- Rebuild for server 1.11

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> - 6.8.2-7
- Rebuild for server 1.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Dave Airlie <airlied@redhat.com> 6.8.2-5
- fix pixmap private API

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 6.8.2-4
- Add ABI requires magic (#542742)

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 6.8.2-3
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 6.8.2-2
- Rebuild for server 1.8

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 6.8.2-1
- mach64 6.8.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> 6.8.1-1
- mach64 6.8.1
- mach64-6.8.1-defaultdepth.patch: Default to depth 16 (#472687)

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 6.8.0-3.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 6.8.0-2
- update for latest server API

* Mon Aug 04 2008 Adam Jackson <ajax@redhat.com> 6.8.0-1
- Initial build of separate mach64 driver.

