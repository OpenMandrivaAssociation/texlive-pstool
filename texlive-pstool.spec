Name:		texlive-pstool
Version:	46393
Release:	1
Summary:	Support for psfrag within pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pstool
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package works in the same sort of way as pst-pdf, but it
also processes the PostScript graphics with psfrag to add
labels within the graphic, before conversion. Thus the bundle
replaces two steps of an ordinary workflow. (Naturally, the
package requires that \write 18 is enabled.) Pstool ensures
that each version of each graphic is compiled once only (the
graphic is (re-)compiled only if it has changed since the
previous compilation of the document). This drastically speeds
up the running of the package in the typical case (though the
first run of any document is inevitably just as slow as with
any similar package).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pstool
%doc %{_texmfdistdir}/doc/latex/pstool

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
