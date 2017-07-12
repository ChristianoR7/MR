
HADOOP_CMD="/usr/local/src/hadoop-1.2.1/bin/hadoop"
STREAM_JAR_PATH="/usr/local/src/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"

INPUT_FILE_PATH_1="/The_Man_of_Property.txt"
OUTPUT_PATH="/output_cachefile_broadcast"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.cachefile的意思是将white_list上传到hafs上并且给其一个别名，命名为WWWHHH，并且此任务也起了一个叫demo的名字
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func WWWHHH" \
    -reducer "python red.py reduer_func" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf  "mapred.job.name=cachefile_demo" \
    -cacheFile "hdfs://master:9000/cachefile_dir/white_list/white_list.txt#WWWHHH" \
    -file "./map.py" \
    -file "./red.py"

    #-cacheFile "$HDFS_FILE_PATH#WH" \

