# Typoglycemia

A [typoglycemic](https://en.wikipedia.org/wiki/Typoglycemia) word jumbler written in Python, with several options.

This script was written hastily over the course of a few hours, so it's not very robust and hasn't been thoroughly tested. It has no requirements other than built-in Python modules.

## Usage

```
Supply input through stdin.

Options:
h       Print this help page
f       Preserve first letter
f[n]    Preserve first n letters
l       Preserve last letter
l[n]    Preserve last n letters
k[n]    Preserve ("keep") at least n additional letters
%[n]    Preserve at least an additional n% of letters
d[n]    Restrict letter travel distance to a maximum of n

Options can be strung together or separated by whitespace; e.g.
f2ld3
f2 l d3
fl %50 k2

Behavior for redundant or invalid options is unspecified. All options are
case-insensitive. Only integers are allowed at this time.

Be wary of using low d[n] values with long words. This option is implemented
very poorly and can be extremely slow.
```

In most terminals, use ctrl-D to close stdin when typing text manually.

## Example

### Example 1

Jumble the sample text, preserving the first and last letters:

`cat sample.txt | python3 jumble-text.py fl`

```
Tcoymipyglea is a nsoigloem for a puteorprd rcenet dseicvroy aobut the cvointgie
posscrees bhiend rinaedg werttin text. The wrod aprapes to be a pemoratantu of
"typo", as in tpagahproycil erorr, and "hplyiocegmya". It is an ubran
legend/Ieenrtnt meme taht aerapps to hvae an eemlnet of tutrh to it.[1] No such
rearsech was creriad out at the Uitvnsriey of Crdbiagme.[1]

An eaxmple of this text, as cteuralcid in Sepemtebr 2003, raeds as fwlolos:

Arcnocidg to a rhseaecrer at Cgrmbiade Uiesvtnriy, it dosen't mtetar in what
order the lrteets in a wrod are, the olny imtonaprt thnig is that the frsit and
last leettr be at the rihgt plcae. The rest can be a ttaol mses and you can
sltil raed it whotuit plorebm. This is bsuaece the hmuan mind does not raed
eervy leettr by iestlf, but the word as a whloe.

— Mtat Daivs, MRC Cgiotonin and Biran Seccnies, "Rdinaeg jmlebud ttexs",
hptts://www.mrc-cbu.cam.ac.uk/ppoele/mtat.diavs/cibragdme/ A few mteksais wree
mdae:

The wrod "rehreacesr" looekd like "rrcecaeshh" was srbceamld, wtih "er" bnieg
rcpealed wtih "ch"; The wrod "irmanoptt" lekood lkie "iopemnrtt", a mislpienslg
of the word, was smcreblad. Tsehe emails may have been ipinresd by a ltteer to
New Sstcineit in 1999[2] from Gaharm Rloaiwsnn of the Uientrsviy of Ntoahgitnm
in wihch he dieucssss his 1976 Ph.D. teihss[3] or phrpeas by the rrecaesh of
Tmhoas R. Jradon's gruop on the rlvteiae iunfcleens of the eitxreor and iinteror
lterets of wdros.[4]

https://en.wkiepiida.org/wkii/Typlcemgyoia (jembuld portion was ulneujmbd)
```

### Example 2

Jumble the sample text, preserving the first two letters and at least 50% of the other letters:

`cat sample.txt | python3 jumble-text.py f2 %50`

```
Tyeoglyicpma is a nemlogiso for a purrdotep rectne discoveyr abuot the cogiivnte
prosessce behind reidang wrttien text. The word apperas to be a poratmnueat of
"typo", as in typairapogchl error, and "hygoplcyemia". It is an urbna
legend/Intrenet meme that appaers to have an eletenm of truth to it.[1] No such
rereasch was carerid out at the Unyvsriite of Cambeigdr.[1]

An exapmle of this text, as circtualed in Sebteepmr 2003, reads as follosw:

Accorgind to a reseahcrer at Camdriegb Univetsyri, it doesn't maettr in what
order the letesrt in a word are, the only imnorpatt thing is that the firts and
last leettr be at the right place. The rest can be a toatl mess and you can
stlil read it witohut problem. This is beacuse the humna mind does not read
evrey letter by itself, but the word as a whole.

— Matt Davsi, MRC Cognniiot and Brain Scseicen, "Reading jubmled testx",
https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmbdriage/ A few miskates were
made:

The word "reseaechrr" looked like "rereahchsc" was sclaebrmd, with "er" begni
replaced with "ch"; The word "impotrant" looked like "imoprtent", a milgpeslins
of the word, was scrambled. These emails may have been inepirsd by a lertet to
New Scisntiet in 1999[2] from Graham Ralwiosnn of the Unisetviry of Nohginttam
in which he discusses his 1976 Ph.D. thseis[3] or perhaps by the research of
Thoams R. Jordan's gropu on the relative influensec of the exiertor and inoeritr
letters of words.[4]

htspt://en.wieiipdka.org/wiki/Tylopcyiemga (juebldm pontiro was undumblej)
```

### Example 3

Jumble the sample text, ensuring that no letter is moved more than 3 spaces away
from its origin:

`cat sample.txt | python3 jumble-text.py d3`

```
Toygcplyiema is a olnesomgi fro a upprotder cernet dicosyevr utaob eth gociinvte
rcepsoess hbendi erdagin wirntet ttex. eTh rdow paesrpa ot eb a otaptrmenau of
"oypt", as in ptgoyrapichla rrreo, nad "yholcpegiyam". tI is an rnaub
elegnd/tInenert mmee ttah aapepsr ot veah na eeenlmt of ruhtt ot ti.[1] oN cshu
eresharc wsa caeridr uot ta het nUveiityrs fo Crmbaedig.[1]

nA xelapem of hsit text, sa circaeudlt in etSpeberm 2003, esrad sa olflswo:

coArcgnid ot a srecerraeh at Camdbrgie ineUivryts, ti dones't tarmet ni what
redor het tetlesr ni a rowd era, eht oyln imptotrna tghin is ttha het frsti dan
atsl eltter eb ta eth grthi caepl. Teh setr anc be a toatl ssme adn oyu anc
sitll erda ti hoiwtut oprlmbe. hsiT si cbaeseu the muhna inmd osde nto rdea
reyve lteret by telisf, utb hte owrd sa a owhel.

— Mtta Diasv, CRM giConniot dna rinBa Secenisc, "eRidnag umjbeld estxt",
thpts://www.mcr-bcu.mca.ca.ku/ppeloe/matt.vdisa/bacmdeirg/ A wfe itmasske rwee
emad:

eTh owrd "sreeacrher" lkoeod leki "rseechrahc" asw armscedlb, iwht "er" bnieg
lercdpae whti "hc"; heT dwro "oimrpntat" lodkoe ikel "opimrettn", a misepslgiln
fo het orwd, saw csmarldbe. seThe emasli aym vaeh nebe ipneisrd by a eerltt ot
weN Scteitnis in 1999[2] orfm haGram aiRwlnnso of eht nUievtrsyi fo tNtoinhamg
ni hcwhi he sdciusess his 1976 Ph.D. stheis[3] or parehps yb eth esrreahc of
mhoTas R. roaJnd's gporu on het ltreiave nifelcsuen of the eerxitro nda tneiroir
teelstr fo rwdos.[4]

tthps://ne.wkeiipiad.rgo/kiwi/pTyoglcmyiea (mjelubd potnroi saw jumnubled)
```
