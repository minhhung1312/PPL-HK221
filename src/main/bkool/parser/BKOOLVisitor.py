# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_declaration.
    def visitClass_declaration(self, ctx:BKOOLParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_declare.
    def visitAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutable_declare.
    def visitMutable_declare(self, ctx:BKOOLParser.Mutable_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutable_declare.
    def visitImmutable_declare(self, ctx:BKOOLParser.Immutable_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_var_declare.
    def visitList_var_declare(self, ctx:BKOOLParser.List_var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_var_declare_immu.
    def visitList_var_declare_immu(self, ctx:BKOOLParser.List_var_declare_immuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_declare.
    def visitMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor_declare.
    def visitConstructor_declare(self, ctx:BKOOLParser.Constructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_declare.
    def visitVar_declare(self, ctx:BKOOLParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_declare_immu.
    def visitVar_declare_immu(self, ctx:BKOOLParser.Var_declare_immuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_params.
    def visitList_params(self, ctx:BKOOLParser.List_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter_type.
    def visitParameter_type(self, ctx:BKOOLParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_attribute.
    def visitType_attribute(self, ctx:BKOOLParser.Type_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_statement.
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_attribute.
    def visitLocal_attribute(self, ctx:BKOOLParser.Local_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKOOLParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_invo.
    def visitAttribute_invo(self, ctx:BKOOLParser.Attribute_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_statement.
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_statement.
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_statement.
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_statement.
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:BKOOLParser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_methodinvo.
    def visitObj_methodinvo(self, ctx:BKOOLParser.Obj_methodinvoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_exp.
    def visitBool_exp(self, ctx:BKOOLParser.Bool_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_exp.
    def visitInt_exp(self, ctx:BKOOLParser.Int_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_exp.
    def visitReturn_exp(self, ctx:BKOOLParser.Return_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_exp.
    def visitIndex_exp(self, ctx:BKOOLParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#object_create.
    def visitObject_create(self, ctx:BKOOLParser.Object_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_exp.
    def visitList_exp(self, ctx:BKOOLParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_exps.
    def visitList_exps(self, ctx:BKOOLParser.List_expsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_literal.
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_literal_basic.
    def visitList_literal_basic(self, ctx:BKOOLParser.List_literal_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal_basic.
    def visitLiteral_basic(self, ctx:BKOOLParser.Literal_basicContext):
        return self.visitChildren(ctx)



del BKOOLParser