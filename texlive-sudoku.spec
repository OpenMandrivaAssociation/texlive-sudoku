%global tl_name sudoku
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Create sudoku grids
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sudoku
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sudoku.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The sudoku package provides an environment for typesetting sudoku grids.
A sudoku puzzle is a 9x9 grid where some of the squares in the grid
contain numbers. The rules are simple: every column can only contain the
digits 1 to 9, every row can only contain the digits 1 to 9 and every
3x3 box can only contain the digits 1 to 9. More information, including
help and example puzzles, can be found at sudoku.org.uk. This site also
has blank sudoku grids (or worksheets), but you will not need to print
them from there if you have this package installed.

