import csv
import json


def csv_file_to_json(csv_file_path, json_file_path):
    data = []
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"成功将 {csv_file_path} 转换为 {json_file_path}")
    except FileNotFoundError:
        print(f"错误：未找到文件 {csv_file_path}")
    except Exception as e:
        print(f"发生未知错误：{e}")


# 请替换为实际的 CSV 文件路径
csv_file_path = 'data/kumo/relative_action_count.csv'
# 请替换为实际想要保存的 JSON 文件路径
json_file_path = 'relative_action_count.json'
csv_file_to_json(csv_file_path, json_file_path)