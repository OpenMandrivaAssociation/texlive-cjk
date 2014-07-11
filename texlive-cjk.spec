# revision 30576
# category Package
# catalog-ctan /language/chinese/CJK
# catalog-date 2012-05-09 20:27:35 +0200
# catalog-license gpl
# catalog-version 4.8.3
Name:		texlive-cjk
Version:	4.8.3
Release:	8
Summary:	CJK language support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/chinese/CJK
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk.source.tar.xz
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
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42goth.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42goth.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42maru.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42maru.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42min.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c42min.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c52maru.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c52maru.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c52min.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c52min.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70goth.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70goth.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70maru.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70maru.fdx
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70min.fd
%{_texmfdistdir}/tex/latex/cjk/contrib/wadalab/c70min.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/Bg5.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/Bg5.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/Bg5.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/Bg5.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/HK.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bkai.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bkai.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bsmi.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bsmi.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bsmir.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00bsmir.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00cns.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00fs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00kai.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00kair.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00kair.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c00song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c01song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c05song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/Bg5/c09song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CEF/c80song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CEF/c81song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CJK.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/CJK.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKfntef.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKnumb.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKspace.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKulem.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKutf8.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CJKvert.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/EUC-TW.bdg
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/EUC-TW.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/EUC-TW.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c31song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c32song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c33song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c34song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c35song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c36song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/CNS/c37song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/GB.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/GB.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10fs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10gbsn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10gbsn.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10gkai.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10gkai.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c10song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c11song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c19song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c20song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/GB/c21song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/EUC-JP.bdg
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/EUC-JP.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/EUC-JP.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/EUC-JPdnp.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/JIS.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/JIS.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/JISdnp.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/c40song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/c41song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/c42song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/c43song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/JIS/c50song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/HLaTeX.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/KSHL.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63bm.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63dn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63gr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63gs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63gt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63jgt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63jmj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63jnv.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63jsr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63pg.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63pga.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63ph.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63pn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63sh.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63tz.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63vd.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c63yt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64bm.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64dn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64gr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64gs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64gt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64jgt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64jmj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64jnv.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64jsr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64pg.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64pga.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64ph.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64pn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64sh.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64tz.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64vd.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c64yt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65bm.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65dn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65gr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65gs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65gt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65jgt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65jmj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65jnv.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65jsr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65pg.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65pga.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65ph.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65pn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65sh.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65tz.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65vd.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/c65yt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/HLaTeX/pshan.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/KS.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/KS.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60dr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60gr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60gs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60gt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60hgt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60hmj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60hol.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60hpg.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c60mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61dr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61gr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61gs.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61gt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61hgt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61hmj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61hol.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61hpg.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c61mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/c62song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hangul.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hangul.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hangul2.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hangul2.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hanja.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/KS/hanja.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJIS.bdg
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJIS.cap
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJIS.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJIS.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJIS.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJISdnp.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/SJISdnp.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/SJIS/c49song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/UTF8.bdg
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/UTF8.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/UTF8.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70bkai.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70bkai.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70bsmi.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70bsmi.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70gbsn.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70gbsn.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70gkai.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70gkai.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70mj.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70mj.fdx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/c70song.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/ja.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/ko-Hang.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/ko-Hang2.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/ko-Hani.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/zh-Hans.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/UTF8/zh-Hant.cpx
%{_texmfdistdir}/tex/latex/cjk/texinput/extended.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/extended.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/mule/MULEenc.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/pinyin.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/pmC.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/pmCbig.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/pmCsmall.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/ruby.sty
%{_texmfdistdir}/tex/latex/cjk/texinput/standard.bdg
%{_texmfdistdir}/tex/latex/cjk/texinput/standard.chr
%{_texmfdistdir}/tex/latex/cjk/texinput/standard.enc
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90cmr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90cmss.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90cmtt.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90enc.def
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90gar.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/c90nrsr.fd
%{_texmfdistdir}/tex/latex/cjk/texinput/thai/thaicjk.ldf
%{_texmfdistdir}/tex/latex/cjk/utils/pyhyphen/pinyin.ldf
%doc %{_texmfdistdir}/doc/latex/cjk/ChangeLog
%doc %{_texmfdistdir}/doc/latex/cjk/MANIFEST
%doc %{_texmfdistdir}/doc/latex/cjk/Makefile
%doc %{_texmfdistdir}/doc/latex/cjk/README
%doc %{_texmfdistdir}/doc/latex/cjk/TODO
%doc %{_texmfdistdir}/doc/latex/cjk/doc/CEF.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/CJK.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/CJKnumb.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/CJKspace.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/CJKutf8.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/COPYING
%doc %{_texmfdistdir}/doc/latex/cjk/doc/INSTALL
%doc %{_texmfdistdir}/doc/latex/cjk/doc/TDS.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/chinese/README
%doc %{_texmfdistdir}/doc/latex/cjk/doc/chinese/READMEb5.tex
%doc %{_texmfdistdir}/doc/latex/cjk/doc/chinese/READMEgb.tex
%doc %{_texmfdistdir}/doc/latex/cjk/doc/chinese/emTeXb5.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/chinese/teTeXb5.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/cjk-enc.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/cjk/README
%doc %{_texmfdistdir}/doc/latex/cjk/doc/cjk/READMEb5.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/doc/commands.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/dvidrv.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/fdxfiles.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/fonts.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/hbf2gf.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/history.2_5
%doc %{_texmfdistdir}/doc/latex/cjk/doc/history.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/README
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/ascii.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/japanese.jis
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/japanese.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/jp-fonts.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/jp-tex.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/preview.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/japanese/shibuaki.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdf/READMEb5.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdf/READMEgb.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/HOWTO.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/bkai.map
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/cid-x.map
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/cwtb.map
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/dvipdfmx.cfg
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/gen-map.pl
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/map.list
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5/c00cwtb.fd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5/c00tmpl.fd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/texinput/GB/c10tmpl.fd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/texinput/JIS/c40tmpl.fd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/texinput/SJIS/c49tmpl.fd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/updmap.my
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pdfhowto/examples/wcl.sfd
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pinyin.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/pyhyphen.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/reftex.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/ruby.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/thaifont.txt
%doc %{_texmfdistdir}/doc/latex/cjk/doc/vertical.txt
%doc %{_texmfdistdir}/doc/latex/cjk/examples/Big5.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/Big5vert.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CEF_test.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CJKbabel.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CJKfntef.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CJKmixed.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CJKspace.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/CJKutf8.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/GB.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/JIS.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/KS.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/README
%doc %{_texmfdistdir}/doc/latex/cjk/examples/SJIS.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/UTF8.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/Big5.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/Big5vert.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/CEF_test.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/CJKbabel.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/SJIS.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/muletest.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/rubytest.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/cjk/thai.cjk
%doc %{_texmfdistdir}/doc/latex/cjk/examples/muletest.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/Big5.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/Big5vert.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CEF_test.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CJKbabel.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CJKfntef.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CJKmixed.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CJKspace.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/CJKutf8.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/GB.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/JIS.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/KS.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/SJIS.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/UTF8.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/muletest.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/py_test.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/pytest.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/rubytest.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/thai.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/pdf/thai_utf8.pdf
%doc %{_texmfdistdir}/doc/latex/cjk/examples/py_test.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/rubytest.tex
%doc %{_texmfdistdir}/doc/latex/cjk/examples/thai.tex
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/bin-cjkutils.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/c90.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/cjk-build.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/cjk.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/dnp.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/garuda-c90.pl
%doc %{_texmfdistdir}/doc/latex/cjk/texlive/norasi-c90.pl
%doc %{_texmfdistdir}/doc/latex/cjk/utils/pyhyphen/pytest.tex
#- source
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/fixwada
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/fixwada2.pl
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/makefont
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/makeuniwada.pl
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/wadalab.map
%doc %{_texmfdistdir}/source/latex/cjk/contrib/wadalab/wadalab.txt
%doc %{_texmfdistdir}/source/latex/cjk/texinput/KS/HLaTeX/c63mj.fd
%doc %{_texmfdistdir}/source/latex/cjk/texinput/KS/HLaTeX/c64mj.fd
%doc %{_texmfdistdir}/source/latex/cjk/texinput/KS/HLaTeX/c65mj.fd
%doc %{_texmfdistdir}/source/latex/cjk/utils/Bg5conv/bg5conv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/Bg5conv/bg5latex.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/Bg5conv/bg5latex.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cef5conv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cef5ltx.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cef5ltx.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cefconv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/ceflatex.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/ceflatex.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cefsconv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cefsltx.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/CEFconv/cefsltx.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/SJISconv/sjisconv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/SJISconv/sjisltx.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/SJISconv/sjisltx.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/extconv/bg5pltx.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/extconv/bg5pltx.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/extconv/extconv.w
%doc %{_texmfdistdir}/source/latex/cjk/utils/extconv/gbklatex.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/extconv/gbklatex.cmd
%doc %{_texmfdistdir}/source/latex/cjk/utils/f_name.bat
%doc %{_texmfdistdir}/source/latex/cjk/utils/hbf2gf/Makefile.gnu
%doc %{_texmfdistdir}/source/latex/cjk/utils/hbf2gf/Makefile.in
%doc %{_texmfdistdir}/source/latex/cjk/utils/hbf2gf/README
%doc %{_texmfdistdir}/source/latex/cjk/utils/hbf2gf/c-auto.h
%doc %{_texmfdistdir}/source/latex/cjk/utils/hbf2gf/dvidrv.btm
%doc %{_texmfdistdir}/source/latex/cjk/utils/lisp/cjkspace.el
%doc %{_texmfdistdir}/source/latex/cjk/utils/lisp/cjktilde.el
%doc %{_texmfdistdir}/source/latex/cjk/utils/lisp/emacs/cjk-enc.el
%doc %{_texmfdistdir}/source/latex/cjk/utils/lisp/emacs/thai-word.el
%doc %{_texmfdistdir}/source/latex/cjk/utils/lisp/mule-2.3/cjk-enc.el
%doc %{_texmfdistdir}/source/latex/cjk/utils/pyhyphen/pinyin.c
%doc %{_texmfdistdir}/source/latex/cjk/utils/pyhyphen/pinyin.tr
%doc %{_texmfdistdir}/source/latex/cjk/utils/pyhyphen/pyhyph.tex
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/clonevf.pl
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/hlatex2agl.pl
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/makefdx.pl
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/sfd2uni.pl
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/subfonts.pe
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/uni2sfd.pl
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/vertical.pe
%doc %{_texmfdistdir}/source/latex/cjk/utils/subfonts/vertref.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
