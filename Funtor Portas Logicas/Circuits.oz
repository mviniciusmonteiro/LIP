functor
import
   Gates at 'Gates.ozf'
%Exportando os circuitos logicos criados
export
   comparator:Comparator
   full_subtractor:FullSubtractor
   circuito3:Circuito3
define
   proc {Comparator X Y Z ?R} % X == Y == Z
      K L
   in
      K = {Gates.xorg X Y}
      L = {Gates.xorg Y Z}
      R = {Gates.norg K L}
   end

   proc {FullSubtractor A B Te ?Ts ?S}
      K L M
   in
      K = {Gates.andg {Gates.notg A} B} % ~A ^ B
      L = {Gates.andg {Gates.notg A} Te} % ~A ^ Te
      M = {Gates.andg B Te} % B ^ Te
      Ts = {Gates.org K {Gates.org L M}} % (~A ^ B) v (~A ^ Te) v (B ^ Te)  
      S = {Gates.xorg Te {Gates.xorg A B}} % (Te v_ (A v_ B))
   end

   proc {Circuito3 A B C ?X}
   	K L 
   in
   	K = {Gates.andg {Gates.notg A} B}
   	L = {Gates.andg B C}
   	X = {Gates.org K L}
   end
end
