import ply.yacc as yacc
from rustarrlex import tokens

start='declaration'

def p_declaration(p):
    '''
    declaration : LET IDENTIFIER EQUAL LPAREN NUMBER RPAREN SEMICOLON
                | LET IDENTIFIER EQUAL LPAREN NUMBER COMMA NUMBER RPAREN SEMICOLON
                | LET IDENTIFIER EQUAL LPAREN NUMBER COMMA NUMBER COMMA NUMBER RPAREN SEMICOLON
    '''
    #works for the following prompts
    # let <variable>=[<number>];
    # let <variable>=[<number>,<number>];
    # let <variable>=[<number>,<number>,<number>];
    print('valid array declaration')

def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print("Syntax error at EOF")


parser=yacc.yacc()

if __name__=="__main__":
    while True:
        try:
            data=input('enter a array declaration  ')
            if not data:
                break
            parser.parse(data)
        except EOFError:
            break