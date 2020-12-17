#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools_scm
Version  : 5.0.1
Release  : 89
URL      : https://files.pythonhosted.org/packages/af/df/f8aa8a78d4d29e0cffa4512e9bc223ed02f24893fe1837c6cee2749ebd67/setuptools_scm-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/df/f8aa8a78d4d29e0cffa4512e9bc223ed02f24893fe1837c6cee2749ebd67/setuptools_scm-5.0.1.tar.gz
Summary  : the blessed package to manage your versions by scm tags
Group    : Development/Tools
License  : MIT
Requires: setuptools_scm-license = %{version}-%{release}
Requires: setuptools_scm-python = %{version}-%{release}
Requires: setuptools_scm-python3 = %{version}-%{release}
Requires: setuptools
Requires: toml
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : toml

%description
==============
        
        ``setuptools_scm`` handles managing your Python package versions
        in SCM metadata instead of declaring them as the version argument
        or in a SCM managed file.
        
        Additionally ``setuptools_scm`` provides setuptools with a list of files that are managed by the SCM
        (i.e. it automatically adds all of the SCM-managed files to the sdist).
        Unwanted files must be excluded by discarding them via ``MANIFEST.in``.

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
Requires: pypi(setuptools)

%description python3
python3 components for the setuptools_scm package.


%prep
%setup -q -n setuptools_scm-5.0.1
cd %{_builddir}/setuptools_scm-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608171947
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
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
cp %{_builddir}/setuptools_scm-5.0.1/LICENSE %{buildroot}/usr/share/package-licenses/setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
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
