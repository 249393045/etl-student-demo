import pandas as pd
import os
import shutil
import numpy as np
import argparse
import logging
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
logging.basicConfig()
# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("etl_clean.log",encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger(__name__)

parser = argparse.ArgumentParser(description= "学生数据ETL清洗自动化脚本，仅CSV版本")
parser.add_argument("--input",required=True,help="原始csv文件路径")
parser.add_argument("--output",default="clean_result.csv",help="清洗完成输出csv路径")
args = parser.parse_args()

try:
    input_file = args.input
    if os.path.isfile(input_file) and "bak" not in input_file:
        name, ext = os.path.splitext(input_file)
        bak_file = f"{name}_bak{ext}"
        shutil.copy(input_file, bak_file)
        logger.info(f"原始文件已备份:{input_file}->{bak_file}")

    logger.info(f"开始ETL任务,读取csv文件{args.input}")
    df = pd.read_csv(args.input)
    logger.info(f"数据读取成功,共{len(df)}行")

    # ========== 数据清洗逻辑 ==========
    df["score"] = df["score"].fillna(0)
    logger.info(f"分数缺失部分填充完毕")

    df.loc[(df["score"] < 0) | (df["score"] > 100), "score"] = 0
    logger.info(f"异常分数修正完成")

    df["level"] = np.where(df["score"] > 90, "A",
                           np.where(df["score"] > 80, "B",
                                    np.where(df["score"] > 60, "C", "D")))
    logger.info(f"成绩等级计算完成")

    df = df[df["score"]>0]
    logger.info(f"过滤缺考学生,剩余有效数据{len(df)}行")

    # 输出csv文件
    df.to_csv(args.output, index=False, encoding="utf-8")
    logger.info(f"数据清洗完成,结果保存至{args.output}")

    # 透视表
    df_pivot = df.pivot_table(index="class_id",columns="level",values="score",aggfunc="mean")
    logger.info(f"创建透视表成功")
    print(f"\n透视表:{df_pivot}")

    # 绘图
    df_report = df.groupby("class_id")["score"].agg(avg_score="mean").reset_index()
    plt.figure(figsize=(8,5))
    plt.bar(df_report["class_id"], df_report["avg_score"], color=["#4472C4","#ED7D31","#A5A5A5"])
    plt.title("每个班级平均值")
    plt.xlabel("班级")
    plt.ylabel("平均值")
    plt.grid(axis="y",alpha=0.3)
    plt.savefig("test.png",bbox_inches="tight")
    plt.close()
    logger.info(f"可视化视图创建完成:'test.png'")

except Exception as e:
    logger.error(f"ETL任务失败:{str(e)}",exc_info=True)
