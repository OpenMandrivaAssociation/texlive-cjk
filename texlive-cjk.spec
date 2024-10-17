Name:		texlive-cjk
Version:	60865
Release:	2
Summary:	CJK language support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/chinese/CJK
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-arphic
Requires:	texlive-cns
Requires:	texlive-garuda-c90
Requires:	texlive-norasi-c90
Requires:	texlive-uhc
Requires:	texlive-wadalab

%description
CJK is a macro package for LaTeX, providing simultaneous
support for various Asian scripts in many encodings (including
Unicode): - Chinese (both traditional and simplified), -
Japanese, - Korean and - Thai. A special add-on feature is an
interface to the Emacs editor (cjk-enc.el) which gives
simultaneous, easy-to-use support to a bunch of other scripts
in addition to the above: - Cyrillic, - Greek, - Latin-based
scripts, - Russian and - Vietnamese.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cjk
%doc %{_texmfdistdir}/doc/latex/cjk
#- source
%doc %{_texmfdistdir}/source/latex/cjk

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
