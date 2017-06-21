# source this file to access LAL
export LAL_PREFIX
LAL_PREFIX="/home/daniel/.virtualenvs/IGRlaptop21/minke"
export PYTHONPATH
PYTHONPATH=`echo "$PYTHONPATH" | /bin/sed -e 's|/home/daniel/.virtualenvs/IGRlaptop21/minke/lib/python2.7/site-packages:||g;'`
PYTHONPATH="/home/daniel/.virtualenvs/IGRlaptop21/minke/lib/python2.7/site-packages:$PYTHONPATH"
export MANPATH
MANPATH=`echo "$MANPATH" | /bin/sed -e 's|/home/daniel/.virtualenvs/IGRlaptop21/minke/share/man:||g;'`
MANPATH="/home/daniel/.virtualenvs/IGRlaptop21/minke/share/man:$MANPATH"
export LAL_DATADIR
LAL_DATADIR="/home/daniel/.virtualenvs/IGRlaptop21/minke/share/lal"
export PATH
PATH=`echo "$PATH" | /bin/sed -e 's|/home/daniel/.virtualenvs/IGRlaptop21/minke/bin:||g;'`
PATH="/home/daniel/.virtualenvs/IGRlaptop21/minke/bin:$PATH"
export PKG_CONFIG_PATH
PKG_CONFIG_PATH=`echo "$PKG_CONFIG_PATH" | /bin/sed -e 's|/home/daniel/.virtualenvs/IGRlaptop21/minke/lib/pkgconfig:||g;'`
PKG_CONFIG_PATH="/home/daniel/.virtualenvs/IGRlaptop21/minke/lib/pkgconfig:$PKG_CONFIG_PATH"
