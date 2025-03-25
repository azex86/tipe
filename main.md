$ \frac{du_c(t)}{dt} * C = i(t) $  
$ U_r = R*i(t)$  
$ E = U_g(t) = U_r(t) + U_c(t) $  
d'où $U_g(t) = R*i(t) + U_c(t) = R*C*\frac{dU_c(t)}{dt} + U_c(t)$  
c'est à dire  avec la méthode d'Euler
  
  $\frac{dU_g(t+h)}{dt} = \frac{U_g(t) - U_c(t)}{RC}$  
  $ U_c(t+h) = U_c(t) + \frac{dU_c(t+h)}{dt} * h$  
