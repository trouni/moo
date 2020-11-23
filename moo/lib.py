# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for moo Project
"""

from os.path import split
import pandas as pd
import datetime
import getpass

pd.set_option('display.width', 200)


def try_me():
    print("\033[92m{:>65}".format(f'_________________'))
    print("")
    print(moo())
    print("{:>65}".format(f'___________  ____'))
    print("{:>65}\033[0m".format(f'           \/    '))
    print("""
                                 .a@@@@@a.     ,a@@@@@@@@a,     .a@@@@@a. 
                              .@@@@@@@@@@@a,a@@@@@@@@@@@@@@a,a@@@@@@@@@@@. 
                              @@@@@@@@@@@@a@@@@@@@@@@@@@@@@@@a@@@@@@@@@@@@ 
                               @@@@'    `@a@@@@@@@@@@@@@@@@@@@@a@'   `@@@@ 
                               `@'        @@@@@@@@@@@@@@@@@@@@@@       `@' 
              .########################## @@@@@@@@@\"@@@\"@@@@@@@@ 
           .##############################`@@@@@@@@a@@@a@@@@@@@' 
         .#####################;;#########,@@@@@@@@@@@@@@@@@@@@, 
       ,;;;;;######;;;;#####;;;;;;;##;;;,@@@@@@@@@@@@@@@@@@@@@@@@, 
     ,;;;;;;;;;;;;;;;;;;###;;;;;;;;;;;;;@@@@@( )@@@@@@@@@@( )@@@@@ 
    ;;';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;`@@@@@@@@@@@@@@@@@@@@@@@@' 
   ;;';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;`@@@@@@@@@@@@@@@@@@@@', 
  ;;' ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; \"\"\"\"\"\"\"\"\"\"\"\"\"\",;;  ', 
 ;;'  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;    ', 
;;;;  ###;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;####;;;;;;;;;;;;;;      ; 
`;;'  ####;;;##;;;;;;;;;;;;;;;;;;;;;;;;;;###########;;;;;;;;;;;    ,' 
  `   ##########;;;;;;;'''''''''''''''''''''''''''###;;;;;;;;;;    ; 
      #############;;'                            #;;;;;;;;;;;;     `, 
      #############                               ;;;;;;;;;;;;;     () 
      #############                               ;;;;;;;;;;;;; 
      #oOOOOOOOOOo#                               ;oOOOOOOOOOo; 
    oOOOOOOOOOOOOOOOo                           oOOOOOOOOOOOOOOOo 
   OOOOOOOOOOOOOOOOOOO                         OOOOOOOOOOOOOOOOOOO 
   OOOOOOO () OOOOOOOO                         OOOOOOOO () OOOOOOO 
   `OOOOOOOooOOOOOOOO'                         `OOOOOOOOooOOOOOOO' 
     `OOOOOOOOOOOOO'                             `OOOOOOOOOOOOO' 
        \"\"\"\"\"\"\"\"\"                                   \"\"\"\"\"\"\"\"\"
    """)
    pass

def moo():
    return "{:>70}".format(f'Mooooooo... Hello {getpass.getuser()}!')


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import moo
    folder_source, _ = split(moo.__file__)
    moo()
