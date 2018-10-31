# Configuration

## Hadoop Cluster

- hdfs-site_master.xml
  - namenode setting
- hdfs-site_slave.xml
  - datanode setting
- mapred-site.xml
  - mapred.framework : yarn
- yarn-site.xml
  - yarn setting
- core-site.xml
  - fs.default.name setting : hdfs://master:9000
- masters 
  - master hostname
- slaves
  - slaves hostname
- hosts
  - master, slave ip setting