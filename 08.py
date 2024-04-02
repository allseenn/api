import sys
!{sys.executable} -m pip install -U pip --user
!{sys.executable} -m pip install -U codeium-jupyter --user
!jupyter nbextension install --py codeium --user
!jupyter nbextension enable --py codeium --user
!jupyter serverextension enable --py codeium --user

import sys
!{sys.executable} -m pip install -U pip
!{sys.executable} -m pip install -U codeium-jupyter
!jupyter nbextension install --py codeium --user
!jupyter nbextension enable --py codeium --user
!jupyter serverextension enable --py codeium --user

jupyter nbextension enable codeium --user --py
