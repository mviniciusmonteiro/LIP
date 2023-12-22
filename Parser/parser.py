def is_ident(x):
    return isinstance(x, str)

def id(s1):
    x, sn = s1[0], s1[1:]
    if is_ident(x):
        return x, sn

def sequence(non_term, sep, s1):
  x1, s2 = non_term(s1)
  t, s3 = s2[0], s2[1:]
  if sep(t):
    x2, sn = sequence(non_term, sep, s3)
    return (f"{t}({x1} {x2})", sn)
  else:
    return (x1, s2)

def comp(s1):
  return sequence(expr, cop, s1)

def expr(s1):
  return sequence(term, eop, s1)

def term(s1):
  return sequence(fact, top, s1)

def fact(s1):
  t = s1[0]
  if isinstance(t, int) or is_ident(t):
    s2 = s1[1:]
    return (t, s2)
  else:
    if s1[0] == "(":
      e, s3 = expr(s1[1:])
      if s3[0] == ")":
        return e, s3[1:]

def cop(y):
  return y in ['<', '>', '=<', '>=', '==', '!=']
def eop(y):
  return y in ['+', '-']
def top(y):
  return y in ['*', '/']

def stat(s1):
    t, s2 = s1[0], s1[1:]
    match t:
      case "begin":
         s2, sn = sequence(stat, lambda x: x == ';', s2)  
         if sn[0] == "end":
           return (s2, sn[1:])
      case "if": 
        c, s3 = comp(s2)
        if s3[0] == "then":
          s4 = s3[1:]
          x, s5 = stat(s4)
          if s5[0] == "else":
            s6 = s5[1:]
            x2, sn = stat(s6)
            return (f"if({c} {x} {x2})", sn)
      case "while":
        c, s3 = comp(s2)
        if s3[0] == "do":
          s4 = s3[1:]
          x, sn = stat(s4)
          return(f"while({c} {x})", sn)
      case "read":
        i, sn = id(s2)
        return (f"read({i}", sn)
      case "write":
        e, sn = expr(s2)
        return (f"write({e}", sn)
      case _:
        if is_ident(t):
            if s2[0] == ":=":
              s3 = s2[1:]
              e, sn = expr(s3)
              return (f"assign({t}, {e})",sn)
        else: 
            return (s1) 

def prog(s1):
    if s1[0] == "program":  
        s2 = s1[1:]      
        y, s3 = id(s2)   
        if s3[0] == ";":
            s4 = s3[1:]
            z, s5 = stat(s4)   
            if s5[0] == "end": 
                return(f"prog({y} {z})") 

# Tokenize a entrada e execute o programa
input = ["program", "foo", ";", "while", "a", "+", 3, "<", "b", "do", "b", ":=", "b", "+", 1, "end"]

resultado = prog(input)
print(resultado)

#resultado dev ser: prog(foo while(´<´(´+´(a 3) b) assign(b ´+´(b 1))))