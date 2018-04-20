# Script generated with Bloom
pkgdesc="ROS - A metapackage to aggregate the packages required to use publish / subscribe, services, launch files, and other core ROS concepts."


pkgname='ros-lunar-ros-core'
pkgver='1.3.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-common-msgs'
'ros-lunar-gencpp'
'ros-lunar-geneus'
'ros-lunar-genlisp'
'ros-lunar-genmsg'
'ros-lunar-gennodejs'
'ros-lunar-genpy'
'ros-lunar-message-generation'
'ros-lunar-message-runtime'
'ros-lunar-ros'
'ros-lunar-ros-comm'
'ros-lunar-rosbag-migration-rule'
'ros-lunar-rosconsole-bridge'
'ros-lunar-roscpp-core'
'ros-lunar-rosgraph-msgs'
'ros-lunar-roslisp'
'ros-lunar-rospack'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

