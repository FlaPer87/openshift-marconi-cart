OpenShift Marconi Cartridge
===========================

Runs [Marconi](https://github.com/openstack/marconi) on [OpenShift](https://openshift.redhat.com/app/login) using downloadable cartridge support.  To install to OpenShift from the CLI (you'll need version 1.9 or later of rhc), create your app and then run:

    rhc add-cartridge http://marconi-flaper87.rhcloud.com/manifest/master

    Any log output will be generated to $OPENSHIFT_MARCONI_DIR/logs/marconi.log
