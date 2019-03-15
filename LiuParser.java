// Generated from Liu.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LiuParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Colon=1, Coma=2, Left_par=3, Right_par=4, Left_bracket=5, Right_bracket=6, 
		Dot=7, Dash=8, If=9, Else=10, Iterate=11, Return=12, Boolean=13, Id=14, 
		String=15, Ws=16, Number=17;
	public static final int
		RULE_program = 0, RULE_function_code = 1, RULE_instruction = 2, RULE_definition = 3, 
		RULE_identification = 4, RULE_identification2 = 5, RULE_terminal_definition = 6, 
		RULE_execution = 7, RULE_execution_function_name = 8, RULE_execution_function_name2 = 9, 
		RULE_if_statement = 10, RULE_else_statement = 11, RULE_iterate_statement = 12, 
		RULE_return_statement = 13, RULE_definition_function_name = 14, RULE_definition_function_name2 = 15, 
		RULE_parameters = 16, RULE_parameters2 = 17, RULE_parameters3 = 18, RULE_extended_literal = 19, 
		RULE_basic_literal = 20, RULE_literal = 21, RULE_function = 22, RULE_group = 23, 
		RULE_group2 = 24, RULE_group3 = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "function_code", "instruction", "definition", "identification", 
			"identification2", "terminal_definition", "execution", "execution_function_name", 
			"execution_function_name2", "if_statement", "else_statement", "iterate_statement", 
			"return_statement", "definition_function_name", "definition_function_name2", 
			"parameters", "parameters2", "parameters3", "extended_literal", "basic_literal", 
			"literal", "function", "group", "group2", "group3"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':'", "','", "'('", "')'", "'{'", "'}'", "'.'", "'-'", "'if'", 
			"'else'", "'iterate'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Colon", "Coma", "Left_par", "Right_par", "Left_bracket", "Right_bracket", 
			"Dot", "Dash", "If", "Else", "Iterate", "Return", "Boolean", "Id", "String", 
			"Ws", "Number"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Liu.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LiuParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public Function_codeContext function_code() {
			return getRuleContext(Function_codeContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			function_code();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_codeContext extends ParserRuleContext {
		public InstructionContext instruction() {
			return getRuleContext(InstructionContext.class,0);
		}
		public TerminalNode Dot() { return getToken(LiuParser.Dot, 0); }
		public Function_codeContext function_code() {
			return getRuleContext(Function_codeContext.class,0);
		}
		public Function_codeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_code; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterFunction_code(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitFunction_code(this);
		}
	}

	public final Function_codeContext function_code() throws RecognitionException {
		Function_codeContext _localctx = new Function_codeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function_code);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Left_par) | (1L << If) | (1L << Iterate) | (1L << Return) | (1L << Id))) != 0)) {
				{
				setState(54);
				instruction();
				setState(55);
				match(Dot);
				setState(56);
				function_code();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstructionContext extends ParserRuleContext {
		public DefinitionContext definition() {
			return getRuleContext(DefinitionContext.class,0);
		}
		public ExecutionContext execution() {
			return getRuleContext(ExecutionContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public InstructionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterInstruction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitInstruction(this);
		}
	}

	public final InstructionContext instruction() throws RecognitionException {
		InstructionContext _localctx = new InstructionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instruction);
		try {
			setState(63);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				execution();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(62);
				return_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefinitionContext extends ParserRuleContext {
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public TerminalNode Colon() { return getToken(LiuParser.Colon, 0); }
		public Extended_literalContext extended_literal() {
			return getRuleContext(Extended_literalContext.class,0);
		}
		public Definition_function_nameContext definition_function_name() {
			return getRuleContext(Definition_function_nameContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public DefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterDefinition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitDefinition(this);
		}
	}

	public final DefinitionContext definition() throws RecognitionException {
		DefinitionContext _localctx = new DefinitionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_definition);
		try {
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				identification();
				setState(66);
				match(Colon);
				setState(67);
				extended_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				definition_function_name();
				setState(70);
				match(Colon);
				setState(71);
				function();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentificationContext extends ParserRuleContext {
		public TerminalNode Id() { return getToken(LiuParser.Id, 0); }
		public Identification2Context identification2() {
			return getRuleContext(Identification2Context.class,0);
		}
		public IdentificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identification; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterIdentification(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitIdentification(this);
		}
	}

	public final IdentificationContext identification() throws RecognitionException {
		IdentificationContext _localctx = new IdentificationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_identification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(Id);
			setState(76);
			identification2();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Identification2Context extends ParserRuleContext {
		public TerminalNode Id() { return getToken(LiuParser.Id, 0); }
		public Identification2Context identification2() {
			return getRuleContext(Identification2Context.class,0);
		}
		public Identification2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identification2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterIdentification2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitIdentification2(this);
		}
	}

	public final Identification2Context identification2() throws RecognitionException {
		Identification2Context _localctx = new Identification2Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_identification2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(78);
				match(Id);
				setState(79);
				identification2();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Terminal_definitionContext extends ParserRuleContext {
		public TerminalNode Id() { return getToken(LiuParser.Id, 0); }
		public TerminalNode Colon() { return getToken(LiuParser.Colon, 0); }
		public Basic_literalContext basic_literal() {
			return getRuleContext(Basic_literalContext.class,0);
		}
		public Definition_function_nameContext definition_function_name() {
			return getRuleContext(Definition_function_nameContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public Terminal_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminal_definition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterTerminal_definition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitTerminal_definition(this);
		}
	}

	public final Terminal_definitionContext terminal_definition() throws RecognitionException {
		Terminal_definitionContext _localctx = new Terminal_definitionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_terminal_definition);
		try {
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				match(Id);
				setState(83);
				match(Colon);
				setState(84);
				basic_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				definition_function_name();
				setState(86);
				match(Colon);
				setState(87);
				function();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExecutionContext extends ParserRuleContext {
		public Execution_function_nameContext execution_function_name() {
			return getRuleContext(Execution_function_nameContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public Iterate_statementContext iterate_statement() {
			return getRuleContext(Iterate_statementContext.class,0);
		}
		public ExecutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execution; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterExecution(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitExecution(this);
		}
	}

	public final ExecutionContext execution() throws RecognitionException {
		ExecutionContext _localctx = new ExecutionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_execution);
		try {
			setState(94);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Left_par:
			case Id:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				execution_function_name();
				}
				break;
			case If:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				if_statement();
				}
				break;
			case Iterate:
				enterOuterAlt(_localctx, 3);
				{
				setState(93);
				iterate_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Execution_function_nameContext extends ParserRuleContext {
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Execution_function_name2Context execution_function_name2() {
			return getRuleContext(Execution_function_name2Context.class,0);
		}
		public Execution_function_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execution_function_name; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterExecution_function_name(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitExecution_function_name(this);
		}
	}

	public final Execution_function_nameContext execution_function_name() throws RecognitionException {
		Execution_function_nameContext _localctx = new Execution_function_nameContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_execution_function_name);
		try {
			setState(104);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Id:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				identification();
				setState(97);
				group();
				setState(98);
				execution_function_name2();
				}
				break;
			case Left_par:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				group();
				setState(101);
				identification();
				setState(102);
				execution_function_name2();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Execution_function_name2Context extends ParserRuleContext {
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public Execution_function_name2Context execution_function_name2() {
			return getRuleContext(Execution_function_name2Context.class,0);
		}
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Execution_function_name2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execution_function_name2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterExecution_function_name2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitExecution_function_name2(this);
		}
	}

	public final Execution_function_name2Context execution_function_name2() throws RecognitionException {
		Execution_function_name2Context _localctx = new Execution_function_name2Context(_ctx, getState());
		enterRule(_localctx, 18, RULE_execution_function_name2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Id:
				{
				setState(106);
				identification();
				setState(107);
				execution_function_name2();
				}
				break;
			case Left_par:
				{
				setState(109);
				group();
				setState(110);
				execution_function_name2();
				}
				break;
			case Coma:
			case Right_par:
			case Dot:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode If() { return getToken(LiuParser.If, 0); }
		public List<GroupContext> group() {
			return getRuleContexts(GroupContext.class);
		}
		public GroupContext group(int i) {
			return getRuleContext(GroupContext.class,i);
		}
		public Else_statementContext else_statement() {
			return getRuleContext(Else_statementContext.class,0);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterIf_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitIf_statement(this);
		}
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(If);
			setState(115);
			group();
			setState(116);
			group();
			setState(117);
			else_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_statementContext extends ParserRuleContext {
		public TerminalNode Else() { return getToken(LiuParser.Else, 0); }
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public Else_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterElse_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitElse_statement(this);
		}
	}

	public final Else_statementContext else_statement() throws RecognitionException {
		Else_statementContext _localctx = new Else_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(119);
				match(Else);
				setState(120);
				group();
				}
				break;
			case 2:
				{
				setState(121);
				match(Else);
				setState(122);
				if_statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Iterate_statementContext extends ParserRuleContext {
		public TerminalNode Iterate() { return getToken(LiuParser.Iterate, 0); }
		public List<GroupContext> group() {
			return getRuleContexts(GroupContext.class);
		}
		public GroupContext group(int i) {
			return getRuleContext(GroupContext.class,i);
		}
		public Iterate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterate_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterIterate_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitIterate_statement(this);
		}
	}

	public final Iterate_statementContext iterate_statement() throws RecognitionException {
		Iterate_statementContext _localctx = new Iterate_statementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_iterate_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(Iterate);
			setState(126);
			group();
			setState(127);
			group();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode Return() { return getToken(LiuParser.Return, 0); }
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterReturn_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitReturn_statement(this);
		}
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(Return);
			setState(130);
			group();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Definition_function_nameContext extends ParserRuleContext {
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public Definition_function_name2Context definition_function_name2() {
			return getRuleContext(Definition_function_name2Context.class,0);
		}
		public Definition_function_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition_function_name; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterDefinition_function_name(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitDefinition_function_name(this);
		}
	}

	public final Definition_function_nameContext definition_function_name() throws RecognitionException {
		Definition_function_nameContext _localctx = new Definition_function_nameContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_definition_function_name);
		try {
			setState(140);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Id:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				identification();
				setState(133);
				parameters();
				setState(134);
				definition_function_name2();
				}
				break;
			case Left_par:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				parameters();
				setState(137);
				identification();
				setState(138);
				definition_function_name2();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Definition_function_name2Context extends ParserRuleContext {
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public Definition_function_name2Context definition_function_name2() {
			return getRuleContext(Definition_function_name2Context.class,0);
		}
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public Definition_function_name2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition_function_name2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterDefinition_function_name2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitDefinition_function_name2(this);
		}
	}

	public final Definition_function_name2Context definition_function_name2() throws RecognitionException {
		Definition_function_name2Context _localctx = new Definition_function_name2Context(_ctx, getState());
		enterRule(_localctx, 30, RULE_definition_function_name2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Id:
				{
				setState(142);
				identification();
				setState(143);
				definition_function_name2();
				}
				break;
			case Left_par:
				{
				setState(145);
				parameters();
				setState(146);
				definition_function_name2();
				}
				break;
			case Colon:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParametersContext extends ParserRuleContext {
		public TerminalNode Left_par() { return getToken(LiuParser.Left_par, 0); }
		public Parameters3Context parameters3() {
			return getRuleContext(Parameters3Context.class,0);
		}
		public TerminalNode Right_par() { return getToken(LiuParser.Right_par, 0); }
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterParameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitParameters(this);
		}
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_parameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(Left_par);
			setState(151);
			parameters3();
			setState(152);
			match(Right_par);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameters2Context extends ParserRuleContext {
		public TerminalNode Coma() { return getToken(LiuParser.Coma, 0); }
		public DefinitionContext definition() {
			return getRuleContext(DefinitionContext.class,0);
		}
		public Parameters2Context parameters2() {
			return getRuleContext(Parameters2Context.class,0);
		}
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public Parameters2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterParameters2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitParameters2(this);
		}
	}

	public final Parameters2Context parameters2() throws RecognitionException {
		Parameters2Context _localctx = new Parameters2Context(_ctx, getState());
		enterRule(_localctx, 34, RULE_parameters2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(154);
				match(Coma);
				setState(155);
				definition();
				setState(156);
				parameters2();
				}
				break;
			case 2:
				{
				setState(158);
				match(Coma);
				setState(159);
				identification();
				setState(160);
				parameters2();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameters3Context extends ParserRuleContext {
		public DefinitionContext definition() {
			return getRuleContext(DefinitionContext.class,0);
		}
		public Parameters2Context parameters2() {
			return getRuleContext(Parameters2Context.class,0);
		}
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public Parameters3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterParameters3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitParameters3(this);
		}
	}

	public final Parameters3Context parameters3() throws RecognitionException {
		Parameters3Context _localctx = new Parameters3Context(_ctx, getState());
		enterRule(_localctx, 36, RULE_parameters3);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(164);
				definition();
				setState(165);
				parameters2();
				}
				break;
			case 2:
				{
				setState(167);
				identification();
				setState(168);
				parameters2();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Extended_literalContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public GroupContext group() {
			return getRuleContext(GroupContext.class,0);
		}
		public Extended_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extended_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterExtended_literal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitExtended_literal(this);
		}
	}

	public final Extended_literalContext extended_literal() throws RecognitionException {
		Extended_literalContext _localctx = new Extended_literalContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_extended_literal);
		try {
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(173);
				group();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Basic_literalContext extends ParserRuleContext {
		public TerminalNode String() { return getToken(LiuParser.String, 0); }
		public TerminalNode Number() { return getToken(LiuParser.Number, 0); }
		public TerminalNode Boolean() { return getToken(LiuParser.Boolean, 0); }
		public ExecutionContext execution() {
			return getRuleContext(ExecutionContext.class,0);
		}
		public IdentificationContext identification() {
			return getRuleContext(IdentificationContext.class,0);
		}
		public Basic_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_basic_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterBasic_literal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitBasic_literal(this);
		}
	}

	public final Basic_literalContext basic_literal() throws RecognitionException {
		Basic_literalContext _localctx = new Basic_literalContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_basic_literal);
		try {
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				match(String);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(177);
				match(Number);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(178);
				match(Boolean);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(179);
				execution();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(180);
				identification();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Basic_literalContext basic_literal() {
			return getRuleContext(Basic_literalContext.class,0);
		}
		public Terminal_definitionContext terminal_definition() {
			return getRuleContext(Terminal_definitionContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal);
		try {
			setState(185);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				basic_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
				terminal_definition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode Left_bracket() { return getToken(LiuParser.Left_bracket, 0); }
		public Function_codeContext function_code() {
			return getRuleContext(Function_codeContext.class,0);
		}
		public TerminalNode Right_bracket() { return getToken(LiuParser.Right_bracket, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(Left_bracket);
			setState(188);
			function_code();
			setState(189);
			match(Right_bracket);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GroupContext extends ParserRuleContext {
		public TerminalNode Left_par() { return getToken(LiuParser.Left_par, 0); }
		public Group2Context group2() {
			return getRuleContext(Group2Context.class,0);
		}
		public TerminalNode Right_par() { return getToken(LiuParser.Right_par, 0); }
		public GroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterGroup(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitGroup(this);
		}
	}

	public final GroupContext group() throws RecognitionException {
		GroupContext _localctx = new GroupContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_group);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(Left_par);
			setState(192);
			group2();
			setState(193);
			match(Right_par);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group2Context extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Group3Context group3() {
			return getRuleContext(Group3Context.class,0);
		}
		public Group2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterGroup2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitGroup2(this);
		}
	}

	public final Group2Context group2() throws RecognitionException {
		Group2Context _localctx = new Group2Context(_ctx, getState());
		enterRule(_localctx, 48, RULE_group2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Left_par) | (1L << If) | (1L << Iterate) | (1L << Boolean) | (1L << Id) | (1L << String) | (1L << Number))) != 0)) {
				{
				setState(195);
				literal();
				setState(196);
				group3();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group3Context extends ParserRuleContext {
		public TerminalNode Coma() { return getToken(LiuParser.Coma, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Group3Context group3() {
			return getRuleContext(Group3Context.class,0);
		}
		public Group3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).enterGroup3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LiuListener ) ((LiuListener)listener).exitGroup3(this);
		}
	}

	public final Group3Context group3() throws RecognitionException {
		Group3Context _localctx = new Group3Context(_ctx, getState());
		enterRule(_localctx, 50, RULE_group3);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Coma) {
				{
				setState(200);
				match(Coma);
				setState(201);
				literal();
				setState(202);
				group3();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23\u00d1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\3\2\3\2\3\3\3\3\3\3\3\3\5\3=\n\3\3\4\3\4\3\4\5\4"+
		"B\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5L\n\5\3\6\3\6\3\6\3\7\3\7\5\7"+
		"S\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\\\n\b\3\t\3\t\3\t\5\ta\n\t\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nk\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13"+
		"s\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r~\n\r\3\16\3\16\3\16\3\16"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u008f\n\20"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0097\n\21\3\22\3\22\3\22\3\22\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00a5\n\23\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\5\24\u00ad\n\24\3\25\3\25\5\25\u00b1\n\25\3\26\3\26\3\26\3"+
		"\26\3\26\5\26\u00b8\n\26\3\27\3\27\5\27\u00bc\n\27\3\30\3\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u00c9\n\32\3\33\3\33\3\33\3\33"+
		"\5\33\u00cf\n\33\3\33\2\2\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \""+
		"$&(*,.\60\62\64\2\2\2\u00d2\2\66\3\2\2\2\4<\3\2\2\2\6A\3\2\2\2\bK\3\2"+
		"\2\2\nM\3\2\2\2\fR\3\2\2\2\16[\3\2\2\2\20`\3\2\2\2\22j\3\2\2\2\24r\3\2"+
		"\2\2\26t\3\2\2\2\30}\3\2\2\2\32\177\3\2\2\2\34\u0083\3\2\2\2\36\u008e"+
		"\3\2\2\2 \u0096\3\2\2\2\"\u0098\3\2\2\2$\u00a4\3\2\2\2&\u00ac\3\2\2\2"+
		"(\u00b0\3\2\2\2*\u00b7\3\2\2\2,\u00bb\3\2\2\2.\u00bd\3\2\2\2\60\u00c1"+
		"\3\2\2\2\62\u00c8\3\2\2\2\64\u00ce\3\2\2\2\66\67\5\4\3\2\67\3\3\2\2\2"+
		"89\5\6\4\29:\7\t\2\2:;\5\4\3\2;=\3\2\2\2<8\3\2\2\2<=\3\2\2\2=\5\3\2\2"+
		"\2>B\5\b\5\2?B\5\20\t\2@B\5\34\17\2A>\3\2\2\2A?\3\2\2\2A@\3\2\2\2B\7\3"+
		"\2\2\2CD\5\n\6\2DE\7\3\2\2EF\5(\25\2FL\3\2\2\2GH\5\36\20\2HI\7\3\2\2I"+
		"J\5.\30\2JL\3\2\2\2KC\3\2\2\2KG\3\2\2\2L\t\3\2\2\2MN\7\20\2\2NO\5\f\7"+
		"\2O\13\3\2\2\2PQ\7\20\2\2QS\5\f\7\2RP\3\2\2\2RS\3\2\2\2S\r\3\2\2\2TU\7"+
		"\20\2\2UV\7\3\2\2V\\\5*\26\2WX\5\36\20\2XY\7\3\2\2YZ\5.\30\2Z\\\3\2\2"+
		"\2[T\3\2\2\2[W\3\2\2\2\\\17\3\2\2\2]a\5\22\n\2^a\5\26\f\2_a\5\32\16\2"+
		"`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2a\21\3\2\2\2bc\5\n\6\2cd\5\60\31\2de\5\24"+
		"\13\2ek\3\2\2\2fg\5\60\31\2gh\5\n\6\2hi\5\24\13\2ik\3\2\2\2jb\3\2\2\2"+
		"jf\3\2\2\2k\23\3\2\2\2lm\5\n\6\2mn\5\24\13\2ns\3\2\2\2op\5\60\31\2pq\5"+
		"\24\13\2qs\3\2\2\2rl\3\2\2\2ro\3\2\2\2rs\3\2\2\2s\25\3\2\2\2tu\7\13\2"+
		"\2uv\5\60\31\2vw\5\60\31\2wx\5\30\r\2x\27\3\2\2\2yz\7\f\2\2z~\5\60\31"+
		"\2{|\7\f\2\2|~\5\26\f\2}y\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\31\3\2\2\2\177"+
		"\u0080\7\r\2\2\u0080\u0081\5\60\31\2\u0081\u0082\5\60\31\2\u0082\33\3"+
		"\2\2\2\u0083\u0084\7\16\2\2\u0084\u0085\5\60\31\2\u0085\35\3\2\2\2\u0086"+
		"\u0087\5\n\6\2\u0087\u0088\5\"\22\2\u0088\u0089\5 \21\2\u0089\u008f\3"+
		"\2\2\2\u008a\u008b\5\"\22\2\u008b\u008c\5\n\6\2\u008c\u008d\5 \21\2\u008d"+
		"\u008f\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u008a\3\2\2\2\u008f\37\3\2\2"+
		"\2\u0090\u0091\5\n\6\2\u0091\u0092\5 \21\2\u0092\u0097\3\2\2\2\u0093\u0094"+
		"\5\"\22\2\u0094\u0095\5 \21\2\u0095\u0097\3\2\2\2\u0096\u0090\3\2\2\2"+
		"\u0096\u0093\3\2\2\2\u0096\u0097\3\2\2\2\u0097!\3\2\2\2\u0098\u0099\7"+
		"\5\2\2\u0099\u009a\5&\24\2\u009a\u009b\7\6\2\2\u009b#\3\2\2\2\u009c\u009d"+
		"\7\4\2\2\u009d\u009e\5\b\5\2\u009e\u009f\5$\23\2\u009f\u00a5\3\2\2\2\u00a0"+
		"\u00a1\7\4\2\2\u00a1\u00a2\5\n\6\2\u00a2\u00a3\5$\23\2\u00a3\u00a5\3\2"+
		"\2\2\u00a4\u009c\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5"+
		"%\3\2\2\2\u00a6\u00a7\5\b\5\2\u00a7\u00a8\5$\23\2\u00a8\u00ad\3\2\2\2"+
		"\u00a9\u00aa\5\n\6\2\u00aa\u00ab\5$\23\2\u00ab\u00ad\3\2\2\2\u00ac\u00a6"+
		"\3\2\2\2\u00ac\u00a9\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\'\3\2\2\2\u00ae"+
		"\u00b1\5,\27\2\u00af\u00b1\5\60\31\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3"+
		"\2\2\2\u00b1)\3\2\2\2\u00b2\u00b8\7\21\2\2\u00b3\u00b8\7\23\2\2\u00b4"+
		"\u00b8\7\17\2\2\u00b5\u00b8\5\20\t\2\u00b6\u00b8\5\n\6\2\u00b7\u00b2\3"+
		"\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7"+
		"\u00b6\3\2\2\2\u00b8+\3\2\2\2\u00b9\u00bc\5*\26\2\u00ba\u00bc\5\16\b\2"+
		"\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc-\3\2\2\2\u00bd\u00be\7"+
		"\7\2\2\u00be\u00bf\5\4\3\2\u00bf\u00c0\7\b\2\2\u00c0/\3\2\2\2\u00c1\u00c2"+
		"\7\5\2\2\u00c2\u00c3\5\62\32\2\u00c3\u00c4\7\6\2\2\u00c4\61\3\2\2\2\u00c5"+
		"\u00c6\5,\27\2\u00c6\u00c7\5\64\33\2\u00c7\u00c9\3\2\2\2\u00c8\u00c5\3"+
		"\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\63\3\2\2\2\u00ca\u00cb\7\4\2\2\u00cb"+
		"\u00cc\5,\27\2\u00cc\u00cd\5\64\33\2\u00cd\u00cf\3\2\2\2\u00ce\u00ca\3"+
		"\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\65\3\2\2\2\24<AKR[`jr}\u008e\u0096\u00a4"+
		"\u00ac\u00b0\u00b7\u00bb\u00c8\u00ce";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}