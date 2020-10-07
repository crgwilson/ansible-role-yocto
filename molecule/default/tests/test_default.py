import pytest


DEBIAN_PACKAGE_LIST = [
    "gawk",
    "wget",
    "diffstat",
    "unzip",
    "texinfo",
    "gcc-multilib",
    "build-essential",
    "chrpath",
    "socat",
    "libsdl1.2-dev",
    "xterm",
]

REDHAT_PACKAGE_LIST = [
    "gawk",
    "make",
    "wget",
    "tar",
    "bzip2",
    "gzip",
    "python",
    "unzip",
    "perl",
    "patch",
    "diffutils",
    "diffstat",
    "cpp",
    "gcc",
    "gcc-c++",
    "glibc-devel",
    "texinfo",
    "chrpath",
    "socat",
    "SDL-devel",
    "xterm",
]


def test_default_packages(host):
    if host.system_info.distribution == "centos":
        package_list = REDHAT_PACKAGE_LIST
    else:
        package_list = DEBIAN_PACKAGE_LIST

    for p in package_list:
        p = host.package(p)
        assert p.is_installed


@pytest.mark.parametrize(
    "path",
    [
        ("/opt/yocto"),
        ("/opt/yocto/layers"),
        ("/opt/yocto/layers/poky"),
        ("/opt/yocto/layers/openembedded-core"),
        ("/opt/yocto/layers/meta-openembedded"),
    ],
)
def test_default_directories(host, path):
    d = host.file(path)
    assert d.is_directory
    assert d.user == "root"
    assert d.group == "root"
    assert d.mode == 0o755
