# spark-unit-testing
To be able to develop and test PySpark locally you need to have Spark available. This repository shows an example how to do that.

Note: it is also possible to mock Spark. While this enables testing, it does still require access to Spark for development.

## Required environment

This depends on a locally running container with Spark. First install Docker, then run:

```
git clone https://github.com/Blogem/docker-spark.git
cd docker-spark
./build.sh
docker run --name spark-master -h spark-master -p 7077:7077 -p 8080:8080 -e ENABLE_INIT_DAEMON=false -d bde2020/spark-master:3.1.1-hadoop3.2
```

Spark Web UI is now available at http://localhost:8080.

but how to connect to it using pyspark?