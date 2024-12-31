#coding:utf-8
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, IntegerType, FloatType, DoubleType, StructType
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.functions import count,avg,regexp_extract,max
from pyspark.sql.functions import col, sum, when
from pyspark.sql.functions import desc,asc

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark").master("local[*]") \
        .config("spark.sql.shuffle.partitions", 2) \
        .config("spark.sql.warehouse.dir", "hdfs://node1:8020/user/hive/warehouse") \
        .config("hive.metastore.uris", "thrift://node1:9083") \
        .enableHiveSupport() \
        .getOrCreate()

    sc = spark.sparkContext
    #读取数据表
    jobData = spark.read.table("jobData")

    #需求1，城市平均工资前10
    top_city = jobData.groupBy("city")\
        .agg(avg("maxSalary")\
        .alias("avgSalary"))\
        .orderBy(desc("avgSalary"))
    result1 = top_city.limit(10)

    result1.write.mode("overwrite"). \
        format("jdbc"). \
        option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
        option("dbtable", "averageCity"). \
        option("user", "root"). \
        option("password", "root"). \
        option("encoding", "utf-8"). \
        save()
    result1.write.mode("overwrite").saveAsTable("averageCity", "parquet")
    spark.sql("SELECT * FROM averageCity").show()

    # #需求二 工资区间
    # jobData_classfiy = jobData.withColumn("salary_category",
    #                                       when(col("maxSalary").between(0,5000), "0-5k")
    #                                       .when(col("maxSalary").between(5000,7000), "5k-7k")
    #                                       .when(col("maxSalary").between(7000,10000), "7k-10k")
    #                                       .when(col("maxSalary").between(100000,20000), "10k-20k")
    #                                       .when(col("maxSalary")>20000, "20k以上")
    #                                       .otherwise("未分类"))
    #
    # result2 = jobData_classfiy.groupBy("salary_category").agg(count("*").alias("count"))
    #
    # result2.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "salaryCategory"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result2.write.mode("overwrite").saveAsTable("salaryCategory", "parquet")
    # spark.sql("SELECT * FROM salaryCategory").show()
    #
    #
    # #需求三 工资经验分析
    # result3 = jobData_classfiy.groupBy("workExperience")\
    #     .agg(avg("maxSalary").alias("avg_max_salary"),
    #          avg("minSalary").alias("avg_min_salary"))\
    #    .orderBy("workExperience")
    #
    # result3.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "workExperience"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result3.write.mode("overwrite").saveAsTable("workExperience", "parquet")
    # spark.sql("SELECT * FROM workExperience").show()
    #
    # # 需求四  城市分布
    # result4 = jobData_classfiy.groupBy("city").count()
    # result4.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "addresssum"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result4.write.mode("overwrite").saveAsTable("addresssum", "parquet")
    # spark.sql("SELECT * FROM addresssum").show()
    #
    #
    # job_df = jobData.withColumn("people_num", when(col("companyPeople").rlike(r'-'),
    #                                                  regexp_extract(col("companyPeople"), r'(\d+)-(\d+)', 1).cast("int"))
    #                             .otherwise(col("companyPeople").cast("int")))
    # people_classify = job_df.withColumn("people_category",
    #                                       when(col("people_num").between(0,10), "0-10人")
    #                                      .when(col("people_num").between(10,50), "10-50人")
    #                                      .when(col("people_num").between(50,150), "50-150人")
    #                                      .when(col("people_num").between(150,500), "150-500人")
    #                                      .when(col("people_num").between(500,1000), "500-1000人")
    #                                     .when(col("people_num")>1000, "1000人以上")
    #                                     .otherwise("未分类"))
    # result5 = people_classify.groupBy("people_category").agg(count("*").alias("count"))
    # result5.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "peopleCategory"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result5.write.mode("overwrite").saveAsTable("peopleCategory", "parquet")
    # spark.sql("SELECT * FROM peopleCategory").show()
    #
    # top_10_salary = jobData.orderBy(col("maxSalary").desc()).limit(10)
    #
    # top_10_salary.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "salaryTop"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # top_10_salary.write.mode("overwrite").saveAsTable("salaryTop", "parquet")
    # spark.sql("SELECT * FROM salaryTop").show()


    #需求6 薪资分析 行业薪资
    result6 = jobData.groupBy("type").agg(
        sum(when(col("maxSalary")<=5000, 1).otherwise(0)).alias("0-5000"),
        sum(when(col("maxSalary").between(5001,7000), 1).otherwise(0)).alias("5001-7000"),
        sum(when(col("maxSalary").between(7001,10000), 1).otherwise(0)).alias("7001-10000"),
        sum(when(col("maxSalary").between(10001,20000), 1).otherwise(0)).alias("10001-20000"),
        sum(when(col("maxSalary")>20000, 1).otherwise(0)).alias("20000以上")
    )

    result6.write.mode("overwrite"). \
        format("jdbc"). \
        option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
        option("dbtable", "typeSalary"). \
        option("user", "root"). \
        option("password", "root"). \
        option("encoding", "utf-8"). \
        save()
    result6.write.mode("overwrite").saveAsTable("typeSalary", "parquet")
    spark.sql("SELECT * FROM typeSalary").show()

    #需求7行业平均薪资
    result7 = jobData.groupBy("type").agg(avg(col("maxSalary").alias("avg_max_salary")))
    result7.write.mode("overwrite"). \
        format("jdbc"). \
        option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
        option("dbtable", "averageType"). \
        option("user", "root"). \
        option("password", "root"). \
        option("encoding", "utf-8"). \
        save()
    result7.write.mode("overwrite").saveAsTable("averageType", "parquet")
    spark.sql("SELECT * FROM averageType").show()

    #需求8 经验平均薪资和个数
    result8 = jobData.groupBy("workExperience").agg(
        avg(col("maxSalary")).alias("avgSalary"),
        count("*").alias("count")
    )
    result8.write.mode("overwrite"). \
        format("jdbc"). \
        option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
        option("dbtable", "averageExperience"). \
        option("user", "root"). \
        option("password", "root"). \
        option("encoding", "utf-8"). \
        save()
    result8.write.mode("overwrite").saveAsTable("averageExperience", "parquet")
    spark.sql("SELECT * FROM averageExperience").show()

    # #需求9 学历
    # result9 = jobData.groupBy("education").agg(
    #     count("*").alias("count")
    # )
    # result9.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "educationCount"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result9.write.mode("overwrite").saveAsTable("educationCount", "parquet")
    # spark.sql("SELECT * FROM educationCount").show()
    #
    #
    # #行业个数
    # result10 = jobData.groupBy("type").agg(
    #     count("*").alias("count")
    # )
    # result10.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "typeCount"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result10.write.mode("overwrite").saveAsTable("typeCount", "parquet")
    # spark.sql("SELECT * FROM typeCount").show()
    #
    # #需求11 各类型最大值
    # result11 = jobData.groupBy("type").agg(
    #     max(col("maxSalary")).alias("maxSalary")
    # )
    # result11.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "typeMax"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result11.write.mode("overwrite").saveAsTable("typeMax", "parquet")
    # spark.sql("SELECT * FROM typeMax").show()
    #
    # #需求12 城市薪资分布
    # conditions = [
    #     (col("maxSalary") <= 5000, '0-5000'),
    #     ((col("maxSalary") > 5000) & (col("maxSalary") <= 7000), '5000-7000'),
    #     ((col("maxSalary") > 7000) & (col("maxSalary") <= 10000), '7000-10000'),
    #     ((col("maxSalary") >= 10000) & (col("maxSalary") <= 20000), '10000-20000'),
    #     (col("maxSalary") > 20000, '20000以上')
    # ]
    # result12 = jobData.groupBy("city").agg(
    #     *[count(when(condition, 1)).alias(range_name) for condition, range_name in conditions]
    # )
    # result12.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "citySalary"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result12.write.mode("overwrite").saveAsTable("citySalary", "parquet")
    # spark.sql("SELECT * FROM citySalary").show()
    #
    # #城市人数
    # conditionsTwo = [
    #     (col("people_num") <= 10, '0-10'),
    #     ((col("people_num") >= 10) & (col("people_num") <= 50), '10-50'),
    #     ((col("people_num") >= 50) & (col("people_num") <= 150), '50-150'),
    #     ((col("people_num") >= 150) & (col("people_num") <= 500), '150-500'),
    #     ((col("people_num") >= 500) & (col("people_num") <= 1000), '500-1000'),
    #     (col("people_num") > 1000, '1000以上')
    # ]
    # result13 = job_df.groupBy("city").agg(
    #     *[count(when(condition, 1)).alias(range_name) for condition, range_name in conditionsTwo]
    # )
    #
    # result13.write.mode("overwrite"). \
    #     format("jdbc"). \
    #     option("url", "jdbc:mysql://node1:3306/bigdata?useSSL=false&useUnicode=true&charset=utf8"). \
    #     option("dbtable", "cityPeople"). \
    #     option("user", "root"). \
    #     option("password", "root"). \
    #     option("encoding", "utf-8"). \
    #     save()
    # result13.write.mode("overwrite").saveAsTable("cityPeople", "parquet")
    # spark.sql("SELECT * FROM cityPeople").show()
    #
    #
    #
    #
