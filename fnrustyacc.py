import ply.yacc as yacc
from fnrustlex import tokens

start='declaration'


def p_declaration(p):
    '''
    declaration : FN  IDENTIFIER LPAREN RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON INT RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON CHAR RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON INT COMMA IDENTIFIER COLON CHAR RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON INT COMMA IDENTIFIER COLON INT RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON CHAR COMMA IDENTIFIER COLON CHAR RPAREN FLOWEROPEN FLOWERCLOSE
                | FN IDENTIFIER LPAREN IDENTIFIER COLON CHAR COMMA IDENTIFIER COLON INT RPAREN FLOWEROPEN FLOWERCLOSE
    '''
    print('valid function declaration')

    #works for the following prompts
    # fn <variable>(){}
    # fn <variable>(<variable>:i32){}
    # fn <variable>(<variable>:char){}
    # fn <variable>(<variable>:i32,<variable>:char){}
    # fn <variable>(<variable>:i32,<variable>:int){}
    # fn <variable>(<variable>:char,<variable>:char){}
    # fn <variable>(<variable>:char,<variable>:int){}

def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print("Syntax error at EOF")


parser=yacc.yacc()

if __name__=="__main__":
    while True:
        try:
            data=input('enter a fn loop declaration  ')
            if not data:
                break
            parser.parse(data)
        except EOFError:
            break