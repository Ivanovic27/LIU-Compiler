// Generated from Liu.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LiuParser}.
 */
public interface LiuListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LiuParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(LiuParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(LiuParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#function_code}.
	 * @param ctx the parse tree
	 */
	void enterFunction_code(LiuParser.Function_codeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#function_code}.
	 * @param ctx the parse tree
	 */
	void exitFunction_code(LiuParser.Function_codeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#instruction}.
	 * @param ctx the parse tree
	 */
	void enterInstruction(LiuParser.InstructionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#instruction}.
	 * @param ctx the parse tree
	 */
	void exitInstruction(LiuParser.InstructionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#definition}.
	 * @param ctx the parse tree
	 */
	void enterDefinition(LiuParser.DefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#definition}.
	 * @param ctx the parse tree
	 */
	void exitDefinition(LiuParser.DefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#identification}.
	 * @param ctx the parse tree
	 */
	void enterIdentification(LiuParser.IdentificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#identification}.
	 * @param ctx the parse tree
	 */
	void exitIdentification(LiuParser.IdentificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#identification2}.
	 * @param ctx the parse tree
	 */
	void enterIdentification2(LiuParser.Identification2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#identification2}.
	 * @param ctx the parse tree
	 */
	void exitIdentification2(LiuParser.Identification2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#terminal_definition}.
	 * @param ctx the parse tree
	 */
	void enterTerminal_definition(LiuParser.Terminal_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#terminal_definition}.
	 * @param ctx the parse tree
	 */
	void exitTerminal_definition(LiuParser.Terminal_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#execution}.
	 * @param ctx the parse tree
	 */
	void enterExecution(LiuParser.ExecutionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#execution}.
	 * @param ctx the parse tree
	 */
	void exitExecution(LiuParser.ExecutionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#execution_function_name}.
	 * @param ctx the parse tree
	 */
	void enterExecution_function_name(LiuParser.Execution_function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#execution_function_name}.
	 * @param ctx the parse tree
	 */
	void exitExecution_function_name(LiuParser.Execution_function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#execution_function_name2}.
	 * @param ctx the parse tree
	 */
	void enterExecution_function_name2(LiuParser.Execution_function_name2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#execution_function_name2}.
	 * @param ctx the parse tree
	 */
	void exitExecution_function_name2(LiuParser.Execution_function_name2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(LiuParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(LiuParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void enterElse_statement(LiuParser.Else_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void exitElse_statement(LiuParser.Else_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#iterate_statement}.
	 * @param ctx the parse tree
	 */
	void enterIterate_statement(LiuParser.Iterate_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#iterate_statement}.
	 * @param ctx the parse tree
	 */
	void exitIterate_statement(LiuParser.Iterate_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(LiuParser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(LiuParser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#definition_function_name}.
	 * @param ctx the parse tree
	 */
	void enterDefinition_function_name(LiuParser.Definition_function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#definition_function_name}.
	 * @param ctx the parse tree
	 */
	void exitDefinition_function_name(LiuParser.Definition_function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#definition_function_name2}.
	 * @param ctx the parse tree
	 */
	void enterDefinition_function_name2(LiuParser.Definition_function_name2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#definition_function_name2}.
	 * @param ctx the parse tree
	 */
	void exitDefinition_function_name2(LiuParser.Definition_function_name2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(LiuParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(LiuParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#parameters2}.
	 * @param ctx the parse tree
	 */
	void enterParameters2(LiuParser.Parameters2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#parameters2}.
	 * @param ctx the parse tree
	 */
	void exitParameters2(LiuParser.Parameters2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#parameters3}.
	 * @param ctx the parse tree
	 */
	void enterParameters3(LiuParser.Parameters3Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#parameters3}.
	 * @param ctx the parse tree
	 */
	void exitParameters3(LiuParser.Parameters3Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#extended_literal}.
	 * @param ctx the parse tree
	 */
	void enterExtended_literal(LiuParser.Extended_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#extended_literal}.
	 * @param ctx the parse tree
	 */
	void exitExtended_literal(LiuParser.Extended_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#basic_literal}.
	 * @param ctx the parse tree
	 */
	void enterBasic_literal(LiuParser.Basic_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#basic_literal}.
	 * @param ctx the parse tree
	 */
	void exitBasic_literal(LiuParser.Basic_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(LiuParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(LiuParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(LiuParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(LiuParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#group}.
	 * @param ctx the parse tree
	 */
	void enterGroup(LiuParser.GroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#group}.
	 * @param ctx the parse tree
	 */
	void exitGroup(LiuParser.GroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#group2}.
	 * @param ctx the parse tree
	 */
	void enterGroup2(LiuParser.Group2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#group2}.
	 * @param ctx the parse tree
	 */
	void exitGroup2(LiuParser.Group2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LiuParser#group3}.
	 * @param ctx the parse tree
	 */
	void enterGroup3(LiuParser.Group3Context ctx);
	/**
	 * Exit a parse tree produced by {@link LiuParser#group3}.
	 * @param ctx the parse tree
	 */
	void exitGroup3(LiuParser.Group3Context ctx);
}