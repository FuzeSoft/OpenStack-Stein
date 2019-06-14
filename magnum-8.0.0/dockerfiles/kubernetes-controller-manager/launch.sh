#!/bin/sh

. /etc/kubernetes/controller-manager
. /etc/kubernetes/config

ARGS="$@ $KUBE_LOGTOSTDERR $KUBE_LOG_LEVEL $KUBE_MASTER $KUBE_CONTROLLER_MANAGER_ARGS"

ARGS="${ARGS} --secure-port=0"

exec /usr/local/bin/kube-controller-manager $ARGS
