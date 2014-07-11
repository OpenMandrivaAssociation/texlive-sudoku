# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sudoku
# catalog-date 2007-03-12 11:51:09 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-sudoku
Version:	1.0
Release:	8
Summary:	Create sudoku grids
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sudoku
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The sudoku package provides an environment for typesetting
sudoku grids. A sudoku puzzle is a 9x9 grid where some of the
squares in the grid contain numbers. The rules are simple:
every column can only contain the digits 1 to 9, every row can
only contain the digits 1 to 9 and every 3x3 box can only
contain the digits 1 to 9. More information, including help and
example puzzles, can be found at sudoku.org.uk. This site also
has blank sudoku grids (or worksheets), but you will not need
to print them from there if you have this package installed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sudoku/sudoku.sty
%doc %{_texmfdistdir}/doc/latex/sudoku/CHANGES
%doc %{_texmfdistdir}/doc/latex/sudoku/README
%doc %{_texmfdistdir}/doc/latex/sudoku/sudoku.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sudoku/sudoku.dtx
%doc %{_texmfdistdir}/source/latex/sudoku/sudoku.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756350
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719609
- texlive-sudoku
- texlive-sudoku
- texlive-sudoku
- texlive-sudoku

