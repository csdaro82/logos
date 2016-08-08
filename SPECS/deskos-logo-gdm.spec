Name:           deskos-logo-gdm
Version:        0.1.0
Release:        1%{?dist}
Summary:        Logo de deskos para GDM

Group:          User Interface/Desktops
License:        GPLv3	
URL:            https://proyectodeskos.org/
Source0:        01-deskos-logo
Source1:        deskos-logo.png

BuildArch:      noarch
Requires(post): glib2
Requires(post): dconf

%description
Logo Sistema Operativo DeskOS
(icono DeskOS) para la pantalla de login (GDM).

%install
install -d %{buildroot}%{_sysconfdir}/dconf/db/gdm.d
install -d %{buildroot}%{_datadir}/pixmaps/deskos

install %{SOURCE0} %{buildroot}/etc/dconf/db/gdm.d/
install %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/deskos/

%post
dconf update

%postun
dconf update

%files
%defattr(-,root,root)
%{_sysconfdir}/dconf/db/gdm.d/01-deskos-logo
%{_datadir}/pixmaps/deskos/deskos-logo.png

%changelog

* Thu Aug 04 2016 Dario Cordova <dario.cordova@soportelibre.com> - 0.1.0-1
- Version inicial
