
HADOOP_CMD="/usr/local/src/hadoop-1.2.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"

INPUT_FILE_PATH_1="/The_Man_of_Property.txt"
OUTPUT_PATH="/output_cachearchive_broadcast"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.在第四次cacheArchive的基础上改动，输出的结果带.gz扩展名，表示结果是压缩文件
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func WH.gz" \
    -reducer "python red.py reduer_func" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf  "mapred.job.name=cachefile_demo" \
    -jobconf  "mapred.output.compress=true" \
    -jobconf  "mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec" \
    -cacheArchive "hdfs://master:9000/cachefile_dir/white_list_dir.tar.gz#WH.gz" \
    -file "./map.py" \
    -file "./red.py"

