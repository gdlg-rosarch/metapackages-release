# Script generated with Bloom
pkgdesc="ROS - A metapackage which extends ros_core and includes other basic non-robot tools like actionlib, dynamic reconfigure, nodelets, and pluginlib."


pkgname='ros-kinetic-ros-base'
pkgver='1.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-bond-core'
'ros-kinetic-class-loader'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-nodelet-core'
'ros-kinetic-pluginlib'
'ros-kinetic-ros-core'
)

conflicts=()
replaces=()

_dir=ros_base
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_base $srcdir/ros_base
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

