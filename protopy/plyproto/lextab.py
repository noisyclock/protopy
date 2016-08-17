# lextab.py. This file automatically created by PLY (version 3.8). Don't edit!
_tabversion   = '3.8'
_lextokens    = {'RPAR', 'LINE_COMMENT', 'OPTION', 'TO', 'SFIXED64', 'SINT32', 'RPC', 'SERVICE', 'NAME', 'REPEATED', 'LBRACE', 'BOOL', 'EXTENSIONS', 'UINT64', 'RBRACE', 'IMPORT', 'STRING', 'LBRACK', 'UINT32', 'FALSE', 'NUM', 'FIXED64', 'STARTTOKEN', 'ENUM', 'RETURNS', 'TRUE', 'MAX', 'SINT64', 'INT32', 'EXTENDS', 'LPAR', 'DOT', 'INT64', 'OPTIONAL', 'SFIXED32', 'PACKAGE', 'BLOCK_COMMENT', 'MESSAGE', 'FLOAT', 'BYTES', 'EXTEND', 'FIXED32', 'EQ', 'SEMI', 'REQUIRED', 'RBRACK', 'DOUBLE', 'STRING_LITERAL'}
_lexreflags   = 0
_lexliterals  = '()+-*/=?:,.^|&~!=[]{};<>@%'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_BLOCK_COMMENT>/\\*(.|\\n)*?\\*/)|(?P<t_NAME>[A-Za-z_$][A-Za-z0-9_$]*)|(?P<t_newline>\\n+)|(?P<t_newline2>(\\r\\n)+)|(?P<t_STRING_LITERAL>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_NUM>[+-]?\\d+)|(?P<t_ignore_LINE_COMMENT>//.*)|(?P<t_LPAR>\\()|(?P<t_LBRACK>\\[)|(?P<t_RPAR>\\))|(?P<t_STARTTOKEN>\\+)|(?P<t_RBRACK>\\])|(?P<t_DOT>\\.)|(?P<t_EQ>=)|(?P<t_RBRACE>})|(?P<t_SEMI>;)|(?P<t_LBRACE>{)', [None, ('t_BLOCK_COMMENT', 'BLOCK_COMMENT'), None, ('t_NAME', 'NAME'), ('t_newline', 'newline'), ('t_newline2', 'newline2'), None, (None, 'STRING_LITERAL'), None, None, (None, 'NUM'), (None, None), (None, 'LPAR'), (None, 'LBRACK'), (None, 'RPAR'), (None, 'STARTTOKEN'), (None, 'RBRACK'), (None, 'DOT'), (None, 'EQ'), (None, 'RBRACE'), (None, 'SEMI'), (None, 'LBRACE')])]}
_lexstateignore = {'INITIAL': ' \t\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
