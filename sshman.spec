Name:     sshman
Version:  0.3.2
Release:  1%{?dist}
Summary:  A SSH manager based on sessions
License:  MIT
URL:      https://github.com/auth-xyz/sshman
BuildRequires: python3
BuildRequires: wget

%define url https://github.com/auth-xyz/sshman/releases/download/v0.3.2/linux-vancouver.tar.gz

%description
sshman is a simple SSH manager which creates and manages sessions.

%prep
# Ensuring the installation is fresh.
[ -f "/usr/bin/sshman" ] && unlink /usr/bin/sshman

# Making directories
mkdir -p $HOME/.sshm/.bin
mkdir -p $HOME/.sshm/.cache

# Downloading latest version and extracting
wget %{url} -O %{_builddir}/linux-snow-dome.tar.gz
tar xvfz %{_builddir}/linux-snow-dome.tar.gz --directory %{_builddir}

mv %{_builddir}/sshman $HOME/.sshm/.bin/

%install
mkdir -p %{buildroot}%{_bindir}
cp -p $HOME/.sshm/.bin/sshman %{buildroot}%{_bindir}/sshman


%files
%defattr(-,root,root,-)
/usr/bin/sshman

%post

%changelog
* Thu Aug 24 2023 auth-xyz <smmc.auth@gmail.com> 0.3.2-1
- Updated to new version (smmc.auth@gmail.com)

* Sun Aug 20 2023 auth-xyz <smmc.auth@gmail.com> 0.3.0-1
- Changed the spec for the new version (smmc.auth@gmail.com)
- OK NOW I FIXED IT (smmc.auth@gmail.com)
- Now the thing works i think (smmc.auth@gmail.com)
- please (smmc.auth@gmail.com)
- big update to 0.3.0 (smmc.auth@gmail.com)
* Sun Aug 20 2023 auth-xyz <smmc.auth@gmail.com>
- Changed the spec for the new version (smmc.auth@gmail.com)
- OK NOW I FIXED IT (smmc.auth@gmail.com)
- Now the thing works i think (smmc.auth@gmail.com)
- please (smmc.auth@gmail.com)

* Sun Aug 20 2023 auth-xyz <smmc.auth@gmail.com>
- please god (smmc.auth@gmail.com)

* Sat Aug 19 2023 Auth P <smmc.auth@gmail.com>
- Initial version of the package

