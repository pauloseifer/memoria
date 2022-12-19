oi(um).
oi(dois).
oi(três).

javai(dois).
tchau(X) :- oi(X), javai(X).
    
%fatorial(1, 1).
%fatorial(N, Result) :- M is N - 1.
%fatorial(M, ProxResult), Result is ProxResult * N.

fatorial(0, 1).
fatorial(N, Resultado) :-
    N > 0,
    N1 is N - 1,
    fatorial(N1, R),
    Resultado is R * N.

multiplica(X, Y, Z) :-
    Z is X * Y.
