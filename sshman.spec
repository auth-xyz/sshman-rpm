Name:     sshman
Version:  0.3.2
Release:  1%{?dist}
Summary:  A SSH manager based on sessions
License:  MIT
URL:      https://github.com/auth-xyz/sshman
BuildRequires: python3
BuildRequires: wget

%define url https://github.com/auth-xyz/sshman/releases/download/v0.3.2/linux-vancouver.tar.gz
%define package vancouver

%description
sshman is a simple SSH manager which creates and manages sessions.

%prep
# Ensuring the installation is fresh.
[ -f "/usr/bin/sshman" ] && unlink /usr/bin/sshman

# Making directories
mkdir -p $HOME/.sshm/.bin
mkdir -p $HOME/.sshm/.cache

# Downloading latest version and extracting
wget %{url} -O %{_builddir}/linux-%{package}.tar.gz
tar xvfz %{_builddir}/linux-snow-dome.tar.gz --directory %{_builddir}

mv %{_builddir}/sshman $HOME/.sshm/.bin/

%install
mkdir -p %{buildroot}%{_bindir}
/usr/bin/ln -s $HOME/.sshm/.bin/sshman %{buildroot}%{_bindir}/sshman


%files
%defattr(-,root,root,-)
/usr/bin/sshman

%post
umask 007
/sbin/ldconfig > /dev/null 2>&1


%postun
umask 007
/sbin/ldconfig > /dev/null 2>&1
/usr/bin/rm %{_builddir}/linux-%{package}.tar.gz


%changelog
* Thu Aug 24 2023 auth-xyz <smmc.auth@gmail.com>
- Might have fixed some issues. building lcoally works (smmc.auth@gmail.com)
- S (smmc.auth@gmail.com)
- A (smmc.auth@gmail.com)
- Should fix the --update feature on release (authenticover@gmail.com)

* Thu Aug 24 2023 auth-xyz <smmc.auth@gmail.com>
- Should fix the --update feature on release (authenticover@gmail.com)
