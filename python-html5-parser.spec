%define oname   html5-parser

Name:           python-%{oname}
Version:	0.4.10
Release:	1
Summary:        Fast C based HTML 5 parsing for python

Source0:	https://files.pythonhosted.org/packages/source/h/html5-parser/html5-parser-%{version}.tar.gz
License:        ASL 2.0
Group:          Development/Python
Url:            http://pypi.python.org/pypi/html5-parser/
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:	pkgconfig(libxml-2.0)

%description
A fast implementation of the HTML 5 parsing spec for Python. 
Parsing is done in C using a variant of the gumbo parser.
The gumbo parse tree is then transformed into an lxml tree,
also in C, yielding parse times that can be a thirtieth of
the html5lib parse times. That is a speedup of 30x.  This
differs, for instance, from the gumbo python bindings, where 
the initial parsing is done in C but the transformation into
the final tree is done in python.

%package -n python2-html5-parser
Summary: %{summary}

%description -n python2-html5-parser
A fast implementation of the HTML 5 parsing spec for Python 2. 
Parsing is done in C using a variant of the gumbo parser.
The gumbo parse tree is then transformed into an lxml tree,
also in C, yielding parse times that can be a thirtieth of
the html5lib parse times. That is a speedup of 30x.  This
differs, for instance, from the gumbo python bindings, where 
the initial parsing is done in C but the transformation into
the final tree is done in python.

%prep
%setup -qn %{oname}-%{version}

%build
python3 setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%doc LICENSE README.rst
%{py_platsitedir}/html5_parser-%{version}-*.egg-info
%{py_platsitedir}/html5_parser
