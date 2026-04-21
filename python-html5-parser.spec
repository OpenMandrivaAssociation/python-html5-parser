%define module html5-parser
%define oname html5_parser

Name:		python-html5-parser
Version:	0.4.12
Release:	3
Summary:	Fast C based HTML 5 parsing for python
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.python.org/pypi/html5-parser/
Source0:	https://files.pythonhosted.org/packages/source/h/%{module}/%{module}-%{version}.tar.gz

# python-lxml and html5-parser require to be built using the same versions of
# libxml2 in order for html5-parser to not emit runtime errors and for its
# tests to complete.
# Packages that consume them such as calibre will either fail to start or emit
# runtime errors when doing basic operations.
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	python%{pyver}dist(beautifulsoup4)
BuildRequires:	python%{pyver}dist(chardet)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A fast implementation of the HTML 5 parsing spec for Python. 
Parsing is done in C using a variant of the gumbo parser.
The gumbo parse tree is then transformed into an lxml tree,
also in C, yielding parse times that can be a thirtieth of
the html5lib parse times. That is a speedup of 30x.  This
differs, for instance, from the gumbo python bindings, where 
the initial parsing is done in C but the transformation into
the final tree is done in python.

%prep -a
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
# Remove shebangs from library files
sed -i -e '/^#!\//, 1d' src/html5_parser/*.py

%check
export PYTHONPATH="%{buildroot}%{python_sitearch}"
%{__python} setup.py test

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/%{oname}
%{python_sitearch}/%{oname}-%{version}*.*-info
