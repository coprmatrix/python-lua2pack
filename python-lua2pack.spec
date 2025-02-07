#
# spec file for package python-lua2pack
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-lua2pack
Version:        1.0.4
Release:        0
Summary:        Generate RPM or DSC spec files from luarocks
License:        GPL-3.0-only
URL:            https://github.com/huakim/lua2pack
Source:         lua2pack-%{version}.tar.gz
BuildRequires: %{python_module pytest}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module jinja2-easy.generator}
BuildRequires:  %{python_module luadata.luatable}
BuildRequires:  %{python_module lupa}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requests-glob}
BuildRequires:  %{python_module requests-stdin}
BuildRequires:  %{python_module requests-text}
BuildRequires:  %{python_module toposort}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jinja2
Requires:       python-jinja2-easy.generator
Requires:       python-luadata.luatable
Requires:       python-lupa
Requires:       python-platformdirs
Requires:       python-requests
Requires:       python-requests-glob
Requires:       python-requests-stdin
Requires:       python-requests-text
Requires:       python-toposort
BuildArch:      noarch
%python_subpackages

%description
Generate RPM or DSC spec files from luarocks

%prep
%autosetup -p1 -n lua2pack-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lua2pack
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest


%post
%python_install_alternative lua2pack

%postun
%python_uninstall_alternative lua2pack

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/lua2pack
%{python_sitelib}/lua2pack
%{python_sitelib}/lua2pack-%{version}.dist-info

%changelog
