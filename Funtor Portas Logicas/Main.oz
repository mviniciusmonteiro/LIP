functor
import
   Browser
   Circuits at 'Circuits.ozf'
define
   %Circuito Comparador
   X = 1|1|1|_
   Y = 1|1|1|_
   Z = 1|1|1|_ R
   {Circuits.comparator X Y Z R}
   {Browser.browse 'Circuito 1:'}
   {Browser.browse R}
   
   %Circuito Subtrator Completo
   A = 0|0|0|0|1|1|1|1|_
   B = 0|0|1|1|0|0|1|1|_
   Te = 0|1|0|1|0|1|0|1|_ Ts S
   {Circuits.full_subtractor A B Te Ts S}
   {Browser.browse 'Circuito 2:'}
   {Browser.browse Ts}
   {Browser.browse S}
   
   %Terceiro Circuito criado
   C = 0|1|0|1|0|1|0|1|_ P
   {Circuits.circuito3 A B C P}
   {Browser.browse 'Circuito 3:'}
   {Browser.browse P}
end
