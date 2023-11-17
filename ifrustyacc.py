import ply.yacc as yacc
from ifrustlex import tokens

start='declaration'

def p_declaration(p):
    '''
    declaration : IF LPAREN IDENTIFIER GREATER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE 
                | IF LPAREN IDENTIFIER GREATER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE ELSE FLOWEROPEN FLOWERCLOSE 
                | IF LPAREN IDENTIFIER LESSER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE 
                | IF LPAREN IDENTIFIER LESSER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE ELSE FLOWEROPEN FLOWERCLOSE 
                | IF LPAREN NUMBER RPAREN FLOWEROPEN FLOWERCLOSE 
    '''
    print('valid IF-ELSE declaration')

    #works for the following prompts
    # if(<variable> > <variable>){}
    # if(<variable> > <variable>){}else{}
    # if(<variable> < <variable>){}
    # if(<variable> < <variable>){}else{}
    # if(<number>){}

def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print("Syntax error at EOF")


parser=yacc.yacc()

if __name__=="__main__":
    while True:
        try:
            data=input('enter a if else  ')
            if not data:
                break
            parser.parse(data)
        except EOFError:
            break