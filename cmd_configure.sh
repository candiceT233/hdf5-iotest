
UUID_INCLUDE=`spack find -p uuid | awk '/util-linux-uuid/ {print $NF "/include"}'`

CFLAGS="-I$UUID_INCLUDE" CC=h5cc ./configure --prefix=$HOME/install/hdf5iotest