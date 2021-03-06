# Generated by rust2rpm 12
# Tests require files not included in crate
%bcond_with check
%global debug_package %{nil}

%global crate zstd
%global upstream_version 0.5.1+zstd.1.4.4

Name:           rust-%{crate}
Version:        0.5.1
Release:        2%{?dist}
Summary:        Binding for the zstd compression library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/zstd
Source:         %{crates_source %{crate} %{upstream_version}}
# Initial patched metadata
# * Remove zstd version from version field
# * Remove bindgen feature as it is now the default to build with system zstd
Patch0:         zstd-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Binding for the zstd compression library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc Readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages
which use "futures" feature of "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+legacy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+legacy-devel %{_description}

This package contains library source intended for building other packages
which use "legacy" feature of "%{crate}" crate.

%files       -n %{name}+legacy-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages
which use "tokio" feature of "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-io-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-io" feature of "%{crate}" crate.

%files       -n %{name}+tokio-io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-devel %{_description}

This package contains library source intended for building other packages
which use "wasm" feature of "%{crate}" crate.

%files       -n %{name}+wasm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{upstream_version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 06:14:56 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Initial package
