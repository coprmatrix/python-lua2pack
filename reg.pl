my $name = <<'EOF';
%files -n %{python_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%ghost %{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/__init__.py
%{python3_sitelib}/%{pypi_name}/__pycache__/*
%{python3_sitelib}/%{pypi_name}/lua_runtime.py
%{python3_sitelib}/%{pypi_name}/osdeps/__init__.py
%{python3_sitelib}/%{pypi_name}/osdeps/__pycache__/*
%{python3_sitelib}/%{pypi_name}/osdeps/generic.py
%{python3_sitelib}/%{pypi_name}/osdeps/lua_rockspec.py
%{python3_sitelib}/%{pypi_name}/osdeps/obsinfo.py
%{python3_sitelib}/%{pypi_name}/osdeps_utils.py
%{python3_sitelib}/%{pypi_name}/templates/generic.spec
%{python3_sitelib}/%{pypi_name}/templates/obs.obsinfo
%{python3_sitelib}/%{pypi_name}/templates/rock.rockspec
EOF

s/%files -n %{python_name}.*/${name}/g;
