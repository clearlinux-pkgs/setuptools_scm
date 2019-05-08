#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools_scm
Version  : 3.3.0
Release  : 64
URL      : https://files.pythonhosted.org/packages/31/c4/18481dd3d0ca210d78c265bac3352a37b491fa19346af19ebb7562d0de15/setuptools_scm-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/c4/18481dd3d0ca210d78c265bac3352a37b491fa19346af19ebb7562d0de15/setuptools_scm-3.3.0.tar.gz
Summary  : the blessed package to manage your versions by scm tags
Group    : Development/Tools
License  : MIT
Requires: setuptools_scm-license = %{version}-%{release}
Requires: setuptools_scm-python = %{version}-%{release}
Requires: setuptools_scm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev
BuildRequires : setuptools-legacypython
BuildRequires : setuptools_scm

%description
setuptools_scm
===============
``setuptools_scm`` handles managing your Python package versions
in SCM metadata instead of declaring them as the version argument
or in a SCM managed file.

%package license
Summary: license components for the setuptools_scm package.
Group: Default

%description license
license components for the setuptools_scm package.


%package python
Summary: python components for the setuptools_scm package.
Group: Default
Requires: setuptools_scm-python3 = %{version}-%{release}

%description python
python components for the setuptools_scm package.


%package python3
Summary: python3 components for the setuptools_scm package.
Group: Default
Requires: python3-core

%description python3
python3 components for the setuptools_scm package.


%prep
%setup -q -n setuptools_scm-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557285383
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools_scm
cp LICENSE %{buildroot}/usr/share/package-licenses/setuptools_scm/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools_scm/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
