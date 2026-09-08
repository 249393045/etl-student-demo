import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("etl_run.log",encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_raw_csv():
     raw_data = {
        "name": ["张三", "李四", "王五", "赵六", "孙七", "周八"],
        "age": [20, 21, None, 22, 23, 21],
        "score": [95, -5, 72, 88, None, 66],
        "class_id": [1, 1, 2, 2, 3, 3]
    }
     df_raw = pd.DataFrame(raw_data)
     df_raw.to_csv("raw_student.csv", index=False, encoding="utf-8")
     logger.info("步骤1完成：生成原始脏数据 raw_student.csv")
     return df_raw

def clean_data():
    df = pd.read_csv("raw_student.csv",encoding="utf-8")
    df["age"] = df["age"].fillna(df["age"].mean())
    df["score"] = df["score"].fillna(0)
    df.loc[(df["score"]<0) | (df["score"]>100),"score"]=0
    df["level"] = np.where(df["score"]>90,"A",
                           np.where(df["score"]>80,"B",
                                    np.where(df["score"]>=60,"C","D")))
    logger.info("步骤2完成： 数据处理完毕")
    logger.info(f"\n{df}")
    return df

def init_mysql_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS etl_class;")
    create_class_sql = """
    CREATE TABLE etl_class(
        class_id INT PRIMARY KEY AUTO_INCREMENT,
        class_name VARCHAR(30),
        teacher VARCHAR(20)
    );
    """
    cursor.execute(create_class_sql)
    cursor.executemany("INSERT INTO etl_class(class_name, teacher) VALUES(%s, %s)", [
        ("一班", "王老师"),
        ("二班", "李老师"),
        ("三班", "张老师")
    ])
    cursor.execute("DROP TABLE IF EXISTS etl_student;")
    create_student_sql = """
                         CREATE TABLE etl_student \
                         ( \
                             id       INT PRIMARY KEY AUTO_INCREMENT, \
                             name     VARCHAR(20), \
                             age      INT, \
                             score    INT, \
                             level    CHAR(1), \
                             class_id INT
                         ); \
                         """
    cursor.execute(create_student_sql)
    logger.info("步骤3完成：MySQL建表完成")

def insert_to_mysql(df,cursor,conn):
    insert_sql="""
    INSERT INTO etl_student(name,age,score,level,class_id) VALUES(%s,%s,%s,%s,%s);
    """
    for _, row in df.iterrows():
        cursor.execute(insert_sql, (row["name"],row["age"],row["score"],row["level"],row["class_id"]))
    conn.commit()
    logger.info("步骤4成功：清洗后的数据入库完成")

def do_stat_report(conn):
    join_sql = """
    SELECT c.class_name, AVG(s.score) AS avg_score, MAX(s.score) AS max_score
    FROM etl_student s 
    LEFT JOIN etl_class c ON c.class_id = s.class_id
    GROUP BY c.class_name;
    """
    df_report = pd.read_sql(join_sql, conn)
    logger.info("完成JOIN班级统计报表")
    logger.info(f"\n{df_report}")
    df_report.to_csv("class_score.csv",index=False,encoding="utf-8")
    logger.info("报表导出,至 class_score.csv")
    plt.figure(figsize=(8,5))
    plt.bar(df_report["class_name"],df_report["avg_score"],color=["#4472C4","#ED7D31","#A5A5A5"])
    plt.title("各个班级平均分")
    plt.xlabel("班级")
    plt.ylabel("平均分")
    plt.grid(axis="y",alpha=0.3)
    plt.savefig("class_avg_score.png",dpi=150,bbox_inches='tight')
    plt.close()
    logger.info("图表保存 class_avg_score.png")
    join_left_sql = """
    SELECT c.class_name, AVG(s.score) as avg_score, Max(s.score) as max_score
    FROM etl_student s 
    LEFT JOIN etl_class c ON c.class_id = s.class_id
    WHERE s.score >= 60
    GROUP BY c.class_name;
    """
    test_insert = pd.read_sql(join_left_sql, conn)
    logger.info("\n几个学生班级统计")
    logger.info(f"\n{test_insert}")
    test_insert.to_csv("pass_class_report.csv",index=False,encoding="utf-8-sig")
    logger.info("已导出 pass_class_report.csv")

def main():
    conn = None
    cursor = None
    try:
        generate_raw_csv()
        df = clean_data()
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="python_etl",
            charset="utf8mb4"
        )
        cursor = conn.cursor()
        init_mysql_table(cursor)
        insert_to_mysql(df,cursor,conn)
        do_stat_report(conn)
        logger.info("全部ETL流程执行成功！")
    except Exception as e:
        logger.error(f"ETL程序发生异常：{str(e)}",exc_info=True)
        if conn:
            conn.rollback()         #出错回滚
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        logger.info("数据库连接已关闭")


if __name__ == "__main__":
    main()
