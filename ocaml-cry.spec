%define debug_package %{nil}

Name:     ocaml-cry

Version:  0.6.2
Release:  0.0%{dist}
Summary:  OCaml icecast/shoutcast lib
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-cry
Source0:  https://github.com/savonet/ocaml-cry/releases/download/%{version}/ocaml-cry-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/cry/META
/usr/lib64/ocaml/cry/cry.a
/usr/lib64/ocaml/cry/cry.cma
/usr/lib64/ocaml/cry/cry.cmi
/usr/lib64/ocaml/cry/cry.cmx
/usr/lib64/ocaml/cry/cry.cmxa
/usr/lib64/ocaml/cry/cry.mli
/usr/lib64/ocaml/cry/cry_ssl.cmi
/usr/lib64/ocaml/cry/cry_ssl.cmx

%description
OCaml low level implementation of the shout protocol.

%changelog
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.6.2-0.0
- Clean up Release tag
- Fix Fedora Rawhide build

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-cry.spec
