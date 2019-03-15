// Generated from Liu.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LiuLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Colon=1, Coma=2, Left_par=3, Right_par=4, Left_bracket=5, Right_bracket=6, 
		Dot=7, Dash=8, If=9, Else=10, Iterate=11, Return=12, Boolean=13, Id=14, 
		String=15, Ws=16, Number=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"Colon", "Coma", "Left_par", "Right_par", "Left_bracket", "Right_bracket", 
			"Dot", "Dash", "If", "Else", "Iterate", "Return", "Boolean", "Id", "String", 
			"Ws", "Number"
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


	public LiuLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Liu.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23z\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5"+
		"\16V\n\16\3\17\3\17\7\17Z\n\17\f\17\16\17]\13\17\3\20\3\20\3\20\3\20\7"+
		"\20c\n\20\f\20\16\20f\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\6\22o\n"+
		"\22\r\22\16\22p\3\22\3\22\6\22u\n\22\r\22\16\22v\5\22y\n\22\2\2\23\3\3"+
		"\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21"+
		"!\22#\23\3\2\b\5\2C\\aac|\6\2\62;C\\aac|\3\2))\6\2\f\f\17\17))^^\4\2\f"+
		"\f\17\17\5\2\13\f\16\17\"\"\2\u0080\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23"+
		"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2"+
		"\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2"+
		"\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63\3\2\2\2\23"+
		"\65\3\2\2\2\258\3\2\2\2\27=\3\2\2\2\31E\3\2\2\2\33U\3\2\2\2\35W\3\2\2"+
		"\2\37^\3\2\2\2!i\3\2\2\2#n\3\2\2\2%&\7<\2\2&\4\3\2\2\2\'(\7.\2\2(\6\3"+
		"\2\2\2)*\7*\2\2*\b\3\2\2\2+,\7+\2\2,\n\3\2\2\2-.\7}\2\2.\f\3\2\2\2/\60"+
		"\7\177\2\2\60\16\3\2\2\2\61\62\7\60\2\2\62\20\3\2\2\2\63\64\7/\2\2\64"+
		"\22\3\2\2\2\65\66\7k\2\2\66\67\7h\2\2\67\24\3\2\2\289\7g\2\29:\7n\2\2"+
		":;\7u\2\2;<\7g\2\2<\26\3\2\2\2=>\7k\2\2>?\7v\2\2?@\7g\2\2@A\7t\2\2AB\7"+
		"c\2\2BC\7v\2\2CD\7g\2\2D\30\3\2\2\2EF\7t\2\2FG\7g\2\2GH\7v\2\2HI\7w\2"+
		"\2IJ\7t\2\2JK\7p\2\2K\32\3\2\2\2LM\7V\2\2MN\7t\2\2NO\7w\2\2OV\7g\2\2P"+
		"Q\7H\2\2QR\7c\2\2RS\7n\2\2ST\7u\2\2TV\7g\2\2UL\3\2\2\2UP\3\2\2\2V\34\3"+
		"\2\2\2W[\t\2\2\2XZ\t\3\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\"+
		"\36\3\2\2\2][\3\2\2\2^d\t\4\2\2_c\n\5\2\2`a\7^\2\2ac\n\6\2\2b_\3\2\2\2"+
		"b`\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2\2fd\3\2\2\2gh\t\4\2\2"+
		"h \3\2\2\2ij\t\7\2\2jk\3\2\2\2kl\b\21\2\2l\"\3\2\2\2mo\4\62;\2nm\3\2\2"+
		"\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qx\3\2\2\2rt\7\60\2\2su\4\62;\2ts\3\2"+
		"\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2xr\3\2\2\2xy\3\2\2\2y$\3\2"+
		"\2\2\n\2U[bdpvx\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}