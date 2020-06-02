from lib.args import get_args
from lib.spark import get_spark

cmd_args = get_args()
spark = get_spark()

# 1. load delta table
print(f"Load delta table from {cmd_args.delta_path}...")
df = spark.read.format("delta").load(cmd_args.delta_path)

# 2. export to parquet snapshot
print(f"Storing snapshot in {cmd_args.snapshot_path}...")
df.write.mode("overwrite").parquet(cmd_args.snapshot_path)

# 3. done
print("Done!")
