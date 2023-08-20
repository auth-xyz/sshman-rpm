Name:     sshman
Version:  0.2.4
Release:  1%{?dist}
Summary:  A SSH manager based on sessions
License:  MIT
URL:      https://github.com/auth-xyz/sshman
BuildRequires: python3
BuildRequires: wget

%define url https://github.com/auth-xyz/sshman/releases/download/v0.2.4/linux-snow-dome.tar.gz

%description
sshman is a simple SSH manager which creates and manages sessions.

%prep
# Ensuring the installation is fresh.
sudo unlink /usr/bin/sshman

# Making directories
mkdir -p $HOME/.sshm/.bin
mkdir -p $HOME/.sshm/.cache

# Downloading latest version and extracting
wget %{url} -O %{_builddir}/linux-snow-dome.tar.gz
tar xvfz %{_builddir}/linux-snow-dome.tar.gz --directory %{_builddir}

mv %{_builddir}/sshman $HOME/.sshm/.bin/
sudo ln -s $HOME/.sshm/.bin/sshman /usr/bin

%install
mkdir -p %{buildroot}%{_bindir}
cp -p $HOME/.sshm/.bin/sshman %{buildroot}%{_bindir}/sshman


%files
%defattr(-,root,root,-)
/usr/bin/sshman

%post

%changelog
* Sat Aug 19 2023 Auth P <smmc.auth@gmail.com>
- Initial version of the package

