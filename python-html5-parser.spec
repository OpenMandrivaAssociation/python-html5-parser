%define oname   html5-parser

Name:           python-%{oname}
Version:	0.4.7
Release:	1
Summary:        Fast C based HTML 5 parsing for python

Source0:	https://files.pythonhosted.org/packages/db/92/5cfc34f5f9ff9a43e4d2c8d840f9614dbce5cce86c25505bb4cd76505327/html5-parser-0.4.7.tar.gz
License:        ASL 2.0
Group:          Development/Python
Url:            http://pypi.python.org/pypi/html5-parser/
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools
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
%setup -qc 
mv %{oname}-%{version} python2
cp -a python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python} setup.py install --root=%{buildroot}
popd

%files
%doc python3/LICENSE python3/README.rst
%{py_platsitedir}/html5_parser-%{version}-*.egg-info
%{py_platsitedir}/html5_parser

%files -n python2-html5-parser
%doc python2/LICENSE python2/README.rst
%{py2_platsitedir}/html5_parser-%{version}-*.egg-info
%{py2_platsitedir}/html5_parser

