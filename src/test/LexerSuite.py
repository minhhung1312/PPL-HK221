import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    def test_5(self):
        self.assertTrue(TestLexer.test("___________", "___________,<EOF>", 105))

    def test_6(self):
        self.assertTrue(TestLexer.test("asdfabc____12312321______", "asdfabc____12312321______,<EOF>", 106))

    def test_7(self):
        self.assertTrue(TestLexer.test(": =", ":,=,<EOF>", 107))

    def test_8(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 108))

    def test_9(self):
        self.assertTrue(TestLexer.test("555500000", "555500000,<EOF>", 109))

    def test_10(self):
        self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 110))

    def test_11(self):
        self.assertTrue(TestLexer.test("123456789", "123456789,<EOF>", 111))

    def test_12(self):
        self.assertTrue(TestLexer.test("102e-99", "102e-99,<EOF>", 112))

    def test_13(self):
        self.assertTrue(TestLexer.test("0.33E-1", "0.33E-1,<EOF>", 113))

    def test_14(self):
        self.assertTrue(TestLexer.test(".123", ".,123,<EOF>", 114))

    def test_15(self):
        self.assertTrue(TestLexer.test("1611dasas6a51d5a1s", "1611,dasas6a51d5a1s,<EOF>", 115))

    def test_16(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 116))

    def test_17(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 117))

    def test_18(self):
        self.assertTrue(TestLexer.test("#aaaa", "<EOF>", 118))

    def test_19(self):
        self.assertTrue(TestLexer.test("#aaa##a", "<EOF>", 119))

    def test_20(self):
        self.assertTrue(TestLexer.test("#bacd/*cse*/", "<EOF>", 120))

    def test_21(self):
        self.assertTrue(TestLexer.test("#aa/*a*/a/*/*/*/*/*/*/*/*/*/*//*", "<EOF>", 121))
    
    def test_22(self):
        self.assertTrue(TestLexer.test("""12.3E10""", """12.3E10,<EOF>""", 122))

    def test_23(self):
        self.assertTrue(TestLexer.test("""0000002762E+10""", """0000002762E+10,<EOF>""", 123))

    def test_24(self):
        self.assertTrue(TestLexer.test("""00000012E9-0""", """00000012E9,-,0,<EOF>""", 124))

    def test_25(self):
        self.assertTrue(TestLexer.test("/*so so so ###  390423432~~~~ ... so # ..*/", "<EOF>", 125))

    def test_26(self):
        self.assertTrue(TestLexer.test("/*cba////### ...*/ abc", "abc,<EOF>", 126))

    def test_27(self):
        input = """
            /* note
            comment out
            */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_28(self):
        self.assertTrue(TestLexer.test("\"abc\"", """"abc",<EOF>""", 128))

    def test_29(self):
        input = "\" \\naaakcbaskbcska\\t\""
        expect = """" \\naaakcbaskbcska\\t",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_30(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: \"", 130))

    def test_31(self):
        input = """"She asked me and require: \\"Where is John?\\"" """
        expect = """"She asked me and require: \\"Where is John?\\"",<EOF>"""
        self.assertTrue(
            TestLexer.test(input, expect, 131))

    def test_32(self):
        self.assertTrue(TestLexer.test("\"He asked me: ", "Unclosed String: \"He asked me: ", 132))

    def test_33(self):
        input = """class area extends AH {
                        float getArea(){
                            return this.length*this.width / 2;
                        }
                }"""
        expect = "class,area,extends,AH,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_34(self):
        input = "+-*/>>=/[]$"
        expect = "+,-,*,/,>,>=,/,[,],Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("\"SHe", "Unclosed String: \"SHe", 135))

    def test_36(self):
        input = "static final float abc = 2.05;"
        expect = "static,final,float,abc,=,2.05,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_37(self):
        input = "abc?cdef?ach*"
        expect = "abc,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_38(self):
        input = "boolean break class continue do else extends float if int new string then for void nil this final static to "
        expect = "boolean,break,class,continue,do,else,extends,float,if,int,new,string,then,for,void,nil,this,final,static,to,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_39(self):
        input = "A a new () {testcase39 ne ?}"
        expect = "A,a,new,(,),{,testcase39,ne,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_40(self):
        input = "cx743abcd + 1258.e8"
        expect = "cx743abcd,+,1258.e8,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_41(self):
        input = "l = 5, c = 2;"
        expect = "l,=,5,,,c,=,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_42(self):
        self.assertTrue(TestLexer.test(""" "This contains a tab\t" """, """"This contains a tab\t",<EOF>""", 142))

    def test_43(self):
        input = "\"abc\\e messenger def\""
        expect = "Illegal Escape In String: \"abc\\e"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_44(self):
        input = "~!^^^^!"
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_45(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_46(self):
        input = """a= \"He said: \" Im Super\" s \" testtt \" \"; __world = 5; imple = 8;"""
        expect = """a,=,"He said: ",Im,Super," s ",testtt," ",;,__world,=,5,;,imple,=,8,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_47(self):
        input = """a= \"He said: \" Hello \" \n \";"""
        expect = """a,=,"He said: ",Hello,Unclosed String: " """
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_48(self):
        input = "{2.3, 4.2, 102e3,23conmuc}"
        expect = "{,2.3,,,4.2,,,102e3,,,23,conmuc,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_49(self):
        input = "a[4] = {1, 2, 3, 4, 5}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,,,5,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_50(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_51(self):
        input = "a[3 + x.foo(2)] := a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_52(self):
        input = "s:=r*r*this.myPI;"
        expect = "s,:=,r,*,r,*,this,.,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_53(self):
        input = "1/2/3/4/5/6"
        expect = "1,/,2,/,3,/,4,/,5,/,6,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_54(self):
        input = "\" \\h \""
        expect = "Illegal Escape In String: \" \h"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_55(self):
        self.assertTrue(TestLexer.test("final static int x = 5", "final,static,int,x,=,5,<EOF>", 155))

    def test_56(self):
        self.assertTrue(TestLexer.test("{1,2,3,4}", "{,1,,,2,,,3,,,4,},<EOF>", 156))

    def test_57(self):
        self.assertTrue(TestLexer.test("+ - * / ()[]{?}", "+,-,*,/,(,),[,],{,Error Token ?", 157))

    def test_58(self):
        self.assertTrue(TestLexer.test("new X()", "new,X,(,),<EOF>", 158))

    def test_59(self):
        self.assertTrue(TestLexer.test("== != >= <=", "==,!=,>=,<=,<EOF>", 159))

    def test_60(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.n()[3]", "x,.,b,[,2,],:=,x,.,n,(,),[,3,],<EOF>", 160))

    def test_61(self):
        self.assertTrue(TestLexer.test("this.method", "this,.,method,<EOF>", 161))

    def test_62(self):
        self.assertTrue(TestLexer.test("""0o567 0O77""","""0,o567,0,O77,<EOF>""", 162))

    def test_63(self):
        self.assertTrue(TestLexer.test("value := x.foo(5)", "value,:=,x,.,foo,(,5,),<EOF>", 163))

    def test_64(self):
        self.assertTrue(TestLexer.test( "abc - xyz","abc,-,xyz,<EOF>", 164))

    def test_65(self):
        self.assertTrue(TestLexer.test("if then else", "if,then,else,<EOF>", 165))

    def test_66(self):
        self.assertTrue(TestLexer.test("for x:=1 to 2 do writeln(x);", "for,x,:=,1,to,2,do,writeln,(,x,),;,<EOF>", 166))

    def test_67(self):
        self.assertTrue(TestLexer.test("\"        \"", """"        ",<EOF>""", 167))

    def test_68(self):
        self.assertTrue(
            TestLexer.test("io.writeIntLn(this.factorial(x));", "io,.,writeIntLn,(,this,.,factorial,(,x,),),;,<EOF>",168))

    def test_69(self):
        self.assertTrue(TestLexer.test(""" s = "string           
        "a = 4
        g = 9 """,
            """s,=,Unclosed String: "string           """, 169))

    def test_70(self):
        self.assertTrue(TestLexer.test("break continue nil", "break,continue,nil,<EOF>", 170))

    def test_71(self):
        self.assertTrue(TestLexer.test("""Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        """,
            """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>""", 171))

    def test_72(self):
        self.assertTrue(TestLexer.test("a `= b", "a,Error Token `", 172))

    def test_73(self):
        self.assertTrue(TestLexer.test(""" "1"  abc "2" """, """"1",abc,"2",<EOF>""", 173))

    def test_74(self):
        self.assertTrue(TestLexer.test("""Var: x;
        Function: gcd
            Parameter: a,b
            Body:
                If (b == 0) Return a;
                Else Return gcd(b,a%b);
                EndIf.
            EndBody.""",
            """Var,:,x,;,Function,:,gcd,Parameter,:,a,,,b,Body,:,If,(,b,==,0,),Return,a,;,Else,Return,gcd,(,b,,,a,%,b,),;,EndIf,.,EndBody,.,<EOF>""", 174))

    def test_75(self):
        self.assertTrue(TestLexer.test(""" "Ligal\\\ " """, """"Ligal\\\ ",<EOF>""", 175))

    def test_76(self):
        self.assertTrue(TestLexer.test(""" "jasonmamoa \\k """, """Illegal Escape In String: "jasonmamoa \\k""", 176))

    def test_77(self):
        self.assertTrue(TestLexer.test("""** Hello
        World!!! **""",
            """*,*,Hello,World,!,!,!,*,*,<EOF>""", 177))

    def test_78(self):
        self.assertTrue(TestLexer.test("a*3+afdsfb   - 1", "a,*,3,+,afdsfb,-,1,<EOF>", 178))

    def test_79(self):
        self.assertTrue(TestLexer.test("a3%dasfdb2b", "a3,%,dasfdb2b,<EOF>", 179))

    def test_80(self):
        self.assertTrue(TestLexer.test("""foo(2 + x, 4. \. y);""",
            """foo,(,2,+,x,,,4.,\,.,y,),;,<EOF>""", 180))

    def test_81(self):
        self.assertTrue(TestLexer.test("string a := ~b", "string,a,:=,Error Token ~", 181))

    def test_82(self):
        self.assertTrue(
            TestLexer.test(""" "Illegal \\b escape \\l" """, """Illegal Escape In String: "Illegal \\b escape \\l""",182))

    def test_83(self):
        self.assertTrue(TestLexer.test("5.2e-30", "5.2e-30,<EOF>", 183))

    def test_84(self):
        input = """
             void main(){
                 int x;
                 x:= io.readInt();
             }
        """
        expect = """void,main,(,),{,int,x,;,x,:=,io,.,readInt,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_85(self):
        self.assertTrue(TestLexer.test("io.readBool();", "io,.,readBool,(,),;,<EOF>", 185))

    def test_86(self):
        self.assertTrue(TestLexer.test("Shape.getNum();", "Shape,.,getNum,(,),;,<EOF>", 186))

    def test_87(self):
        inputs = """
            class Shape {
                float length, width;
                float getArea() {
                }
            }
        """
        expect = "class,Shape,{,float,length,,,width,;,float,getArea,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(inputs, expect, 187))

    def test_88(self):
        inputs = """
        Shape(float length, width) {
                this.length := length;
                this.width := width;
        }
        """
        expect = "Shape,(,float,length,,,width,),{,this,.,length,:=,length,;,this,.,width,:=,width,;,},<EOF>"
        self.assertTrue(TestLexer.test(inputs, expect, 188))

    def test_89(self):
        input = """
            class Rectangle extends Shape {
                float getArea() {
                    float return this.length*this.width;
                }
            }
        """
        expect = "class,Rectangle,extends,Shape,{,float,getArea,(,),{,float,return,this,.,length,*,this,.,width,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_90(self):
        input = """
            class Triangle extends Shape {
                float getArea() {
                    float return this.length*this.width/2;
                }
            }
        """
        expect = "class,Triangle,extends,Shape,{,float,getArea,(,),{,float,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_91(self):
        input = """
            class Ex2 {
                void main() {
                    Shape s;
                    s:= new Rectangle(3,4);
                }
            }
        """
        expect = "class,Ex2,{,void,main,(,),{,Shape,s,;,s,:=,new,Rectangle,(,3,,,4,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_92(self):
        self.assertTrue(TestLexer.test("bool x = true;", "bool,x,=,true,;,<EOF>", 192))

    def test_93(self):
        self.assertTrue(TestLexer.test("""abc**qwe**Test**""",
            """abc,*,*,qwe,*,*,Test,*,*,<EOF>""", 193))

    def test_94(self):
        self.assertTrue(TestLexer.test("""(*-101*) 11.+12*#$""",
            """(,*,-,101,*,),11.,+,12,*,<EOF>""", 194))

    def test_95(self):
        input = """
            for x:= 5 downto 2 do 
            io.writeIntLn(x);
        """
        expect = "for,x,:=,5,downto,2,do,io,.,writeIntLn,(,x,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_96(self):
        self.assertTrue(TestLexer.test("a >= b <c", "a,>=,b,<,c,<EOF>", 196))

    def test_97(self):
        self.assertTrue(TestLexer.test("asfm@c34;", "asfm,Error Token @", 197))

    def test_98(self):
        self.assertTrue(TestLexer.test("""kz-70S9+0s)f<)?0gg""",
            """kz,-,70,S9,+,0,s,),f,<,),Error Token ?""", 198))

    def test_99(self):
        self.assertTrue(TestLexer.test(""" "Ok I am fine ~" """, """"Ok I am fine ~",<EOF>""", 199))

    def test_100(self):
        self.assertTrue(TestLexer.test("""12.e0 -101 11.E 11.1e2""",
            """12.e0,-,101,11.,E,11.1e2,<EOF>""", 200))