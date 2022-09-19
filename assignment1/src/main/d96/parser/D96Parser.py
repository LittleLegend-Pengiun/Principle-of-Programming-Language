# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0266\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\6\2\u0092\n\2\r\2\16\2\u0093")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u009c\n\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\7\4\u00a3\n\4\f\4\16\4\u00a6\13\4\3\5\3\5\5\5\u00aa")
        buf.write("\n\5\3\6\3\6\3\6\5\6\u00af\n\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00bf\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00cb\n\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d8\n\r")
        buf.write("\3\16\3\16\3\16\5\16\u00dd\n\16\3\17\3\17\3\17\5\17\u00e2")
        buf.write("\n\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00ea\n\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00f8\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\5\25\u0104\n\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u010d\n\27\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u0119\n\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u0122\n\34\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\7\36\u012c\n\36\f\36\16\36")
        buf.write("\u012f\13\36\3\37\3\37\3 \3 \3 \3 \3 \3 \7 \u0139\n \f")
        buf.write(" \16 \u013c\13 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0146")
        buf.write("\n\"\f\"\16\"\u0149\13\"\3#\3#\3$\3$\3$\5$\u0150\n$\3")
        buf.write("%\3%\3&\3&\3&\5&\u0157\n&\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\7(\u0163\n(\f(\16(\u0166\13(\3)\3)\3*\3*\3*\3*\5")
        buf.write("*\u016e\n*\3*\3*\3*\3*\3*\5*\u0175\n*\3*\5*\u0178\n*\7")
        buf.write("*\u017a\n*\f*\16*\u017d\13*\3+\3+\5+\u0181\n+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\5,\u018a\n,\3-\3-\3-\3-\3-\3-\5-\u0192\n")
        buf.write("-\3.\3.\3.\3.\3/\3/\3/\3/\3/\5/\u019d\n/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01a5\n\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01ac\n\60\3\60\5\60\u01af\n\60\7\60\u01b1\n\60")
        buf.write("\f\60\16\60\u01b4\13\60\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\5\62\u01bf\n\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u01c7\n\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01d3\n\64\3\65\3\65\3\65\5")
        buf.write("\65\u01d8\n\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01e8\n\66\3\67\3")
        buf.write("\67\3\67\7\67\u01ed\n\67\f\67\16\67\u01f0\13\67\3\67\3")
        buf.write("\67\3\67\38\38\38\38\38\39\39\39\39\39\39\59\u0200\n9")
        buf.write("\3:\3:\3:\5:\u0205\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\7;\u0212\n;\f;\16;\u0215\13;\3;\3;\5;\u0219\n;\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\5<\u0224\n<\3<\3<\3<\3=\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\5?\u0231\n?\3?\3?\3@\3@\5@\u0237\n@\3@\3")
        buf.write("@\3A\3A\7A\u023d\nA\fA\16A\u0240\13A\3A\3A\3B\3B\5B\u0246")
        buf.write("\nB\3C\3C\3C\5C\u024b\nC\3C\3C\3D\3D\3D\3D\3D\3E\3E\3")
        buf.write("E\3E\5E\u0258\nE\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\3H\3H\3")
        buf.write("H\2\b:>BNR^I\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\2\n")
        buf.write("\3\2\22\23\3\2:;\3\2()\4\2!!#\'\3\2\37 \3\2\31\32\3\2")
        buf.write("\33\35\3\2\66\67\2\u0265\2\u0091\3\2\2\2\4\u0097\3\2\2")
        buf.write("\2\6\u00a4\3\2\2\2\b\u00a9\3\2\2\2\n\u00ab\3\2\2\2\f\u00be")
        buf.write("\3\2\2\2\16\u00c0\3\2\2\2\20\u00c4\3\2\2\2\22\u00ca\3")
        buf.write("\2\2\2\24\u00cc\3\2\2\2\26\u00cf\3\2\2\2\30\u00d7\3\2")
        buf.write("\2\2\32\u00dc\3\2\2\2\34\u00de\3\2\2\2\36\u00e6\3\2\2")
        buf.write("\2 \u00ee\3\2\2\2\"\u00f7\3\2\2\2$\u00f9\3\2\2\2&\u00fc")
        buf.write("\3\2\2\2(\u0103\3\2\2\2*\u0105\3\2\2\2,\u010c\3\2\2\2")
        buf.write(".\u010e\3\2\2\2\60\u0111\3\2\2\2\62\u0118\3\2\2\2\64\u011a")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0123\3\2\2\2:\u0125\3\2\2")
        buf.write("\2<\u0130\3\2\2\2>\u0132\3\2\2\2@\u013d\3\2\2\2B\u013f")
        buf.write("\3\2\2\2D\u014a\3\2\2\2F\u014f\3\2\2\2H\u0151\3\2\2\2")
        buf.write("J\u0156\3\2\2\2L\u0158\3\2\2\2N\u015a\3\2\2\2P\u0167\3")
        buf.write("\2\2\2R\u016d\3\2\2\2T\u0180\3\2\2\2V\u0189\3\2\2\2X\u0191")
        buf.write("\3\2\2\2Z\u0193\3\2\2\2\\\u0197\3\2\2\2^\u01a4\3\2\2\2")
        buf.write("`\u01b5\3\2\2\2b\u01b9\3\2\2\2d\u01c2\3\2\2\2f\u01d2\3")
        buf.write("\2\2\2h\u01d4\3\2\2\2j\u01e7\3\2\2\2l\u01e9\3\2\2\2n\u01f4")
        buf.write("\3\2\2\2p\u01ff\3\2\2\2r\u0204\3\2\2\2t\u0206\3\2\2\2")
        buf.write("v\u021a\3\2\2\2x\u0228\3\2\2\2z\u022b\3\2\2\2|\u022e\3")
        buf.write("\2\2\2~\u0236\3\2\2\2\u0080\u023a\3\2\2\2\u0082\u0245")
        buf.write("\3\2\2\2\u0084\u0247\3\2\2\2\u0086\u024e\3\2\2\2\u0088")
        buf.write("\u0257\3\2\2\2\u008a\u0259\3\2\2\2\u008c\u025c\3\2\2\2")
        buf.write("\u008e\u0263\3\2\2\2\u0090\u0092\5\4\3\2\u0091\u0090\3")
        buf.write("\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\7\2\2\3\u0096")
        buf.write("\3\3\2\2\2\u0097\u0098\7\21\2\2\u0098\u009b\7;\2\2\u0099")
        buf.write("\u009a\7,\2\2\u009a\u009c\7;\2\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7\64\2")
        buf.write("\2\u009e\u009f\5\6\4\2\u009f\u00a0\7\65\2\2\u00a0\5\3")
        buf.write("\2\2\2\u00a1\u00a3\5\b\5\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\5\n\6\2\u00a8")
        buf.write("\u00aa\5\32\16\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2")
        buf.write("\2\u00aa\t\3\2\2\2\u00ab\u00ae\t\2\2\2\u00ac\u00af\5\f")
        buf.write("\7\2\u00ad\u00af\5\16\b\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7\63\2\2\u00b1")
        buf.write("\13\3\2\2\2\u00b2\u00b3\5\20\t\2\u00b3\u00b4\7,\2\2\u00b4")
        buf.write("\u00b5\5\30\r\2\u00b5\u00b6\7\"\2\2\u00b6\u00b7\5\60\31")
        buf.write("\2\u00b7\u00bf\3\2\2\2\u00b8\u00b9\5\20\t\2\u00b9\u00ba")
        buf.write("\7\62\2\2\u00ba\u00bb\5\f\7\2\u00bb\u00bc\7\62\2\2\u00bc")
        buf.write("\u00bd\5\60\31\2\u00bd\u00bf\3\2\2\2\u00be\u00b2\3\2\2")
        buf.write("\2\u00be\u00b8\3\2\2\2\u00bf\r\3\2\2\2\u00c0\u00c1\5\22")
        buf.write("\n\2\u00c1\u00c2\7,\2\2\u00c2\u00c3\5\30\r\2\u00c3\17")
        buf.write("\3\2\2\2\u00c4\u00c5\t\3\2\2\u00c5\21\3\2\2\2\u00c6\u00c7")
        buf.write("\5\20\t\2\u00c7\u00c8\5\24\13\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00cb\5\20\t\2\u00ca\u00c6\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\23\3\2\2\2\u00cc\u00cd\7\62\2\2\u00cd\u00ce\5")
        buf.write("\22\n\2\u00ce\25\3\2\2\2\u00cf\u00d0\5,\27\2\u00d0\27")
        buf.write("\3\2\2\2\u00d1\u00d8\5\u008cG\2\u00d2\u00d8\7\13\2\2\u00d3")
        buf.write("\u00d8\7\f\2\2\u00d4\u00d8\7\r\2\2\u00d5\u00d8\7\16\2")
        buf.write("\2\u00d6\u00d8\7;\2\2\u00d7\u00d1\3\2\2\2\u00d7\u00d2")
        buf.write("\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\31\3\2\2\2\u00d9")
        buf.write("\u00dd\5\34\17\2\u00da\u00dd\5\36\20\2\u00db\u00dd\5 ")
        buf.write("\21\2\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00df\5\20\t\2\u00df\u00e1")
        buf.write("\7.\2\2\u00e0\u00e2\5\"\22\2\u00e1\u00e0\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7/\2\2")
        buf.write("\u00e4\u00e5\5\u0080A\2\u00e5\35\3\2\2\2\u00e6\u00e7\7")
        buf.write("\24\2\2\u00e7\u00e9\7.\2\2\u00e8\u00ea\5\"\22\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ec\7/\2\2\u00ec\u00ed\5\u0080A\2\u00ed\37\3")
        buf.write("\2\2\2\u00ee\u00ef\7\25\2\2\u00ef\u00f0\7.\2\2\u00f0\u00f1")
        buf.write("\7/\2\2\u00f1\u00f2\5\u0080A\2\u00f2!\3\2\2\2\u00f3\u00f4")
        buf.write("\5&\24\2\u00f4\u00f5\5$\23\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f8\5&\24\2\u00f7\u00f3\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8#\3\2\2\2\u00f9\u00fa\7\63\2\2\u00fa\u00fb\5\"\22")
        buf.write("\2\u00fb%\3\2\2\2\u00fc\u00fd\5(\25\2\u00fd\u00fe\7,\2")
        buf.write("\2\u00fe\u00ff\5\30\r\2\u00ff\'\3\2\2\2\u0100\u0101\7")
        buf.write(";\2\2\u0101\u0104\5*\26\2\u0102\u0104\7;\2\2\u0103\u0100")
        buf.write("\3\2\2\2\u0103\u0102\3\2\2\2\u0104)\3\2\2\2\u0105\u0106")
        buf.write("\7\62\2\2\u0106\u0107\5(\25\2\u0107+\3\2\2\2\u0108\u0109")
        buf.write("\5\60\31\2\u0109\u010a\5.\30\2\u010a\u010d\3\2\2\2\u010b")
        buf.write("\u010d\5\60\31\2\u010c\u0108\3\2\2\2\u010c\u010b\3\2\2")
        buf.write("\2\u010d-\3\2\2\2\u010e\u010f\7\62\2\2\u010f\u0110\5,")
        buf.write("\27\2\u0110/\3\2\2\2\u0111\u0112\5\62\32\2\u0112\61\3")
        buf.write("\2\2\2\u0113\u0114\5\64\33\2\u0114\u0115\t\4\2\2\u0115")
        buf.write("\u0116\5\64\33\2\u0116\u0119\3\2\2\2\u0117\u0119\5\64")
        buf.write("\33\2\u0118\u0113\3\2\2\2\u0118\u0117\3\2\2\2\u0119\63")
        buf.write("\3\2\2\2\u011a\u011b\5\66\34\2\u011b\65\3\2\2\2\u011c")
        buf.write("\u011d\58\35\2\u011d\u011e\t\5\2\2\u011e\u011f\58\35\2")
        buf.write("\u011f\u0122\3\2\2\2\u0120\u0122\58\35\2\u0121\u011c\3")
        buf.write("\2\2\2\u0121\u0120\3\2\2\2\u0122\67\3\2\2\2\u0123\u0124")
        buf.write("\5:\36\2\u01249\3\2\2\2\u0125\u0126\b\36\1\2\u0126\u0127")
        buf.write("\5<\37\2\u0127\u012d\3\2\2\2\u0128\u0129\f\4\2\2\u0129")
        buf.write("\u012a\t\6\2\2\u012a\u012c\5<\37\2\u012b\u0128\3\2\2\2")
        buf.write("\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3")
        buf.write("\2\2\2\u012e;\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131")
        buf.write("\5> \2\u0131=\3\2\2\2\u0132\u0133\b \1\2\u0133\u0134\5")
        buf.write("@!\2\u0134\u013a\3\2\2\2\u0135\u0136\f\4\2\2\u0136\u0137")
        buf.write("\t\7\2\2\u0137\u0139\5@!\2\u0138\u0135\3\2\2\2\u0139\u013c")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("?\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\5B\"\2\u013e")
        buf.write("A\3\2\2\2\u013f\u0140\b\"\1\2\u0140\u0141\5D#\2\u0141")
        buf.write("\u0147\3\2\2\2\u0142\u0143\f\4\2\2\u0143\u0144\t\b\2\2")
        buf.write("\u0144\u0146\5D#\2\u0145\u0142\3\2\2\2\u0146\u0149\3\2")
        buf.write("\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148C\3")
        buf.write("\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\5F$\2\u014bE\3")
        buf.write("\2\2\2\u014c\u014d\7\36\2\2\u014d\u0150\5D#\2\u014e\u0150")
        buf.write("\5H%\2\u014f\u014c\3\2\2\2\u014f\u014e\3\2\2\2\u0150G")
        buf.write("\3\2\2\2\u0151\u0152\5J&\2\u0152I\3\2\2\2\u0153\u0154")
        buf.write("\7\32\2\2\u0154\u0157\5H%\2\u0155\u0157\5L\'\2\u0156\u0153")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157K\3\2\2\2\u0158\u0159")
        buf.write("\5N(\2\u0159M\3\2\2\2\u015a\u015b\b(\1\2\u015b\u015c\5")
        buf.write("P)\2\u015c\u0164\3\2\2\2\u015d\u015e\f\4\2\2\u015e\u015f")
        buf.write("\7\60\2\2\u015f\u0160\5\60\31\2\u0160\u0161\7\61\2\2\u0161")
        buf.write("\u0163\3\2\2\2\u0162\u015d\3\2\2\2\u0163\u0166\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165O\3\2\2")
        buf.write("\2\u0166\u0164\3\2\2\2\u0167\u0168\5R*\2\u0168Q\3\2\2")
        buf.write("\2\u0169\u016a\b*\1\2\u016a\u016e\5`\61\2\u016b\u016e")
        buf.write("\5b\62\2\u016c\u016e\5T+\2\u016d\u0169\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u017b\3\2\2\2\u016f")
        buf.write("\u0170\f\6\2\2\u0170\u0171\7*\2\2\u0171\u0177\7;\2\2\u0172")
        buf.write("\u0174\7.\2\2\u0173\u0175\5,\27\2\u0174\u0173\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\7")
        buf.write("/\2\2\u0177\u0172\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a")
        buf.write("\3\2\2\2\u0179\u016f\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017cS\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u0181\5d\63\2\u017f\u0181\5V,\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181U\3\2\2\2\u0182")
        buf.write("\u018a\5X-\2\u0183\u018a\7;\2\2\u0184\u018a\7\30\2\2\u0185")
        buf.write("\u0186\7.\2\2\u0186\u0187\5\60\31\2\u0187\u0188\7/\2\2")
        buf.write("\u0188\u018a\3\2\2\2\u0189\u0182\3\2\2\2\u0189\u0183\3")
        buf.write("\2\2\2\u0189\u0184\3\2\2\2\u0189\u0185\3\2\2\2\u018aW")
        buf.write("\3\2\2\2\u018b\u0192\5\u008eH\2\u018c\u0192\78\2\2\u018d")
        buf.write("\u0192\7=\2\2\u018e\u0192\79\2\2\u018f\u0192\5\u0082B")
        buf.write("\2\u0190\u0192\7\20\2\2\u0191\u018b\3\2\2\2\u0191\u018c")
        buf.write("\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u018e\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192Y\3\2\2\2\u0193")
        buf.write("\u0194\5R*\2\u0194\u0195\7*\2\2\u0195\u0196\7;\2\2\u0196")
        buf.write("[\3\2\2\2\u0197\u0198\5^\60\2\u0198\u0199\7*\2\2\u0199")
        buf.write("\u019a\7;\2\2\u019a\u019c\7.\2\2\u019b\u019d\5,\27\2\u019c")
        buf.write("\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\7/\2\2\u019f]\3\2\2\2\u01a0\u01a1\b\60\1")
        buf.write("\2\u01a1\u01a5\5`\61\2\u01a2\u01a5\5b\62\2\u01a3\u01a5")
        buf.write("\5T+\2\u01a4\u01a0\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01b2\3\2\2\2\u01a6\u01a7\f\6\2\2\u01a7")
        buf.write("\u01a8\7*\2\2\u01a8\u01ae\7;\2\2\u01a9\u01ab\7.\2\2\u01aa")
        buf.write("\u01ac\5,\27\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01af\7/\2\2\u01ae\u01a9\3")
        buf.write("\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01a6")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3_\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b6\7;\2\2\u01b6\u01b7\7-\2\2\u01b7\u01b8\7:\2\2\u01b8")
        buf.write("a\3\2\2\2\u01b9\u01ba\7;\2\2\u01ba\u01bb\7-\2\2\u01bb")
        buf.write("\u01bc\7:\2\2\u01bc\u01be\7.\2\2\u01bd\u01bf\5,\27\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01c1\7/\2\2\u01c1c\3\2\2\2\u01c2\u01c3\7\26\2")
        buf.write("\2\u01c3\u01c4\7;\2\2\u01c4\u01c6\7.\2\2\u01c5\u01c7\5")
        buf.write(",\27\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\7/\2\2\u01c9e\3\2\2\2\u01ca\u01d3")
        buf.write("\5h\65\2\u01cb\u01d3\5n8\2\u01cc\u01d3\5t;\2\u01cd\u01d3")
        buf.write("\5v<\2\u01ce\u01d3\5x=\2\u01cf\u01d3\5z>\2\u01d0\u01d3")
        buf.write("\5|?\2\u01d1\u01d3\5~@\2\u01d2\u01ca\3\2\2\2\u01d2\u01cb")
        buf.write("\3\2\2\2\u01d2\u01cc\3\2\2\2\u01d2\u01cd\3\2\2\2\u01d2")
        buf.write("\u01ce\3\2\2\2\u01d2\u01cf\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d3g\3\2\2\2\u01d4\u01d7\t\2\2")
        buf.write("\2\u01d5\u01d8\5j\66\2\u01d6\u01d8\5l\67\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01da\7\63\2\2\u01dai\3\2\2\2\u01db\u01dc\7;\2\2\u01dc")
        buf.write("\u01dd\7,\2\2\u01dd\u01de\5\30\r\2\u01de\u01df\7\"\2\2")
        buf.write("\u01df\u01e0\5\60\31\2\u01e0\u01e8\3\2\2\2\u01e1\u01e2")
        buf.write("\7;\2\2\u01e2\u01e3\7\62\2\2\u01e3\u01e4\5j\66\2\u01e4")
        buf.write("\u01e5\7\62\2\2\u01e5\u01e6\5\60\31\2\u01e6\u01e8\3\2")
        buf.write("\2\2\u01e7\u01db\3\2\2\2\u01e7\u01e1\3\2\2\2\u01e8k\3")
        buf.write("\2\2\2\u01e9\u01ee\7;\2\2\u01ea\u01eb\7\62\2\2\u01eb\u01ed")
        buf.write("\7;\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f1\u01f2\7,\2\2\u01f2\u01f3\5")
        buf.write("\30\r\2\u01f3m\3\2\2\2\u01f4\u01f5\5p9\2\u01f5\u01f6\7")
        buf.write("\"\2\2\u01f6\u01f7\5\60\31\2\u01f7\u01f8\7\63\2\2\u01f8")
        buf.write("o\3\2\2\2\u01f9\u01fa\5N(\2\u01fa\u01fb\7\60\2\2\u01fb")
        buf.write("\u01fc\5\60\31\2\u01fc\u01fd\7\61\2\2\u01fd\u0200\3\2")
        buf.write("\2\2\u01fe\u0200\5r:\2\u01ff\u01f9\3\2\2\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200q\3\2\2\2\u0201\u0205\7;\2\2\u0202\u0205")
        buf.write("\5Z.\2\u0203\u0205\5`\61\2\u0204\u0201\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0204\u0203\3\2\2\2\u0205s\3\2\2\2\u0206\u0207")
        buf.write("\7\5\2\2\u0207\u0208\7.\2\2\u0208\u0209\5\60\31\2\u0209")
        buf.write("\u020a\7/\2\2\u020a\u0213\5\u0080A\2\u020b\u020c\7\6\2")
        buf.write("\2\u020c\u020d\7.\2\2\u020d\u020e\5\60\31\2\u020e\u020f")
        buf.write("\7/\2\2\u020f\u0210\5\u0080A\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u020b\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0218\3\2\2\2\u0215\u0213\3")
        buf.write("\2\2\2\u0216\u0217\7\7\2\2\u0217\u0219\5\u0080A\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219u\3\2\2\2\u021a")
        buf.write("\u021b\7\b\2\2\u021b\u021c\7.\2\2\u021c\u021d\5\60\31")
        buf.write("\2\u021d\u021e\7\n\2\2\u021e\u021f\5\60\31\2\u021f\u0220")
        buf.write("\7+\2\2\u0220\u0223\5\60\31\2\u0221\u0222\7\27\2\2\u0222")
        buf.write("\u0224\5\60\31\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2")
        buf.write("\2\u0224\u0225\3\2\2\2\u0225\u0226\7/\2\2\u0226\u0227")
        buf.write("\5\u0080A\2\u0227w\3\2\2\2\u0228\u0229\7\3\2\2\u0229\u022a")
        buf.write("\7\63\2\2\u022ay\3\2\2\2\u022b\u022c\7\4\2\2\u022c\u022d")
        buf.write("\7\63\2\2\u022d{\3\2\2\2\u022e\u0230\7\17\2\2\u022f\u0231")
        buf.write("\5\60\31\2\u0230\u022f\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0232\3\2\2\2\u0232\u0233\7\63\2\2\u0233}\3\2\2\2\u0234")
        buf.write("\u0237\5\\/\2\u0235\u0237\5b\62\2\u0236\u0234\3\2\2\2")
        buf.write("\u0236\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\7")
        buf.write("\63\2\2\u0239\177\3\2\2\2\u023a\u023e\7\64\2\2\u023b\u023d")
        buf.write("\5f\64\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0241\3\2\2\2")
        buf.write("\u0240\u023e\3\2\2\2\u0241\u0242\7\65\2\2\u0242\u0081")
        buf.write("\3\2\2\2\u0243\u0246\5\u0084C\2\u0244\u0246\5\u0086D\2")
        buf.write("\u0245\u0243\3\2\2\2\u0245\u0244\3\2\2\2\u0246\u0083\3")
        buf.write("\2\2\2\u0247\u0248\7\t\2\2\u0248\u024a\7.\2\2\u0249\u024b")
        buf.write("\5,\27\2\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c\u024d\7/\2\2\u024d\u0085\3\2\2\2")
        buf.write("\u024e\u024f\7\t\2\2\u024f\u0250\7.\2\2\u0250\u0251\5")
        buf.write("\u0088E\2\u0251\u0252\7/\2\2\u0252\u0087\3\2\2\2\u0253")
        buf.write("\u0254\5\u0084C\2\u0254\u0255\5\u008aF\2\u0255\u0258\3")
        buf.write("\2\2\2\u0256\u0258\5\u0084C\2\u0257\u0253\3\2\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258\u0089\3\2\2\2\u0259\u025a\7\62\2")
        buf.write("\2\u025a\u025b\5\u0088E\2\u025b\u008b\3\2\2\2\u025c\u025d")
        buf.write("\7\t\2\2\u025d\u025e\7\60\2\2\u025e\u025f\5\30\r\2\u025f")
        buf.write("\u0260\7\62\2\2\u0260\u0261\7\67\2\2\u0261\u0262\7\61")
        buf.write("\2\2\u0262\u008d\3\2\2\2\u0263\u0264\t\t\2\2\u0264\u008f")
        buf.write("\3\2\2\2\65\u0093\u009b\u00a4\u00a9\u00ae\u00be\u00ca")
        buf.write("\u00d7\u00dc\u00e1\u00e9\u00f7\u0103\u010c\u0118\u0121")
        buf.write("\u012d\u013a\u0147\u014f\u0156\u0164\u016d\u0174\u0177")
        buf.write("\u017b\u0180\u0189\u0191\u019c\u01a4\u01ab\u01ae\u01b2")
        buf.write("\u01be\u01c6\u01d2\u01d7\u01e7\u01ee\u01ff\u0204\u0213")
        buf.write("\u0218\u0223\u0230\u0236\u023e\u0245\u024a\u0257")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'Array'", "'In'", "'Int'", 
                     "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
                     "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", "'.'", 
                     "'..'", "':'", "'::'", "'('", "')'", "'['", "']'", 
                     "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "ARRAY", "IN", "INT", "FLOAT", 
                      "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                      "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "DOUBLE_EQU", "EQU", "DIF", "SMALLER", "SMA_EQ", "BIGGER", 
                      "BIG_EQ", "STR_EQ", "STR_ADD", "DOT", "DOUBLE_DOT", 
                      "COLLON", "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", 
                      "COMMA", "SEMI", "LP", "RP", "ZERO", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "DOLLAR_ID", "NORMAL_ID", "COMMENT", "STR_LIT", 
                      "WS", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_list_of_members = 2
    RULE_member = 3
    RULE_attribute_declaration = 4
    RULE_attr_decl_bis = 5
    RULE_attr_decl_bis1 = 6
    RULE_possible_id = 7
    RULE_id_list_attribute = 8
    RULE_more_id_attribute = 9
    RULE_value_list = 10
    RULE_type_name = 11
    RULE_method_declaration = 12
    RULE_normal_method = 13
    RULE_constructor = 14
    RULE_destructor = 15
    RULE_list_of_parameters = 16
    RULE_more_parameters = 17
    RULE_parameters = 18
    RULE_id_list = 19
    RULE_more_id = 20
    RULE_list_of_expressions = 21
    RULE_more_expression = 22
    RULE_expression = 23
    RULE_string_expression = 24
    RULE_expr1 = 25
    RULE_relation_expression = 26
    RULE_expr2 = 27
    RULE_logical_expression = 28
    RULE_expr3 = 29
    RULE_adding_expression = 30
    RULE_expr4 = 31
    RULE_multiplying_expression = 32
    RULE_expr5 = 33
    RULE_not_expression = 34
    RULE_expr6 = 35
    RULE_negative_expression = 36
    RULE_expr7 = 37
    RULE_index_expression = 38
    RULE_expr8 = 39
    RULE_object_access_expression = 40
    RULE_expr9 = 41
    RULE_operand = 42
    RULE_all_literals = 43
    RULE_inst_ob_access = 44
    RULE_inst_mth_access = 45
    RULE_super_inst_mth_acess = 46
    RULE_static_ob_access = 47
    RULE_static_mth_access = 48
    RULE_object_creation_expression = 49
    RULE_statements = 50
    RULE_var_and_const_stmt = 51
    RULE_var_and_const_bis = 52
    RULE_var_and_const_bis1 = 53
    RULE_assign_stmt = 54
    RULE_left_hand_side = 55
    RULE_scalar_var = 56
    RULE_if_stmt = 57
    RULE_for_in_stmt = 58
    RULE_break_stmt = 59
    RULE_cont_stmt = 60
    RULE_return_stmt = 61
    RULE_method_invocation_stmt = 62
    RULE_block_stmt = 63
    RULE_array_lit = 64
    RULE_indexed_array = 65
    RULE_multi_demensional_array = 66
    RULE_list_of_arrays = 67
    RULE_more_array = 68
    RULE_array_type = 69
    RULE_all_int_lit = 70

    ruleNames =  [ "program", "class_declaration", "list_of_members", "member", 
                   "attribute_declaration", "attr_decl_bis", "attr_decl_bis1", 
                   "possible_id", "id_list_attribute", "more_id_attribute", 
                   "value_list", "type_name", "method_declaration", "normal_method", 
                   "constructor", "destructor", "list_of_parameters", "more_parameters", 
                   "parameters", "id_list", "more_id", "list_of_expressions", 
                   "more_expression", "expression", "string_expression", 
                   "expr1", "relation_expression", "expr2", "logical_expression", 
                   "expr3", "adding_expression", "expr4", "multiplying_expression", 
                   "expr5", "not_expression", "expr6", "negative_expression", 
                   "expr7", "index_expression", "expr8", "object_access_expression", 
                   "expr9", "operand", "all_literals", "inst_ob_access", 
                   "inst_mth_access", "super_inst_mth_acess", "static_ob_access", 
                   "static_mth_access", "object_creation_expression", "statements", 
                   "var_and_const_stmt", "var_and_const_bis", "var_and_const_bis1", 
                   "assign_stmt", "left_hand_side", "scalar_var", "if_stmt", 
                   "for_in_stmt", "break_stmt", "cont_stmt", "return_stmt", 
                   "method_invocation_stmt", "block_stmt", "array_lit", 
                   "indexed_array", "multi_demensional_array", "list_of_arrays", 
                   "more_array", "array_type", "all_int_lit" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    ARRAY=7
    IN=8
    INT=9
    FLOAT=10
    BOOLEAN=11
    STRING=12
    RETURN=13
    NULL=14
    CLASS=15
    VAL=16
    VAR=17
    CONSTRUCTOR=18
    DESTRUCTOR=19
    NEW=20
    BY=21
    SELF=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    NOT=28
    AND=29
    OR=30
    DOUBLE_EQU=31
    EQU=32
    DIF=33
    SMALLER=34
    SMA_EQ=35
    BIGGER=36
    BIG_EQ=37
    STR_EQ=38
    STR_ADD=39
    DOT=40
    DOUBLE_DOT=41
    COLLON=42
    DOUBLE_COLON=43
    LB=44
    RB=45
    LSB=46
    RSB=47
    COMMA=48
    SEMI=49
    LP=50
    RP=51
    ZERO=52
    INT_LIT=53
    FLOAT_LIT=54
    BOOL_LIT=55
    DOLLAR_ID=56
    NORMAL_ID=57
    COMMENT=58
    STR_LIT=59
    WS=60
    ERROR_TOKEN=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.class_declaration()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 147
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def NORMAL_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.NORMAL_ID)
            else:
                return self.getToken(D96Parser.NORMAL_ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_members(self):
            return self.getTypedRuleContext(D96Parser.List_of_membersContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.CLASS)
            self.state = 150
            self.match(D96Parser.NORMAL_ID)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLLON:
                self.state = 151
                self.match(D96Parser.COLLON)
                self.state = 152
                self.match(D96Parser.NORMAL_ID)


            self.state = 155
            self.match(D96Parser.LP)
            self.state = 156
            self.list_of_members()
            self.state = 157
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MemberContext)
            else:
                return self.getTypedRuleContext(D96Parser.MemberContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_members" ):
                return visitor.visitList_of_members(self)
            else:
                return visitor.visitChildren(self)




    def list_of_members(self):

        localctx = D96Parser.List_of_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_of_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.NORMAL_ID))) != 0):
                self.state = 159
                self.member()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.attribute_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLAR_ID, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.method_declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def attr_decl_bis(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_bisContext,0)


        def attr_decl_bis1(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_bis1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 170
                self.attr_decl_bis()
                pass

            elif la_ == 2:
                self.state = 171
                self.attr_decl_bis1()
                pass


            self.state = 174
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_bisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possible_id(self):
            return self.getTypedRuleContext(D96Parser.Possible_idContext,0)


        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def EQU(self):
            return self.getToken(D96Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attr_decl_bis(self):
            return self.getTypedRuleContext(D96Parser.Attr_decl_bisContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_bis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_bis" ):
                return visitor.visitAttr_decl_bis(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_bis(self):

        localctx = D96Parser.Attr_decl_bisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl_bis)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.possible_id()
                self.state = 177
                self.match(D96Parser.COLLON)
                self.state = 178
                self.type_name()
                self.state = 179
                self.match(D96Parser.EQU)
                self.state = 180
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.possible_id()
                self.state = 183
                self.match(D96Parser.COMMA)
                self.state = 184
                self.attr_decl_bis()
                self.state = 185
                self.match(D96Parser.COMMA)
                self.state = 186
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_bis1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_attribute(self):
            return self.getTypedRuleContext(D96Parser.Id_list_attributeContext,0)


        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl_bis1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_bis1" ):
                return visitor.visitAttr_decl_bis1(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_bis1(self):

        localctx = D96Parser.Attr_decl_bis1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_decl_bis1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.id_list_attribute()
            self.state = 191
            self.match(D96Parser.COLLON)
            self.state = 192
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Possible_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_possible_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPossible_id" ):
                return visitor.visitPossible_id(self)
            else:
                return visitor.visitChildren(self)




    def possible_id(self):

        localctx = D96Parser.Possible_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_possible_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.NORMAL_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_list_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possible_id(self):
            return self.getTypedRuleContext(D96Parser.Possible_idContext,0)


        def more_id_attribute(self):
            return self.getTypedRuleContext(D96Parser.More_id_attributeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list_attribute" ):
                return visitor.visitId_list_attribute(self)
            else:
                return visitor.visitChildren(self)




    def id_list_attribute(self):

        localctx = D96Parser.Id_list_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id_list_attribute)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.possible_id()
                self.state = 197
                self.more_id_attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.possible_id()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_id_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def id_list_attribute(self):
            return self.getTypedRuleContext(D96Parser.Id_list_attributeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_more_id_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_id_attribute" ):
                return visitor.visitMore_id_attribute(self)
            else:
                return visitor.visitChildren(self)




    def more_id_attribute(self):

        localctx = D96Parser.More_id_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_more_id_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(D96Parser.COMMA)
            self.state = 203
            self.id_list_attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_value_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list" ):
                return visitor.visitValue_list(self)
            else:
                return visitor.visitChildren(self)




    def value_list(self):

        localctx = D96Parser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.list_of_expressions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_name)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.match(D96Parser.NORMAL_ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_method(self):
            return self.getTypedRuleContext(D96Parser.Normal_methodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_declaration)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOLLAR_ID, D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possible_id(self):
            return self.getTypedRuleContext(D96Parser.Possible_idContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.possible_id()
            self.state = 221
            self.match(D96Parser.LB)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.NORMAL_ID:
                self.state = 222
                self.list_of_parameters()


            self.state = 225
            self.match(D96Parser.RB)
            self.state = 226
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 229
            self.match(D96Parser.LB)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.NORMAL_ID:
                self.state = 230
                self.list_of_parameters()


            self.state = 233
            self.match(D96Parser.RB)
            self.state = 234
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(D96Parser.DESTRUCTOR)
            self.state = 237
            self.match(D96Parser.LB)
            self.state = 238
            self.match(D96Parser.RB)
            self.state = 239
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def more_parameters(self):
            return self.getTypedRuleContext(D96Parser.More_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_parameters" ):
                return visitor.visitList_of_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_of_parameters(self):

        localctx = D96Parser.List_of_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_of_parameters)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.parameters()
                self.state = 242
                self.more_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_more_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_parameters" ):
                return visitor.visitMore_parameters(self)
            else:
                return visitor.visitChildren(self)




    def more_parameters(self):

        localctx = D96Parser.More_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_more_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.SEMI)
            self.state = 248
            self.list_of_parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = D96Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.id_list()
            self.state = 251
            self.match(D96Parser.COLLON)
            self.state = 252
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def more_id(self):
            return self.getTypedRuleContext(D96Parser.More_idContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_id_list)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(D96Parser.NORMAL_ID)
                self.state = 255
                self.more_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(D96Parser.NORMAL_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_more_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_id" ):
                return visitor.visitMore_id(self)
            else:
                return visitor.visitChildren(self)




    def more_id(self):

        localctx = D96Parser.More_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_more_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(D96Parser.COMMA)
            self.state = 260
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def more_expression(self):
            return self.getTypedRuleContext(D96Parser.More_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expressions" ):
                return visitor.visitList_of_expressions(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expressions(self):

        localctx = D96Parser.List_of_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_of_expressions)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.expression()
                self.state = 263
                self.more_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_more_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_expression" ):
                return visitor.visitMore_expression(self)
            else:
                return visitor.visitChildren(self)




    def more_expression(self):

        localctx = D96Parser.More_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_more_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(D96Parser.COMMA)
            self.state = 269
            self.list_of_expressions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression(self):
            return self.getTypedRuleContext(D96Parser.String_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STR_ADD(self):
            return self.getToken(D96Parser.STR_ADD, 0)

        def STR_EQ(self):
            return self.getToken(D96Parser.STR_EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = D96Parser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expr1()
                self.state = 274
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_EQ or _la==D96Parser.STR_ADD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_expression(self):
            return self.getTypedRuleContext(D96Parser.Relation_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.relation_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def DOUBLE_EQU(self):
            return self.getToken(D96Parser.DOUBLE_EQU, 0)

        def DIF(self):
            return self.getToken(D96Parser.DIF, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def BIGGER(self):
            return self.getToken(D96Parser.BIGGER, 0)

        def SMA_EQ(self):
            return self.getToken(D96Parser.SMA_EQ, 0)

        def BIG_EQ(self):
            return self.getToken(D96Parser.BIG_EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_expression" ):
                return visitor.visitRelation_expression(self)
            else:
                return visitor.visitChildren(self)




    def relation_expression(self):

        localctx = D96Parser.Relation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relation_expression)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.expr2()
                self.state = 283
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.DOUBLE_EQU) | (1 << D96Parser.DIF) | (1 << D96Parser.SMALLER) | (1 << D96Parser.SMA_EQ) | (1 << D96Parser.BIGGER) | (1 << D96Parser.BIG_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self):
            return self.getTypedRuleContext(D96Parser.Logical_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = D96Parser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.logical_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def logical_expression(self):
            return self.getTypedRuleContext(D96Parser.Logical_expressionContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 295
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 296
                    self.expr3() 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = D96Parser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.adding_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expression" ):
                return visitor.visitAdding_expression(self)
            else:
                return visitor.visitChildren(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.expr4() 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = D96Parser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.multiplying_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expression" ):
                return visitor.visitMultiplying_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.expr5() 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expression(self):
            return self.getTypedRuleContext(D96Parser.Not_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.not_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_not_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expression" ):
                return visitor.visitNot_expression(self)
            else:
                return visitor.visitChildren(self)




    def not_expression(self):

        localctx = D96Parser.Not_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_not_expression)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(D96Parser.NOT)
                self.state = 331
                self.expr5()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LB, D96Parser.ZERO, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.NORMAL_ID, D96Parser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negative_expression(self):
            return self.getTypedRuleContext(D96Parser.Negative_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.negative_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Negative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_negative_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative_expression" ):
                return visitor.visitNegative_expression(self)
            else:
                return visitor.visitChildren(self)




    def negative_expression(self):

        localctx = D96Parser.Negative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_negative_expression)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(D96Parser.SUB)
                self.state = 338
                self.expr6()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ZERO, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.NORMAL_ID, D96Parser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.index_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    self.match(D96Parser.LSB)
                    self.state = 349
                    self.expression()
                    self.state = 350
                    self.match(D96Parser.RSB) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = D96Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.object_access_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_ob_access(self):
            return self.getTypedRuleContext(D96Parser.Static_ob_accessContext,0)


        def static_mth_access(self):
            return self.getTypedRuleContext(D96Parser.Static_mth_accessContext,0)


        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def object_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_access_expressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_access_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_access_expression" ):
                return visitor.visitObject_access_expression(self)
            else:
                return visitor.visitChildren(self)



    def object_access_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Object_access_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_object_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 360
                self.static_ob_access()
                pass

            elif la_ == 2:
                self.state = 361
                self.static_mth_access()
                pass

            elif la_ == 3:
                self.state = 362
                self.expr9()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Object_access_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_object_access_expression)
                    self.state = 365
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 366
                    self.match(D96Parser.DOT)
                    self.state = 367
                    self.match(D96Parser.NORMAL_ID)
                    self.state = 373
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 368
                        self.match(D96Parser.LB)
                        self.state = 370
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                            self.state = 369
                            self.list_of_expressions()


                        self.state = 372
                        self.match(D96Parser.RB)

             
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_creation_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_creation_expressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr9)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.object_creation_expression()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ZERO, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.NORMAL_ID, D96Parser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_literals(self):
            return self.getTypedRuleContext(D96Parser.All_literalsContext,0)


        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.ZERO, D96Parser.INT_LIT, D96Parser.FLOAT_LIT, D96Parser.BOOL_LIT, D96Parser.STR_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.all_literals()
                pass
            elif token in [D96Parser.NORMAL_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(D96Parser.NORMAL_ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(D96Parser.LB)
                self.state = 388
                self.expression()
                self.state = 389
                self.match(D96Parser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_int_lit(self):
            return self.getTypedRuleContext(D96Parser.All_int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(D96Parser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(D96Parser.STR_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(D96Parser.BOOL_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_all_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_literals" ):
                return visitor.visitAll_literals(self)
            else:
                return visitor.visitChildren(self)




    def all_literals(self):

        localctx = D96Parser.All_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_all_literals)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZERO, D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.all_int_lit()
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.match(D96Parser.STR_LIT)
                pass
            elif token in [D96Parser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.match(D96Parser.BOOL_LIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.array_lit()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_ob_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_access_expressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_inst_ob_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_ob_access" ):
                return visitor.visitInst_ob_access(self)
            else:
                return visitor.visitChildren(self)




    def inst_ob_access(self):

        localctx = D96Parser.Inst_ob_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_inst_ob_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.object_access_expression(0)
            self.state = 402
            self.match(D96Parser.DOT)
            self.state = 403
            self.match(D96Parser.NORMAL_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_mth_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_inst_mth_acess(self):
            return self.getTypedRuleContext(D96Parser.Super_inst_mth_acessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_inst_mth_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_mth_access" ):
                return visitor.visitInst_mth_access(self)
            else:
                return visitor.visitChildren(self)




    def inst_mth_access(self):

        localctx = D96Parser.Inst_mth_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_inst_mth_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.super_inst_mth_acess(0)
            self.state = 406
            self.match(D96Parser.DOT)
            self.state = 407
            self.match(D96Parser.NORMAL_ID)
            self.state = 408
            self.match(D96Parser.LB)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 409
                self.list_of_expressions()


            self.state = 412
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_inst_mth_acessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_ob_access(self):
            return self.getTypedRuleContext(D96Parser.Static_ob_accessContext,0)


        def static_mth_access(self):
            return self.getTypedRuleContext(D96Parser.Static_mth_accessContext,0)


        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def super_inst_mth_acess(self):
            return self.getTypedRuleContext(D96Parser.Super_inst_mth_acessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_super_inst_mth_acess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuper_inst_mth_acess" ):
                return visitor.visitSuper_inst_mth_acess(self)
            else:
                return visitor.visitChildren(self)



    def super_inst_mth_acess(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Super_inst_mth_acessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_super_inst_mth_acess, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 415
                self.static_ob_access()
                pass

            elif la_ == 2:
                self.state = 416
                self.static_mth_access()
                pass

            elif la_ == 3:
                self.state = 417
                self.expr9()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Super_inst_mth_acessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_super_inst_mth_acess)
                    self.state = 420
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 421
                    self.match(D96Parser.DOT)
                    self.state = 422
                    self.match(D96Parser.NORMAL_ID)
                    self.state = 428
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 423
                        self.match(D96Parser.LB)
                        self.state = 425
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                            self.state = 424
                            self.list_of_expressions()


                        self.state = 427
                        self.match(D96Parser.RB)

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_ob_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_ob_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_ob_access" ):
                return visitor.visitStatic_ob_access(self)
            else:
                return visitor.visitChildren(self)




    def static_ob_access(self):

        localctx = D96Parser.Static_ob_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_ob_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.NORMAL_ID)
            self.state = 436
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 437
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_mth_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_mth_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_mth_access" ):
                return visitor.visitStatic_mth_access(self)
            else:
                return visitor.visitChildren(self)




    def static_mth_access(self):

        localctx = D96Parser.Static_mth_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_static_mth_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(D96Parser.NORMAL_ID)
            self.state = 440
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 441
            self.match(D96Parser.DOLLAR_ID)
            self.state = 442
            self.match(D96Parser.LB)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 443
                self.list_of_expressions()


            self.state = 446
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation_expression" ):
                return visitor.visitObject_creation_expression(self)
            else:
                return visitor.visitChildren(self)




    def object_creation_expression(self):

        localctx = D96Parser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.NEW)
            self.state = 449
            self.match(D96Parser.NORMAL_ID)
            self.state = 450
            self.match(D96Parser.LB)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 451
                self.list_of_expressions()


            self.state = 454
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_and_const_stmt(self):
            return self.getTypedRuleContext(D96Parser.Var_and_const_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_in_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_in_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(D96Parser.Cont_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statements)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.var_and_const_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 459
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 460
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 461
                self.cont_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 462
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 463
                self.method_invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_and_const_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def var_and_const_bis(self):
            return self.getTypedRuleContext(D96Parser.Var_and_const_bisContext,0)


        def var_and_const_bis1(self):
            return self.getTypedRuleContext(D96Parser.Var_and_const_bis1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_and_const_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_and_const_stmt" ):
                return visitor.visitVar_and_const_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_and_const_stmt(self):

        localctx = D96Parser.Var_and_const_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_var_and_const_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 467
                self.var_and_const_bis()
                pass

            elif la_ == 2:
                self.state = 468
                self.var_and_const_bis1()
                pass


            self.state = 471
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_and_const_bisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def EQU(self):
            return self.getToken(D96Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def var_and_const_bis(self):
            return self.getTypedRuleContext(D96Parser.Var_and_const_bisContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_and_const_bis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_and_const_bis" ):
                return visitor.visitVar_and_const_bis(self)
            else:
                return visitor.visitChildren(self)




    def var_and_const_bis(self):

        localctx = D96Parser.Var_and_const_bisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_var_and_const_bis)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(D96Parser.NORMAL_ID)
                self.state = 474
                self.match(D96Parser.COLLON)
                self.state = 475
                self.type_name()
                self.state = 476
                self.match(D96Parser.EQU)
                self.state = 477
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(D96Parser.NORMAL_ID)
                self.state = 480
                self.match(D96Parser.COMMA)
                self.state = 481
                self.var_and_const_bis()
                self.state = 482
                self.match(D96Parser.COMMA)
                self.state = 483
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_and_const_bis1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.NORMAL_ID)
            else:
                return self.getToken(D96Parser.NORMAL_ID, i)

        def COLLON(self):
            return self.getToken(D96Parser.COLLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_and_const_bis1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_and_const_bis1" ):
                return visitor.visitVar_and_const_bis1(self)
            else:
                return visitor.visitChildren(self)




    def var_and_const_bis1(self):

        localctx = D96Parser.Var_and_const_bis1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_var_and_const_bis1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(D96Parser.NORMAL_ID)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 488
                self.match(D96Parser.COMMA)
                self.state = 489
                self.match(D96Parser.NORMAL_ID)
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.match(D96Parser.COLLON)
            self.state = 496
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_hand_side(self):
            return self.getTypedRuleContext(D96Parser.Left_hand_sideContext,0)


        def EQU(self):
            return self.getToken(D96Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.left_hand_side()
            self.state = 499
            self.match(D96Parser.EQU)
            self.state = 500
            self.expression()
            self.state = 501
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_hand_sideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(D96Parser.Scalar_varContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_left_hand_side)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.index_expression(0)
                self.state = 504
                self.match(D96Parser.LSB)
                self.state = 505
                self.expression()
                self.state = 506
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.scalar_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMAL_ID(self):
            return self.getToken(D96Parser.NORMAL_ID, 0)

        def inst_ob_access(self):
            return self.getTypedRuleContext(D96Parser.Inst_ob_accessContext,0)


        def static_ob_access(self):
            return self.getTypedRuleContext(D96Parser.Static_ob_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = D96Parser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_scalar_var)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(D96Parser.NORMAL_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.inst_ob_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 513
                self.static_ob_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(D96Parser.IF)
            self.state = 517
            self.match(D96Parser.LB)
            self.state = 518
            self.expression()
            self.state = 519
            self.match(D96Parser.RB)
            self.state = 520
            self.block_stmt()
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 521
                self.match(D96Parser.ELSEIF)
                self.state = 522
                self.match(D96Parser.LB)
                self.state = 523
                self.expression()
                self.state = 524
                self.match(D96Parser.RB)
                self.state = 525
                self.block_stmt()
                self.state = 531
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 532
                self.match(D96Parser.ELSE)
                self.state = 533
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(D96Parser.FOREACH)
            self.state = 537
            self.match(D96Parser.LB)
            self.state = 538
            self.expression()
            self.state = 539
            self.match(D96Parser.IN)
            self.state = 540
            self.expression()
            self.state = 541
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 542
            self.expression()
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 543
                self.match(D96Parser.BY)
                self.state = 544
                self.expression()


            self.state = 547
            self.match(D96Parser.RB)
            self.state = 548
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(D96Parser.BREAK)
            self.state = 551
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(D96Parser.CONTINUE)
            self.state = 554
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(D96Parser.RETURN)
            self.state = 558
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 557
                self.expression()


            self.state = 560
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def inst_mth_access(self):
            return self.getTypedRuleContext(D96Parser.Inst_mth_accessContext,0)


        def static_mth_access(self):
            return self.getTypedRuleContext(D96Parser.Static_mth_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 562
                self.inst_mth_access()
                pass

            elif la_ == 2:
                self.state = 563
                self.static_mth_access()
                pass


            self.state = 566
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementsContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementsContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(D96Parser.LP)
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 569
                self.statements()
                self.state = 574
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 575
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_demensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_array_lit)
        try:
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
                self.multi_demensional_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(D96Parser.ARRAY)
            self.state = 582
            self.match(D96Parser.LB)
            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ZERO) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.BOOL_LIT) | (1 << D96Parser.NORMAL_ID) | (1 << D96Parser.STR_LIT))) != 0):
                self.state = 583
                self.list_of_expressions()


            self.state = 586
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_demensional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_of_arrays(self):
            return self.getTypedRuleContext(D96Parser.List_of_arraysContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_demensional_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_demensional_array" ):
                return visitor.visitMulti_demensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_demensional_array(self):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_multi_demensional_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(D96Parser.ARRAY)
            self.state = 589
            self.match(D96Parser.LB)
            self.state = 590
            self.list_of_arrays()
            self.state = 591
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_arraysContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def more_array(self):
            return self.getTypedRuleContext(D96Parser.More_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_arrays

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_arrays" ):
                return visitor.visitList_of_arrays(self)
            else:
                return visitor.visitChildren(self)




    def list_of_arrays(self):

        localctx = D96Parser.List_of_arraysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_list_of_arrays)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.indexed_array()
                self.state = 594
                self.more_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.indexed_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_of_arrays(self):
            return self.getTypedRuleContext(D96Parser.List_of_arraysContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_more_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore_array" ):
                return visitor.visitMore_array(self)
            else:
                return visitor.visitChildren(self)




    def more_array(self):

        localctx = D96Parser.More_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_more_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(D96Parser.COMMA)
            self.state = 600
            self.list_of_arrays()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(D96Parser.ARRAY)
            self.state = 603
            self.match(D96Parser.LSB)
            self.state = 604
            self.type_name()
            self.state = 605
            self.match(D96Parser.COMMA)
            self.state = 606
            self.match(D96Parser.INT_LIT)
            self.state = 607
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_all_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_int_lit" ):
                return visitor.visitAll_int_lit(self)
            else:
                return visitor.visitChildren(self)




    def all_int_lit(self):

        localctx = D96Parser.All_int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_all_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            _la = self._input.LA(1)
            if not(_la==D96Parser.ZERO or _la==D96Parser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.logical_expression_sempred
        self._predicates[30] = self.adding_expression_sempred
        self._predicates[32] = self.multiplying_expression_sempred
        self._predicates[38] = self.index_expression_sempred
        self._predicates[40] = self.object_access_expression_sempred
        self._predicates[46] = self.super_inst_mth_acess_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def object_access_expression_sempred(self, localctx:Object_access_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

    def super_inst_mth_acess_sempred(self, localctx:Super_inst_mth_acessContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         




