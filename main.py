import argparse
import boto3
from pathlib import Path
import random
import sys


file_list = Path(__file__).parent / "object_list.txt"
client = boto3.client("s3")

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-refresh", action="store_true", help="Refresh the list of objects")
parser.add_argument(
    "--bucket", type=str, help="Bucket name", required="-refresh" in sys.argv
)
parser.add_argument(
    "-show-random", action="store_true", help="Show a random object. Save to show.jpeg"
)


def find_newest_objects():
    # find the most recently created objects in bucket

    paginator = client.get_paginator("list_objects_v2")
    result = paginator.paginate(Bucket=bucket)
    objects = {}
    for idx, page in enumerate(result):
        for obj in page["Contents"]:
            objects[obj["Key"]] = obj["LastModified"]
    return objects


def dump_objects(objects):

    # sort objects by value and return the keys
    objects = sorted(objects.items(), key=lambda x: x[1], reverse=True)[:5000]
    objects = [x[0] for x in objects]
    file_list.write_text("\n".join(objects))


def download_random_obj():
    objects = file_list.read_text()
    objects = objects.split("\n")
    obj = random.choice(objects)
    client.download_file(bucket, obj, "show.jpeg")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.refresh:
        bucket = args.bucket
        # dump_objects(find_newest_objects(bucket))
    elif args.show_random:
        download_random_obj()
