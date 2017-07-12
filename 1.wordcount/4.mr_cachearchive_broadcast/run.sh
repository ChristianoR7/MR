
HADOOP_CMD="/usr/local/src/hadoop-1.2.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"

INPUT_FILE_PATH_1="/The_Man_of_Property.txt"
OUTPUT_PATH="/output_cachearchive_broadcast"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1. 如果该文件过大，需要将其压缩之后上传到hdfs上，此时用的就是-cacheArchive,压缩文件所在的路径作为一个别名为WH.gz
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func WH.gz" \
    -reducer "python red.py reduer_func" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf  "mapred.job.name=cachefile_demo" \
    -cacheArchive "hdfs://master:9000/w.tar.gz#WH.gz" \ #压缩文件所在的路径，改路径也作为一个别名为WH.gz
    -file "./map.py" \
    -file "./red.py"

