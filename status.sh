#!/bin/bash
case ${1:-''} in 
	start|stop|status|restart)
		systemctl $@ mysqld
		exit $?
	;;
	*)
	exit 1
	;;
esac
