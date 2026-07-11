%global tl_name pstool
%global tl_revision 46393

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5e
Release:	%{tl_revision}.1
Summary:	Support for psfrag within pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pstool
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstool.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package works in the same sort of way as pst-pdf, but it also
processes the PostScript graphics with psfrag to add labels within the
graphic, before conversion. Thus the bundle replaces two steps of an
ordinary workflow. (Naturally, the package requires that \write 18 is
enabled.) Pstool ensures that each version of each graphic is compiled
once only (the graphic is (re-)compiled only if it has changed since the
previous compilation of the document). This drastically speeds up the
running of the package in the typical case (though the first run of any
document is inevitably just as slow as with any similar package).

