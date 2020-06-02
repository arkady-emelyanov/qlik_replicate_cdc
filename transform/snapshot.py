import argparse

from helpers import get_spark

# 0. parse arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-d", "--delta-path", required=True, help="Delta table path")
arg_parser.add_argument("-s", "--snapshot-path", required=True, help="Table snapshot path")
cmd_args = arg_parser.parse_args()

# 1. load table and export parquet
spark = get_spark()

print(f"Load delta table from {cmd_args.delta_path}...")
df = spark.read.format("delta").load(cmd_args.delta_path)
df.show(10, False)

print(f"Storing snapshot in {cmd_args.snapshot_path}...")
df.write.mode("overwrite").parquet(cmd_args.snapshot_path)
print("Done!")
