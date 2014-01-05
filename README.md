OpenShift Marconi Cartridge
===========================

Runs [Marconi](https://github.com/openstack/marconi) on [OpenShift](https://openshift.redhat.com/app/login) using downloadable cartridge support.  To install to OpenShift from the CLI (you'll need version 1.9 or later of rhc), create your app and then run:

    rhc add-cartridge http://cartreflect-claytondev.rhcloud.com/reflect?github=flaper87/openshift-marconi-cart

    Any log output will be generated to $OPENSHIFT_MARCONI_DIR/logs/marconi.log
