# Generated from d:\HK221\PPL\ass1\initial\assignment1\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01d1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3*\3*")
        buf.write("\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\5\66")
        buf.write("\u0152\n\66\3\67\6\67\u0155\n\67\r\67\16\67\u0156\38\3")
        buf.write("8\58\u015b\n8\39\69\u015e\n9\r9\169\u015f\39\39\79\u0164")
        buf.write("\n9\f9\169\u0167\139\59\u0169\n9\39\39\59\u016d\n9\39")
        buf.write("\69\u0170\n9\r9\169\u0171\3:\6:\u0175\n:\r:\16:\u0176")
        buf.write("\3:\3:\7:\u017b\n:\f:\16:\u017e\13:\3;\3;\7;\u0182\n;")
        buf.write("\f;\16;\u0185\13;\3;\3;\3;\3<\3<\7<\u018c\n<\f<\16<\u018f")
        buf.write("\13<\3=\3=\5=\u0193\n=\3=\3=\3>\6>\u0198\n>\r>\16>\u0199")
        buf.write("\3>\3>\3?\3?\7?\u01a0\n?\f?\16?\u01a3\13?\3?\3?\3@\3@")
        buf.write("\7@\u01a9\n@\f@\16@\u01ac\13@\3@\3@\3@\3A\3A\3A\3A\7A")
        buf.write("\u01b5\nA\fA\16A\u01b8\13A\3A\3A\3A\3B\3B\7B\u01bf\nB")
        buf.write("\fB\16B\u01c2\13B\3C\3C\3C\5C\u01c7\nC\3D\3D\3D\3D\5D")
        buf.write("\u01cd\nD\3E\3E\3E\3\u01b6\2F\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089B\3\2\f\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f")
        buf.write("\f\17\17\t\2$$^^ddhhppttvv\6\2\f\f\17\17$$^^\3\2$$\2\u01e0")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u0093\3\2\2\2\7\u0099\3\2\2\2\t\u009f\3\2\2")
        buf.write("\2\13\u00a8\3\2\2\2\r\u00ab\3\2\2\2\17\u00b0\3\2\2\2\21")
        buf.write("\u00b8\3\2\2\2\23\u00be\3\2\2\2\25\u00c1\3\2\2\2\27\u00c5")
        buf.write("\3\2\2\2\31\u00cc\3\2\2\2\33\u00d1\3\2\2\2\35\u00d5\3")
        buf.write("\2\2\2\37\u00dc\3\2\2\2!\u00e1\3\2\2\2#\u00e7\3\2\2\2")
        buf.write("%\u00ec\3\2\2\2\'\u00f0\3\2\2\2)\u00f5\3\2\2\2+\u00fb")
        buf.write("\3\2\2\2-\u0102\3\2\2\2/\u0105\3\2\2\2\61\u010c\3\2\2")
        buf.write("\2\63\u010e\3\2\2\2\65\u0110\3\2\2\2\67\u0112\3\2\2\2")
        buf.write("9\u0114\3\2\2\2;\u0116\3\2\2\2=\u0118\3\2\2\2?\u011b\3")
        buf.write("\2\2\2A\u011e\3\2\2\2C\u0120\3\2\2\2E\u0122\3\2\2\2G\u0125")
        buf.write("\3\2\2\2I\u0128\3\2\2\2K\u012b\3\2\2\2M\u012e\3\2\2\2")
        buf.write("O\u0130\3\2\2\2Q\u0132\3\2\2\2S\u0136\3\2\2\2U\u0138\3")
        buf.write("\2\2\2W\u013b\3\2\2\2Y\u013d\3\2\2\2[\u013f\3\2\2\2]\u0141")
        buf.write("\3\2\2\2_\u0143\3\2\2\2a\u0145\3\2\2\2c\u0147\3\2\2\2")
        buf.write("e\u0149\3\2\2\2g\u014b\3\2\2\2i\u014d\3\2\2\2k\u0151\3")
        buf.write("\2\2\2m\u0154\3\2\2\2o\u015a\3\2\2\2q\u015d\3\2\2\2s\u0174")
        buf.write("\3\2\2\2u\u017f\3\2\2\2w\u0189\3\2\2\2y\u0192\3\2\2\2")
        buf.write("{\u0197\3\2\2\2}\u019d\3\2\2\2\177\u01a6\3\2\2\2\u0081")
        buf.write("\u01b0\3\2\2\2\u0083\u01bc\3\2\2\2\u0085\u01c6\3\2\2\2")
        buf.write("\u0087\u01cc\3\2\2\2\u0089\u01ce\3\2\2\2\u008b\u008c\7")
        buf.write("d\2\2\u008c\u008d\7q\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7n\2\2\u008f\u0090\7g\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7p\2\2\u0092\4\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097\7c\2\2\u0097\u0098")
        buf.write("\7m\2\2\u0098\6\3\2\2\2\u0099\u009a\7e\2\2\u009a\u009b")
        buf.write("\7n\2\2\u009b\u009c\7c\2\2\u009c\u009d\7u\2\2\u009d\u009e")
        buf.write("\7u\2\2\u009e\b\3\2\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\n\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\f\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7g\2\2\u00af\16")
        buf.write("\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7z\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7f\2\2\u00b6\u00b7\7u\2\2\u00b7\20\3\2\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7v\2\2\u00bd\22\3\2\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7h\2\2\u00c0\24\3\2\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\26")
        buf.write("\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\30\3\2\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7j\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7p\2\2\u00d0\32")
        buf.write("\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da")
        buf.write("\7t\2\2\u00da\u00db\7p\2\2\u00db\36\3\2\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\"\3\2\2\2\u00e7\u00e8\7x\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7f\2\2\u00eb$\3")
        buf.write("\2\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7n\2\2\u00ef&\3\2\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7j\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7u\2\2\u00f4(\3")
        buf.write("\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7n\2\2\u00fa*\3")
        buf.write("\2\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7e\2\2\u0101,\3\2\2\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104.\3\2\2\2\u0105\u0106\7f\2\2\u0106\u0107")
        buf.write("\7q\2\2\u0107\u0108\7y\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7q\2\2\u010b\60\3\2\2\2\u010c\u010d")
        buf.write("\7-\2\2\u010d\62\3\2\2\2\u010e\u010f\7/\2\2\u010f\64\3")
        buf.write("\2\2\2\u0110\u0111\7,\2\2\u0111\66\3\2\2\2\u0112\u0113")
        buf.write("\7\61\2\2\u01138\3\2\2\2\u0114\u0115\7^\2\2\u0115:\3\2")
        buf.write("\2\2\u0116\u0117\7\'\2\2\u0117<\3\2\2\2\u0118\u0119\7")
        buf.write("#\2\2\u0119\u011a\7?\2\2\u011a>\3\2\2\2\u011b\u011c\7")
        buf.write("?\2\2\u011c\u011d\7?\2\2\u011d@\3\2\2\2\u011e\u011f\7")
        buf.write(">\2\2\u011fB\3\2\2\2\u0120\u0121\7@\2\2\u0121D\3\2\2\2")
        buf.write("\u0122\u0123\7>\2\2\u0123\u0124\7?\2\2\u0124F\3\2\2\2")
        buf.write("\u0125\u0126\7@\2\2\u0126\u0127\7?\2\2\u0127H\3\2\2\2")
        buf.write("\u0128\u0129\7~\2\2\u0129\u012a\7~\2\2\u012aJ\3\2\2\2")
        buf.write("\u012b\u012c\7(\2\2\u012c\u012d\7(\2\2\u012dL\3\2\2\2")
        buf.write("\u012e\u012f\7#\2\2\u012fN\3\2\2\2\u0130\u0131\7`\2\2")
        buf.write("\u0131P\3\2\2\2\u0132\u0133\7p\2\2\u0133\u0134\7g\2\2")
        buf.write("\u0134\u0135\7y\2\2\u0135R\3\2\2\2\u0136\u0137\7?\2\2")
        buf.write("\u0137T\3\2\2\2\u0138\u0139\7<\2\2\u0139\u013a\7?\2\2")
        buf.write("\u013aV\3\2\2\2\u013b\u013c\7]\2\2\u013cX\3\2\2\2\u013d")
        buf.write("\u013e\7_\2\2\u013eZ\3\2\2\2\u013f\u0140\7}\2\2\u0140")
        buf.write("\\\3\2\2\2\u0141\u0142\7\177\2\2\u0142^\3\2\2\2\u0143")
        buf.write("\u0144\7*\2\2\u0144`\3\2\2\2\u0145\u0146\7+\2\2\u0146")
        buf.write("b\3\2\2\2\u0147\u0148\7=\2\2\u0148d\3\2\2\2\u0149\u014a")
        buf.write("\7<\2\2\u014af\3\2\2\2\u014b\u014c\7\60\2\2\u014ch\3\2")
        buf.write("\2\2\u014d\u014e\7.\2\2\u014ej\3\2\2\2\u014f\u0152\5\37")
        buf.write("\20\2\u0150\u0152\5!\21\2\u0151\u014f\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152l\3\2\2\2\u0153\u0155\t\2\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157n\3\2\2\2\u0158\u015b\5q9\2\u0159")
        buf.write("\u015b\5s:\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("p\3\2\2\2\u015c\u015e\t\2\2\2\u015d\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0168\3\2\2\2\u0161\u0165\7\60\2\2\u0162\u0164")
        buf.write("\t\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0169\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0168\u0161\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\t\3\2\2\u016b\u016d")
        buf.write("\t\4\2\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016f\3\2\2\2\u016e\u0170\t\2\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172r\3\2\2\2\u0173\u0175\t\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017c\7\60\2")
        buf.write("\2\u0179\u017b\t\2\2\2\u017a\u0179\3\2\2\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("t\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0183\7$\2\2\u0180")
        buf.write("\u0182\5\u0085C\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2")
        buf.write("\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\7$\2\2\u0187")
        buf.write("\u0188\b;\2\2\u0188v\3\2\2\2\u0189\u018d\t\5\2\2\u018a")
        buf.write("\u018c\t\6\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018ex\3\2\2")
        buf.write("\2\u018f\u018d\3\2\2\2\u0190\u0193\5\u0081A\2\u0191\u0193")
        buf.write("\5\u0083B\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0195\b=\3\2\u0195z\3\2\2\2\u0196")
        buf.write("\u0198\t\7\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019c\b>\3\2\u019c|\3\2\2\2\u019d\u01a1\7")
        buf.write("$\2\2\u019e\u01a0\5\u0085C\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b")
        buf.write("?\4\2\u01a5~\3\2\2\2\u01a6\u01aa\7$\2\2\u01a7\u01a9\5")
        buf.write("\u0085C\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2")
        buf.write("\u01ac\u01aa\3\2\2\2\u01ad\u01ae\5\u0087D\2\u01ae\u01af")
        buf.write("\b@\5\2\u01af\u0080\3\2\2\2\u01b0\u01b1\7\61\2\2\u01b1")
        buf.write("\u01b2\7,\2\2\u01b2\u01b6\3\2\2\2\u01b3\u01b5\13\2\2\2")
        buf.write("\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b9\u01ba\7,\2\2\u01ba\u01bb\7\61\2\2\u01bb")
        buf.write("\u0082\3\2\2\2\u01bc\u01c0\7%\2\2\u01bd\u01bf\n\b\2\2")
        buf.write("\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u0084\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3\u01c4\7^\2\2\u01c4\u01c7\t\t\2\2\u01c5")
        buf.write("\u01c7\n\n\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7\u0086\3\2\2\2\u01c8\u01c9\7^\2\2\u01c9\u01cd\n")
        buf.write("\t\2\2\u01ca\u01cb\7)\2\2\u01cb\u01cd\n\13\2\2\u01cc\u01c8")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u0088\3\2\2\2\u01ce")
        buf.write("\u01cf\13\2\2\2\u01cf\u01d0\bE\6\2\u01d0\u008a\3\2\2\2")
        buf.write("\27\2\u0151\u0156\u015a\u015f\u0165\u0168\u016c\u0171")
        buf.write("\u0176\u017c\u0183\u018d\u0192\u0199\u01a1\u01aa\u01b6")
        buf.write("\u01c0\u01c6\u01cc\7\3;\2\b\2\2\3?\3\3@\4\3E\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    STRING = 11
    THEN = 12
    FOR = 13
    RETURN = 14
    TRUE = 15
    FALSE = 16
    VOID = 17
    NIL = 18
    THIS = 19
    FINAL = 20
    STATIC = 21
    TO = 22
    DOWNTO = 23
    ADD = 24
    SUB = 25
    MUL = 26
    FLOAT_DIV = 27
    INT_DIV = 28
    MOD = 29
    NEQ = 30
    EQ = 31
    LT = 32
    GT = 33
    LTE = 34
    GTE = 35
    OR = 36
    AND = 37
    NOT = 38
    CONCAT = 39
    NEW = 40
    ASSIGN = 41
    ASSIGN_EQ = 42
    LSB = 43
    RSB = 44
    LP = 45
    RP = 46
    LB = 47
    RB = 48
    SEMI = 49
    COLON = 50
    DOT = 51
    COMMA = 52
    BOOL_LIT = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    FLOAT_LIT_case1 = 56
    FLOAT_LIT_case2 = 57
    STRING_LIT = 58
    ID = 59
    COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'string'", "'then'", 
            "'for'", "'return'", "'true'", "'false'", "'void'", "'nil'", 
            "'this'", "'final'", "'static'", "'to'", "'downto'", "'+'", 
            "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", 
            "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "'new'", "'='", 
            "':='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "STRING", "THEN", "FOR", "RETURN", "TRUE", 
            "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
            "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", "NEQ", "EQ", 
            "LT", "GT", "LTE", "GTE", "OR", "AND", "NOT", "CONCAT", "NEW", 
            "ASSIGN", "ASSIGN_EQ", "LSB", "RSB", "LP", "RP", "LB", "RB", 
            "SEMI", "COLON", "DOT", "COMMA", "BOOL_LIT", "INT_LIT", "FLOAT_LIT", 
            "FLOAT_LIT_case1", "FLOAT_LIT_case2", "STRING_LIT", "ID", "COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "STRING", "THEN", "FOR", 
                  "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
                  "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLOAT_DIV", 
                  "INT_DIV", "MOD", "NEQ", "EQ", "LT", "GT", "LTE", "GTE", 
                  "OR", "AND", "NOT", "CONCAT", "NEW", "ASSIGN", "ASSIGN_EQ", 
                  "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", "COLON", 
                  "DOT", "COMMA", "BOOL_LIT", "INT_LIT", "FLOAT_LIT", "FLOAT_LIT_case1", 
                  "FLOAT_LIT_case2", "STRING_LIT", "ID", "COMMENT", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "STR_CHAR", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.STRING_LIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    raise UncloseString(y)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    y = str(self.text)
                    raise IllegalEscape(y)
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ErrorToken(self.text)
                
     


