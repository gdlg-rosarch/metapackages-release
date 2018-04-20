# Script generated with Bloom
pkgdesc="ROS - A metapackage to aggregate the packages required to use publish / subscribe, services, launch files, and other core ROS concepts."


pkgname='ros-kinetic-ros-core'
pkgver='1.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-common-msgs'
'ros-kinetic-gencpp'
'ros-kinetic-geneus'
'ros-kinetic-genlisp'
'ros-kinetic-genmsg'
'ros-kinetic-gennodejs'
'ros-kinetic-genpy'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-ros'
'ros-kinetic-ros-comm'
'ros-kinetic-rosbag-migration-rule'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp-core'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-roslisp'
'ros-kinetic-rospack'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
)

conflicts=()
replaces=()

_dir=ros_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_core $srcdir/ros_core
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

