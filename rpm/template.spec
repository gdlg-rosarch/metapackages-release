Name:           ros-lunar-ros-core
Version:        1.3.1
Release:        0%{?dist}
Summary:        ROS ros_core package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-catkin
Requires:       ros-lunar-cmake-modules
Requires:       ros-lunar-common-msgs
Requires:       ros-lunar-gencpp
Requires:       ros-lunar-geneus
Requires:       ros-lunar-genlisp
Requires:       ros-lunar-genmsg
Requires:       ros-lunar-gennodejs
Requires:       ros-lunar-genpy
Requires:       ros-lunar-message-generation
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-ros
Requires:       ros-lunar-ros-comm
Requires:       ros-lunar-rosbag-migration-rule
Requires:       ros-lunar-rosconsole-bridge
Requires:       ros-lunar-roscpp-core
Requires:       ros-lunar-rosgraph-msgs
Requires:       ros-lunar-roslisp
Requires:       ros-lunar-rospack
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
BuildRequires:  ros-lunar-catkin

%description
A metapackage to aggregate the packages required to use publish / subscribe,
services, launch files, and other core ROS concepts.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon May 08 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.3.1-0
- Autogenerated by Bloom

* Sun Apr 30 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.3.0-0
- Autogenerated by Bloom

