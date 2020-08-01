GENCCODE_ASSEMBLY_TYPE=-a gcc-darwin
SO=dylib
SOBJ=dylib
A=a
LIBPREFIX=lib
LIB_EXT_ORDER=.67.1.dylib
COMPILE=/Users/runner/miniforge3/conda-bld/icu_1588856494613/_build_env/bin/clang -DU_ATTRIBUTE_DEPRECATED= -D_FORTIFY_SOURCE=2 -mmacosx-version-min=10.9 -isystem /Users/michael/opt/anaconda3/envs/tesserocr_env/include   -DU_HAVE_STRTOD_L=1 -DU_HAVE_XLOCALE_H=1 -DU_HAVE_STRING_VIEW=1  -march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -isystem /Users/michael/opt/anaconda3/envs/tesserocr_env/include -fdebug-prefix-map=/Users/runner/miniforge3/conda-bld/icu_1588856494613/work=/usr/local/src/conda/icu-67.1 -fdebug-prefix-map=/Users/michael/opt/anaconda3/envs/tesserocr_env=/usr/local/src/conda-prefix -std=c11 -Wall -pedantic -Wshadow -Wpointer-arith -Wmissing-prototypes -Wwrite-strings   -fno-common -c
LIBFLAGS=-I/Users/michael/opt/anaconda3/envs/tesserocr_env/include  -dynamic
GENLIB=/Users/runner/miniforge3/conda-bld/icu_1588856494613/_build_env/bin/clang -dynamiclib -dynamic -march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -isystem /Users/michael/opt/anaconda3/envs/tesserocr_env/include -fdebug-prefix-map=/Users/runner/miniforge3/conda-bld/icu_1588856494613/work=/usr/local/src/conda/icu-67.1 -fdebug-prefix-map=/Users/michael/opt/anaconda3/envs/tesserocr_env=/usr/local/src/conda-prefix -std=c11 -Wall -pedantic -Wshadow -Wpointer-arith -Wmissing-prototypes -Wwrite-strings   -Wl,-pie -Wl,-headerpad_max_install_names -Wl,-dead_strip_dylibs -Wl,-rpath,/Users/michael/opt/anaconda3/envs/tesserocr_env/lib -L/Users/michael/opt/anaconda3/envs/tesserocr_env/lib -Wl,-rpath,/Users/michael/opt/anaconda3/envs/tesserocr_env/lib 
LDICUDTFLAGS=
LD_SONAME=-Wl,-compatibility_version -Wl,67 -Wl,-current_version -Wl,67.1 -install_name /Users/michael/opt/anaconda3/envs/tesserocr_env/lib/
RPATH_FLAGS=
BIR_LDFLAGS=
AR=/Users/runner/miniforge3/conda-bld/icu_1588856494613/_build_env/bin/x86_64-apple-darwin13.4.0-ar
ARFLAGS=r -c
RANLIB=/Users/runner/miniforge3/conda-bld/icu_1588856494613/_build_env/bin/x86_64-apple-darwin13.4.0-ranlib
INSTALL_CMD=/usr/bin/install -c
