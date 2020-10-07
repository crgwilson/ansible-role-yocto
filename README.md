# Ansible role: Yocto

![Molecule Test](https://github.com/crgwilson/ansible-role-yocto/workflows/Molecule%20Test/badge.svg)

Install all the necessary components for a build environment using the [Yocto Project](https://www.yoctoproject.org/).

* Install required packages as outlined in the [Yocto Project Quick Start Guide](https://www.yoctoproject.org/docs/1.8/yocto-project-qs/yocto-project-qs.html)
* Create a workspace for running builds
* Install [Poky](https://www.yoctoproject.org/software-item/poky/)
* Optionally install layers from the [OpenEmbedded Layer Index](https://layers.openembedded.org/layerindex/branch/master/layers/)

## Variables

### yocto root directory

The root of our yocto workspace. After setup you'll often want to source the `oe-init-build-env`
script from `"{{ yocto_root_directory }}/layers/poky/oe-init-build-env"`

### yocto_version

The default git ref we will be checking out after cloning poky and any other layers.
Defaults to the `dunfell` tag as that is the latest official release.

### yocto_layers_info

Nested dictionary containing info necessary to be able to clone other
OpenEmbedded layers into our project. Each of these layers are required to
provide a `source_uri` and `version` key, mapping to the target git repo, and
the ref to clone respectively.

Comes populated with a handful of layers by default, but other layers may be
provided as well.

### yocto_layers

A list of OpenEmbedded layers to install using info found the the (above) `yocto_layers_info`
variable. Any layer present in this list is expected to be available within `yocto_layers_info`
with both a `source_uri` and a `version`.

## Testing

Testing for this project is setup using
[Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```

## Dependencies

* [ansible-role-git](https://github.com/crgwilson/ansible-role-git)
