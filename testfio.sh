#!/bin/bash
cat <<EOF
EOF

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ioengine=libaio -numjobs=1 -bs=4k -size=4G -group_reporting -rw=randread  -name=1-4k-randread -runtime=30 >> /data/result/1

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ioengine=libaio -numjobs=1 -bs=16k -size=4G -group_reporting -rw=randread -name=1_16k_randread -runtime=30 >> /data/result/4

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ooengine=libaio -numjobs=1 -bs=4k -size=4G -group_reporting -rw=randwrite -name=1-4k-randwrite -runtime=30 >> /data/result/1

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ioengine=libaio -numjobs=1 -bs=4k -size=4G -group_reporting -rw=read -name=1-4k-read -runtime=30 >> /data/result/1

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ioengine=libaio -numjobs=1 -bs=4k -size=4G -group_reporting -rw=write -name=1-4k-write -runtime=30 >> /data/result/1

fio -directory=/data/test -direct=1 -iodepth=4 -thread -ioengine=libaio -numjobs=1 -bs=4k -size=4G -group_reporting -rw=randrw -name=1-4k-randrw -runtime=30 >> /data/result/1


