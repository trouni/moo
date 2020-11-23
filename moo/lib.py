# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for moo Project
"""

from os.path import split
import datetime
import getpass

pd.set_option('display.width', 200)


def try_me():
    print("\033[92m_________________{:>65}")
    print("")
    print(f"{moo():>70}")
    print("___________  ____{:>65}")
    print("           \\/    \033[0m{:>65}")
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

def moo(username=None):
    username = username if username else getpass.getuser()
    return f'Mooooooo... Hello {username}!'


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import moo
    folder_source, _ = split(moo.__file__)
    moo()
