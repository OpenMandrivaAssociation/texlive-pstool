# revision 29343
# category Package
# catalog-ctan /macros/latex/contrib/pstool
# catalog-date 2013-03-11 10:36:18 +0100
# catalog-license lppl
# catalog-version 1.5a
Name:		texlive-pstool
Version:	1.5a
Release:	1
Summary:	Support for psfrag within pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pstool
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.source.tar.xz
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
%{_texmfdistdir}/tex/latex/pstool/pstool.sty
%doc %{_texmfdistdir}/doc/latex/pstool/README
%doc %{_texmfdistdir}/doc/latex/pstool/example-blx.bib
%doc %{_texmfdistdir}/doc/latex/pstool/example-pstool.tex
%doc %{_texmfdistdir}/doc/latex/pstool/example.aux
%doc %{_texmfdistdir}/doc/latex/pstool/example.bbl
%doc %{_texmfdistdir}/doc/latex/pstool/example.blg
%doc %{_texmfdistdir}/doc/latex/pstool/example.log
%doc %{_texmfdistdir}/doc/latex/pstool/example.pdf
%doc %{_texmfdistdir}/doc/latex/pstool/example.run.xml
%doc %{_texmfdistdir}/doc/latex/pstool/example.synctex
%doc %{_texmfdistdir}/doc/latex/pstool/example.tex
%doc %{_texmfdistdir}/doc/latex/pstool/macros.tex
%doc %{_texmfdistdir}/doc/latex/pstool/pstool.pdf
%doc %{_texmfdistdir}/doc/latex/pstool/pstool.sty
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool-blx.bib
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.aux
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.bbl
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.dvi
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.log
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.ps
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.run.xml
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag-pstool.tex
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag.eps
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag.pdf
%doc %{_texmfdistdir}/doc/latex/pstool/subdir/trial2-psfrag.tex
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool-blx.bib
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.aux
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.bbl
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.dvi
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.log
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.ps
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.run.xml
%doc %{_texmfdistdir}/doc/latex/pstool/trial-pstool.tex
%doc %{_texmfdistdir}/doc/latex/pstool/trial.eps
%doc %{_texmfdistdir}/doc/latex/pstool/trial.pdf
%doc %{_texmfdistdir}/doc/latex/pstool/trial.tex
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool-blx.bib
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.aux
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.bbl
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.dvi
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.log
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.ps
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.run.xml
%doc %{_texmfdistdir}/doc/latex/pstool/trial2-pstool.tex
%doc %{_texmfdistdir}/doc/latex/pstool/trial2.eps
%doc %{_texmfdistdir}/doc/latex/pstool/trial2.pdf
%doc %{_texmfdistdir}/doc/latex/pstool/trial2.tex
#- source
%doc %{_texmfdistdir}/source/latex/pstool/pstool.ins
%doc %{_texmfdistdir}/source/latex/pstool/pstool.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
