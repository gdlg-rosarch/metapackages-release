Name:           ros-jade-ros-base
Version:        1.1.3
Release:        0%{?dist}
Summary:        ROS ros_base package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-actionlib
Requires:       ros-jade-bond-core
Requires:       ros-jade-class-loader
Requires:       ros-jade-common-tutorials
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-nodelet-core
Requires:       ros-jade-pluginlib
Requires:       ros-jade-ros-core
BuildRequires:  ros-jade-catkin

%description
A metapackage which extends ros_core and includes other basic non-robot tools
like actionlib, dynamic reconfigure, nodelets, and pluginlib.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Apr 30 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.1.3-0
- Autogenerated by Bloom

