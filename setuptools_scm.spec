#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools_scm
Version  : 6.3.1
Release  : 98
URL      : https://files.pythonhosted.org/packages/4e/62/056c0127bf45c493168167aed15c4ccb70d2c69154fb1f4acaffc2bab761/setuptools_scm-6.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/62/056c0127bf45c493168167aed15c4ccb70d2c69154fb1f4acaffc2bab761/setuptools_scm-6.3.1.tar.gz
Summary  : the blessed package to manage your versions by scm tags
Group    : Development/Tools
License  : MIT
Requires: setuptools_scm-license = %{version}-%{release}
Requires: setuptools_scm-python = %{version}-%{release}
Requires: setuptools_scm-python3 = %{version}-%{release}
Requires: packaging
Requires: setuptools
Requires: tomli
BuildRequires : buildreq-distutils3
BuildRequires : packaging
BuildRequires : setuptools
BuildRequires : tomli

%description
setuptools_scm
==============
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
Provides: pypi(setuptools_scm)
Requires: pypi(packaging)
Requires: pypi(setuptools)
Requires: pypi(tomli)

%description python3
python3 components for the setuptools_scm package.


%prep
%setup -q -n setuptools_scm-6.3.1
cd %{_builddir}/setuptools_scm-6.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630687188
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
cp %{_builddir}/setuptools_scm-6.3.1/LICENSE %{buildroot}/usr/share/package-licenses/setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
