from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
a = SeqRecord(Seq("CDABBAFCDB1AAEAA-CEDA-EQ-CDABABABALF4LBBAFBSBAAAAA"), id="Alpha")
b = SeqRecord(Seq("2AABBAFCDABA-EAABCEDCDEQFCDABA-APALF4-BBA--SBAAAAA"), id="Beta")
c = SeqRecord(Seq("--AABA-CDB-AAEAA-CEDCDEQ-CDABPBA-ABF4-BBAFBSBMAAAA"), id="Gamma")
d = SeqRecord(Seq("A-ABBAFCDABA-EAA-CEDCDEQA--ABFBAN--F4-BBAFBTYBAAAA"), id="Delta")
e = SeqRecord(Seq("A-ABNBAFCD-BAAEAABCEDA-EQ-CDABAB--BAF4NBBM-BTYBAAAA"), id="Epsilon")
align = MultipleSeqAlignment([a, b, c, d, e])
print(align)