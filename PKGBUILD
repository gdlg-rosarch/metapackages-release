# Script generated with Bloom
pkgdesc="ROS - A metapackage which extends ros_base and includes ROS libaries for any robot hardware. It may not contain any GUI dependencies."


pkgname='ros-kinetic-robot'
pkgver='1.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-control-msgs'
'ros-kinetic-diagnostics'
'ros-kinetic-executive-smach'
'ros-kinetic-filters'
'ros-kinetic-geometry'
'ros-kinetic-robot-model'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-ros-base'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=robot
source=()
md5sums=()

prepare() {
    cp -R $startdir/robot $srcdir/robot
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

