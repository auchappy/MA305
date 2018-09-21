!=======================================================================
!        Calculates Machine Epsilon 
!....&---1---------2---------3---------4---------5---------6---------7--
!####&###1#########2#########3#########4#########5#########6#########7##
         program m_epsilon
         real(kind(1.d0)) :: eps, one, two
         integer :: temp

         eps = 1.d0
         one = 1.d0
         two = 2.d0

         do while(one+eps .GT. one)
            eps = eps/two
         enddo
         eps=two*eps 

         temp = int(log(eps)/log(two))

         write(*,*)
         write(*,'(a,es23.16, a, i3)') 'eps =', eps, ' = 2^', temp 
         write(*,*)

        stop

      end program m_epsilon
!_______________________________________________________________________
!####.###1#########2#########3#########4#########5#########6#########7##

